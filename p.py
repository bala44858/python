
for _ in range(int(input())):
    n=int(input())
    for i in range(n):
        s=input()
        if s[i]=="0":
            print("1",end="")
        else:
            print("0",end="")
    print('')