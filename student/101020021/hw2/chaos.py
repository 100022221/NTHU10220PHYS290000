
from pylab import *


x=0.5
r=arange(1,4,0.01)


for i in range(1000) :
    x=r*x*(1-x)
    
plot(r,x)
show()
