from re import L


for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans=[]
    for i in range(1,n):
        if l[i]!=l[i-1]:
            ans.append(i)
            ans.append(i-1)
    print(len(set(ans)))
