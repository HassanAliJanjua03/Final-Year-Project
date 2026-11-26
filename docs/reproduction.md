# How to explore the project

1. Read the original report and retain its academic attribution. The original RAR archives are still at the repository root.
2. Review the CAD and prototype photos in the separately supplied media package.
3. Inspect the archived G-code before running anything. Check firmware, axis mapping, limit switches, motor-driver current limits and feed rates. Do not execute the archived sequence blindly.
4. Open the supplied SLX models in a compatible MATLAB installation with Simulink, Simscape, Simscape Multibody and applicable electrical/stepper-motor libraries. The models were structurally inspected, not simulated here. Place `robot_tower.slx` on MATLAB's path before running the original plotting script.
5. For the supplementary MATLAB kinematics example, install Peter Corke's Robotics Toolbox and supply verified DH data and joint limits. The example uses standard DH convention.
6. In Unity 2019.3.5f1 or a compatible version, inspect the original scripts. The original controller snippet is incomplete. Use the separate replay example with a calibrated joint-state CSV file. It moves only virtual objects.
7. For the telemetry example, install Python dependencies from its requirements file and set broker/InfluxDB configuration via environment variables. Start with a test broker and bucket; do not expose credentials or public hardware control endpoints.

Original binaries and visual materials are listed in [the media inventory](media-inventory.md). Until they are uploaded, only the original root archives, report, documentation and text source are available online.
