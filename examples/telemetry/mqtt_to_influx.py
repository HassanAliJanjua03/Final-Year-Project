"""Supplementary read-only telemetry bridge. No robot motion commands."""
import json
import logging
import math
import os

import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

FIELDS = ("acc_x", "acc_y", "acc_z", "gyro_x", "gyro_y", "gyro_z", "temperature")
logging.basicConfig(level=logging.INFO)

def make_point(payload):
    data = json.loads(payload)
    if not isinstance(data, dict):
        raise ValueError("JSON object required")
    point = Point("robot_sensors")
    count = 0
    for name in FIELDS:
        value = data.get(name)
        if isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value):
            point.field(name, float(value))
            count += 1
    if not count:
        raise ValueError("No valid sensor values")
    stamp = data.get("timestamp_ns")
    if stamp is not None:
        if type(stamp) is not int or stamp <= 0 or stamp > 2**63 - 1:
            raise ValueError("Expected positive Unix nanoseconds")
        point.time(stamp, WritePrecision.NS)
    return point

def main():
    topic = os.environ["MQTT_TOPIC"]
    url = os.environ["INFLUX_URL"]
    if not url.startswith("https://"):
        raise ValueError("Use HTTPS for the InfluxDB endpoint")
    with InfluxDBClient(url=url, token=os.environ["INFLUX_TOKEN"],
                        org=os.environ["INFLUX_ORG"]) as db:
        with db.write_api(write_options=SYNCHRONOUS) as writer:
            def connected(client, userdata, flags, reason_code, properties):
                if not reason_code.is_failure:
                    client.subscribe(topic, qos=1)
                else:
                    logging.error("MQTT connection refused: %s", reason_code)
            def received(client, userdata, message):
                try:
                    point = make_point(message.payload)
                    writer.write(bucket=os.environ["INFLUX_BUCKET"], record=point)
                except (ValueError, TypeError, OverflowError):
                    logging.warning("Invalid sensor record; skipped")
                except Exception:
                    logging.error("Sensor record could not be written")
            client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
            client.username_pw_set(os.environ["MQTT_USERNAME"], os.environ["MQTT_PASSWORD"])
            client.tls_set()
            client.on_connect = connected
            client.on_message = received
            client.connect(os.environ["MQTT_HOST"], int(os.getenv("MQTT_PORT", "8883")))
            try:
                client.loop_forever()
            finally:
                client.disconnect()

if __name__ == "__main__":
    main()
