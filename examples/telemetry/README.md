# MQTT to InfluxDB — reference example

This is a new example, not the original microcontroller firmware or database client. The bridge expects a JSON message with numeric `acc_x`, `acc_y`, `acc_z`, `gyro_x`, `gyro_y`, `gyro_z`, `temperature` fields (at least one present), and optionally `timestamp_ns`. No physical command topic is used. Sensor units and calibration must be defined by the sender.

Install: `python -m pip install -r requirements.txt`.

Set MQTT_HOST, MQTT_PORT (default 8883), MQTT_TOPIC, MQTT_USERNAME, MQTT_PASSWORD, INFLUX_URL, INFLUX_TOKEN, INFLUX_ORG and INFLUX_BUCKET in environment variables. Use a TLS broker and an HTTPS InfluxDB endpoint with valid certificates. Run `python mqtt_to_influx.py`. Use a least-privilege token and a test bucket. No secrets belong in GitHub.

Configure Grafana's InfluxDB data source and plot the `robot_sensors` measurement by field. For Unity, use calibrated joint-position records via an authenticated service or offline replay; do not map raw IMU values directly to position. This example does not estimate joint state or implement the missing original live Unity integration.
