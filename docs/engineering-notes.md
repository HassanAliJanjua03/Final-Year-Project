# Engineering notes

## Mechanical and electrical design

I modeled the robot tower as an R-P-P-R mechanism. The first and fourth joints are revolute; the second and third are prismatic. Joint axes and dimensions must be verified against the actual CAD assembly before reproducing the kinematics. My system uses Arduino Uno for motion control and ESP32 for data acquisition, with a CNC shield, four drivers and four motors. The ESP32 collects and holds the sensor readings and transmits them over Wi-Fi to InfluxDB. MQTT is shown in my original system diagram; the exact firmware and transport configuration must be checked before reproducing it. It also identifies accelerometer, gyroscope, force, pressure and temperature sensors. The available database screenshots directly show acceleration, angular-rate and temperature fields.

## Actuator model

My stepper motor model (`untitled1.slx`) includes the following components. Its root system includes a stepper motor, switches, pulse generators, inertia, leadscrew, mass, rotational sensor, voltage sources and a transfer function with denominator `[0.000002327 0 0]`. Logged variables: Voltage, Current, Torque, AngularVelocity, Position, Phase1–Phase4. The screenshot shows the numerator 1. For an ideal inertial plant, angular displacement divided by applied torque is 1/(J s²); this interpretation assumes negligible damping and consistent SI units.

## PID controller settings

These are the saved controller settings in my `robot_tower.slx` model. The table identifies block names, not an independently verified controller-to-joint wiring map. These are stored simulation settings, not physical hardware gains.

| Block | P | I | D | N |
| --- | ---: | ---: | ---: | ---: |
| PID Controller | 2.03373501035354 | 1420.30148070152 | 0.000652316044116742 | 121852.047353829 |
| PID Controller1 | 5780742.55423266 | 22528675.7526367 | 367897.490308388 | 8619.03438265045 |
| PID Controller2 | 12391278.5337553 | 94475183.8411176 | 395685.412435965 | 583.989577885221 |
| PID Controller3 | 2.03373501035354 | 1420.30148070152 | 0.000652316044116742 | 121852.047353829 |

The model also contains two revolute joints, two prismatic joints, four sine-wave references, four summing blocks and logged variables Joint1–Joint4. The simulation should be rerun before using these values for another robot configuration. Large gains may reflect the model's force/torque scaling and must not be copied directly to real hardware.

## Kinematics

For standard DH convention, the link transform is RotZ(theta) TransZ(d) TransX(a) RotX(alpha). The end-effector transform is the product of the four link transforms. Revolute joints vary theta; prismatic joints vary d. Forward kinematics maps a known configuration to pose. Inverse kinematics solves for a configuration consistent with a reachable target and joint limits. An R-P-P-R mechanism has four actuated degrees of freedom, so an arbitrary six-dimensional pose is not generally reachable.

## Digital twin and limitations

Use timestamps and coordinate conventions consistently. A dashboard displays acquired sensor readings; a virtual-motion controller requires calibrated joint states (or a validated estimator). Acceleration integration drifts; gyroscope integration also drifts. Use appropriate position/angle measurements or validated fusion, and account for sample rate, calibration, delays and dropped data. No latency or accuracy figures are inferred from the screenshots. The wiring illustration is a reference diagram; check the component documentation before adapting the circuit.
