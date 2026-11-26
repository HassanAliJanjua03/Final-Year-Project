function plot_joint_responses(model)
% Plot the four-joint simulation responses in one figure.
if nargin==0, model='robot_tower'; end
out=sim(model);
units={'Angle (deg)','Displacement (m)','Displacement (m)','Angle (deg)'};
figure('Name','Four-joint response','Color','w');
for k=1:4
    name=sprintf('Joint%d',k);
    s=out.get(name);
    if isa(s,'timeseries')
        t=s.Time; y=s.Data;
    elseif isnumeric(s)
        t=out.tout; y=s;
    elseif isstruct(s) && isfield(s,'time') && isfield(s,'signals')
        t=s.time; y=s.signals.values;
    else
        error('Unsupported format for %s. Inspect logged output.',name);
    end
    y=squeeze(y);
    assert(isvector(y) && numel(t)==numel(y),'Unexpected signal dimensions for %s.',name);
    subplot(2,2,k);
    plot(t(:),y(:),'LineWidth',1.5);
    xlabel('Time (s)'); ylabel(units{k});
    title(sprintf('Joint %d',k)); grid on;
end
% Units follow the original plotting labels; confirm converter settings.
end
