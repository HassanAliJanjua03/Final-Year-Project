# Project setup

My workflow starts with the SolidWorks assembly, continues through the Arduino/GRBL motion-control system and MATLAB modeling, and ends with sensor monitoring and the virtual robot in Unity.

1. Read the [project report](../2118-Design%20and%20Development%20of%20Digital%20Twin%20of%20a%20Robot%20Tower.pdf) and inspect the [hardware setup](../hardware/original/README.md).
2. Open the SLX files in a compatible installation of MATLAB, Simulink, Simscape and Simscape Multibody. The [model index](media-inventory.md) lists the original model filenames.
3. For the [kinematics and joint response scripts](../simulation/README.md), install Peter Corke's Robotics Toolbox and use verified geometry, joint limits and logging settings.
4. Configure the [telemetry bridge](../telemetry/README.md) with a test broker and InfluxDB bucket, then create the Grafana panels.
5. For [Unity 3D](../unity/README.md), configure the virtual joint hierarchy and replay calibrated joint-state measurements in a copy of the scene.

The rebuilt code needs system-specific configuration and runtime validation. The archived G-code is for reference; verify hardware limits and firmware before use.
