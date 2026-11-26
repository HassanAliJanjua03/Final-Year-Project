"""Offline checks with synthetic messages; no hardware or network required."""
import unittest
from sensor_data import parse_sensor_data


class SensorDataTests(unittest.TestCase):
    def test_numeric_fields(self):
        fields, stamp = parse_sensor_data('{"acc_x":9.81,"gyro_y":0,"temperature":22}')
        self.assertEqual(fields, {"acc_x": 9.81, "gyro_y": 0.0, "temperature": 22.0})
        self.assertIsNone(stamp)

    def test_timestamp(self):
        fields, stamp = parse_sensor_data('{"acc_x":1,"timestamp_ns":1733443200000000000}')
        self.assertEqual(fields, {"acc_x": 1.0})
        self.assertEqual(stamp, 1733443200000000000)

    def test_ignores_invalid_fields(self):
        fields, _ = parse_sensor_data('{"acc_x":true,"acc_y":NaN,"acc_z":"2","temperature":20}')
        self.assertEqual(fields, {"temperature": 20.0})

    def test_no_valid_fields(self):
        for raw in ('{}', '{"acc_x":null}', '{"acc_x":Infinity}', '{"acc_x":true}'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                parse_sensor_data(raw)

    def test_invalid_timestamp(self):
        for stamp in ("0", "-1", "true", "1.5", "9223372036854775808"):
            with self.subTest(stamp=stamp), self.assertRaises(ValueError):
                parse_sensor_data('{"acc_x":1,"timestamp_ns":' + stamp + '}')

    def test_invalid_json(self):
        for raw in ('[1,2]', 'not json', 'null'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                parse_sensor_data(raw)


if __name__ == "__main__":
    unittest.main()
