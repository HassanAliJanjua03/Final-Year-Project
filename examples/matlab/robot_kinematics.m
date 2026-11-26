function [robot,T,qIK] = robot_kinematics(dh,q,qlim,target,mask)
% Supplementary example, NOT the original robot model.
% dh: 4x4 [theta d a alpha] standard DH rows, metres and radians.
% q: four joint coordinates (rad,m,m,rad); qlim: 4x2 joint limits.
% For revolute links, theta is treated as an offset; for prismatic
% links, d is treated as an offset. target: RTB SE3 or 4x4 pose.
% mask: 1x6 binary task-space mask with exactly 4 selected components.
% Requires Peter Corke Robotics Toolbox; use measured CAD parameters.
validateattributes(dh,{'numeric'},{'size',[4,4],'finite','real'});
validateattributes(q,{'numeric'},{'numel',4,'finite','real'});
validateattributes(qlim,{'numeric'},{'size',[4,2],'finite','real'});
assert(all(qlim(:,1)<qlim(:,2)),'Invalid joint limits.');
q = q(:)';
assert(all(q>=qlim(:,1)' & q<=qlim(:,2)'),'Initial q outside limits.');
sigma = [0 1 1 0];
for i=1:4
    if sigma(i)==0
        L(i)=Link([0 dh(i,2) dh(i,3) dh(i,4) 0 dh(i,1)],'standard'); %#ok<AGROW>
    else
        L(i)=Link([dh(i,1) 0 dh(i,3) dh(i,4) 1 dh(i,2)],'standard'); %#ok<AGROW>
    end
    L(i).qlim=qlim(i,:);
end
robot=SerialLink(L,'name','Robot Tower (configured example)');
T=robot.fkine(q);
qIK=[];
if nargin>=4 && ~isempty(target)
    assert(nargin==5 && numel(mask)==6 && all(ismember(mask,[0 1])) && nnz(mask)==4,...
        'Select four attainable task components.');
    qIK=robot.ikine(target,'q0',q,'mask',mask);
    assert(numel(qIK)==4 && all(isfinite(qIK)),'IK did not return a valid solution.');
    qIK=qIK(:)';
    assert(all(qIK>=qlim(:,1)' & qIK<=qlim(:,2)'),'IK violates configured joint limits.');
    % Verify achieved pose against the selected task and tolerances before use.
end
end
