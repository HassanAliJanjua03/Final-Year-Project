"""Validate sensor messages before writing them to the time-series database."""
import json
import math

FIELDS = ("acc_x", "acc_y", "acc_z", "gyro_x", "gyro_y", "gyro_z", "temperature")
MAX_TIMESTAMP = 2**63 - 1


def parse_sensor_data(payload):
    """Return a dictionary of finite numeric fields and an optional timestamp."""
    data = json.loads(payload)
    if not isinstance(data, dict):
        raise ValueError("Expected a JSON object")

    fields = {}
    for key in FIELDS:
        value = data.get(key)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            try:
                number = float(value)
            except OverflowError:
                continue
            if math.isfinite(number):
                fields[key] = number
    if not fields:
        raise ValueError("No valid sensor values")

    stamp = data.get("timestamp_ns")
    if stamp is not None and (type(stamp) is not int or not 0 < stamp <= MAX_TIMESTAMP):
        raise ValueError("Expected positive Unix nanoseconds")
    return fields, stamp
