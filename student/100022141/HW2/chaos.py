import math

L=60
i=-L
j=-L
k=-L
summary=0.0

while i<=L:
    while j<=L:
        while k<=L:
            if i==j and j==k and k==0:
               summary = summary 
            elif (i+j+k)%2==0:
                summary=summary+(i**2+j**2+k**2)**(-0.5)
            else:
                summary=summary-((i**2+j**2+k**2)**(-0.5))
            k=k+1
        j=j+1
        k=-L
    i=i+1
    j=-L
    
print summary



