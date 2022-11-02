l=list(map(int,input().split()))
k=int(input())
import math 
c=0
for i in range(len(l)):
    gcd=0
    
    for ind in range(i,len(l)):
        # print(gcd)
        gcd=math.gcd(gcd,l[i])
        if gcd==k:
            c+=1
            print(i,ind, "gcd=",gcd)
print(c)
        