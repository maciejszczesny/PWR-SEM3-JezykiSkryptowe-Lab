x = [-2*pi:0.1:2*pi];
y = sin(x);
z = cos(x);
subplot(2,1,1)
plot(x,y,'b+;sinus;');
grid on;
subplot(2,1,2);
plot(x,z,'g;cosinus;');
grid on;