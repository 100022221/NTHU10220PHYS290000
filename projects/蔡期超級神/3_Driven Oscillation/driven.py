from pylab import*
from math import*
x0=10
v0=20
w=2
w0=0.2
b=10
t=0 #initial time
h=0.01 #time step size
F=100

xdat=[]
vdat=[]#velocity data store here
time=[]#time stored here

v0=v0+h*(-w*w*x0-b*v0+F*math.cos(w0*t))/2

while(t<=50):
   
    x1=x0+h*v0
    v1=v0+h*(-w*w*x1-b*v0+F*math.cos(w*t))
   
    xdat.append(x1)
    vdat.append(v1)
    time.append(t)
    x0=x1
    v0=v1
    t=t+h
   
figure(1)
title("Driven harmonic oscillator motion")
xlabel(" Time")
ylabel("x")
plot(time,xdat)
grid(True)
figure(2)
title("Driven harmonic oscillator motion")
xlabel("Time")
ylabel("Velocity")
plot(time,vdat)
grid(True)
figure(3)
title("Driven harmonic oscillator motion")
xlabel("x")
ylabel("velocity")
plot(xdat,vdat)
grid(True)

show()
