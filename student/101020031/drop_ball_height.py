import math

def the_height(h,t):  
    g=9.8            #�[�t��         
    a=t**2
    s=g*a/2          #�p�y�첾
    H=h-s
    b=2(H+s)/g
    c=math.sqrt(b)   #�q����h�U����a�O�Ҫ�ɶ�
    print"enter h the height of tower,then after t time,the height of the ball is"
    return H
    print"the time the ball takes until it hits the ground is"
    return c
    
