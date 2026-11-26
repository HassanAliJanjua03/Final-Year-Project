clc
clear all
close all
% Run the Simulink model
simOut = sim('robot_tower'); % Replace 'untitled1' with your model name if changed

% Extract the Joint1 from the workspace
time = simOut.tout;      % Simulation time
Joint1 = simOut.Joint1; % Voltage data from the workspace

% Plot Joint1 signal
figure;
plot(time, Joint1, 'b', 'LineWidth', 1.5); % 'r' sets yellow color for the plot
xlabel('Time (s)');
ylabel('Joint Angle (deg)');
title('Position of Joint-1 vs Time');
grid on;

% Extract the Joint2 from the workspace
time = simOut.tout;      % Simulation time
Joint2 = simOut.Joint2; % Voltage data from the workspace

% Plot Joint2 signal
figure;
plot(time, Joint2, 'b', 'LineWidth', 1.5); % 'r' sets yellow color for the plot
xlabel('Time (s)');
ylabel('Linear Displacement (m)');
title('Position of Joint-2 vs Time');
grid on;

% Extract the Joint3 from the workspace
time = simOut.tout;      % Simulation time
Joint3 = simOut.Joint3; % Voltage data from the workspace

% Plot Joint3 signal
figure;
plot(time, Joint3, 'b', 'LineWidth', 1.5); % 'r' sets yellow color for the plot
xlabel('Time (s)');
ylabel('Linear Displacement (m)');
title('Position of Joint-3 vs Time');
grid on;

% Extract the Joint4 from the workspace
time = simOut.tout;      % Simulation time
Joint4 = simOut.Joint4; % Voltage data from the workspace

% Plot Joint4 signal
figure;
plot(time, Joint4, 'b', 'LineWidth', 1.5); % 'r' sets yellow color for the plot
xlabel('Time (s)');
ylabel('Joint Angle (deg)');
title('Position of Joint-4 vs Time');
grid on;
