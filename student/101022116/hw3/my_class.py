from math import * 

class Point:
    def __init__(self):
        self.data = []
    def __init__(self,xi,yi):
        self.x = xi
        self.y = yi
    def __add__(self,P1):
        P2 = Point(0,0)
        P2.x = self.x + P1.x
        P2.y = self.y + P1.y
        return P2
    def __sub__(self,P1):
        P2 = Point(0,0)
        P2.x = self.x - P1.x
        P2.y = self.y - P1.y
        return P2
    def f (self):
        print self.x , self.y
        return self
    def dist(self , x0 = 0 , y0 = 0):
        dx , dy = self.x - x0 , self.y - y0
        return sqrt(dx*dx*1.+dy*dy*1.)
        
def distance_between_points(P1 , P2):
    dP = P1 - P2
    ans =dP.dist()
    return ans
    
P1 = Point(1.0,0.0)
P1.f()
P2 = Point(0.0,1.0)
P2.f()
print distance_between_points(P1,P2)

class Rectangle:
    def __init__(self):
        self.l = []
        self.p = []
    def __init__(self,P,L):
        self.l = L
        self.p = Point(P.x,P.y)
    def __eq__(self,Rect):
        self.l = Rect.L
        self.p = Rect.P
    def f (self):
        print'Pos:',[self.p.x,self.p.y],'Len:',self.l
        return self
    def move_rectangle(self,dx,dy):
        self.p = self.p + Point(dx,dy)
        return self
    def move_rectangle_c(self,dx,dy):
        ans = Rectangle(Point(0,0),R1.l)
        ans.p = self.p + Point(dx,dy)
        return ans

R1 = Rectangle(Point(1,1),[1,1])
R1.f()
R1.move_rectangle(1,1)
R1.f()
R2 = R1.move_rectangle_c(10,10)
    
