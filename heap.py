import math
for _ in range(int(input())):
    msn=int(input())
    l1=[];l2=[]
    for i in range(msn//2):
        if i%2:
            l1.append(1)
            l2.append(3)
        else:
            l1.append(3)
            l2.append(1)
    if msn%2:

        print(*(l1+[0]+l2[::-1]))
    else:
        print(*(l1+l2[::-1]))
