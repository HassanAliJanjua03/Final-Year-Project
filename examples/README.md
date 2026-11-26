# Supplementary reference implementations

These examples were prepared for the portfolio redesign, not recovered from the original project. They are intended as starting points and have not been tested against the physical robot, MATLAB or Unity runtime. They do not command physical hardware.

- [MATLAB kinematics](matlab/robot_kinematics.m) — standard DH, forward/inverse kinematics with supplied geometry.
- [MATLAB joint plotting](matlab/plot_joint_responses.m) — simulation output plotting.
- [MQTT/InfluxDB telemetry](telemetry/README.md) — authenticated telemetry bridge.
- [Unity replay](unity/README.md) — map calibrated recorded joint states to a virtual model.
