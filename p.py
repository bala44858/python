l=[1,2,3,4,5]
m=max(l)
mm=-10**9
for i in l:
    if i!=m:
        mm=max(mm,i)
print(mm)