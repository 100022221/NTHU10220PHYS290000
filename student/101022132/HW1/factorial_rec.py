import math
def factorial_rec(n):
    if not isinstance(n,int):
        print '�A���D�o���O��ƹ�'
    else:
        x=1
        answer=1
        while x<=n:
            answer=answer*x
            x=x+1
        print answer
        
    
