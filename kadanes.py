for _ in range(int(input())):
    s=input()
    a1="";a2=""
    for i in s:
        a1+=i
        a2=i+a2
    # print(a2)
    print(a1+a2)
