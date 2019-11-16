x = [-pi:0.1:pi]; #brzeg x
y = [-pi:0.1:pi]; #brzeg y
[X,Y] = meshgrid(x,y);
Z = sin(X).*cos(Y);
mesh(x,y,Z);