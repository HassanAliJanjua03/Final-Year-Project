# Digital Twin of a 4-DOF Robot Tower

**Robotics · Digital Twin · Industrial IoT**

Bachelor's final-year engineering project integrating a physical R-P-P-R robot tower with a virtual representation and monitoring tools.

```mermaid
flowchart LR
 A[Physical robot] --- B[Arduino / GRBL]
 B --- C[Digital twin integration]
 C --- D[Unity 3D]
 C --- E[Telemetry and monitoring]
```

## Engineering highlights

- Physical robot actuation using Arduino, GRBL and stepper motor drives.
- Unity 3D virtual representation of the robot.
- MATLAB modeling and integration; InfluxDB and Grafana for telemetry and visualization.

## System overview

| Subsystem | Role |
| --- | --- |
| Robot tower (R-P-P-R) | Two rotary and two prismatic joints |
| Arduino / GRBL | Motion-command interface and stepper drive control |
| Unity 3D | Virtual robot representation |
| MATLAB | Modeling and integration |
| InfluxDB / Grafana | Time-series telemetry and monitoring |

The project brings together mechanical design, motion control, virtual modeling and industrial data visualization. The architecture diagram is a functional overview, not a verified communication or wiring schematic.

## Project files

| File | Purpose |
| --- | --- |
| [2118-Design and Development of Digital Twin of a Robot Tower.pdf](2118-Design%20and%20Development%20of%20Digital%20Twin%20of%20a%20Robot%20Tower.pdf) | Engineering report (PDF) |
| [2118-Design and Development of Digital Twin of a Robot Tower.docx](2118-Design%20and%20Development%20of%20Digital%20Twin%20of%20a%20Robot%20Tower.docx) | Editable engineering report |
| [FYP-1.rar](FYP-1.rar) | Original compressed deliverables |
| [FYP-II.rar](FYP-II.rar) | Original compressed deliverables |

## How to explore or reproduce

Read the project report first. The two RAR archives contain the original project deliverables; extract them locally and inspect their dependencies before running. Hardware configuration and calibration are required for physical operation.

## Scope and limitations

The repository is an archive of project deliverables, not yet a standalone installation package. A versioned setup guide, unpacked source tree and measured synchronization performance would make the project easier to reproduce.

## Portfolio

[Hassan Ali Janjua — Engineering portfolio](https://github.com/HassanAliJanjua03)
