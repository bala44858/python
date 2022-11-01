# kadanes algorithm for finding the maximum sum of sub array 
n=int(input())
l=list(map(int,input().split()))
max_final=l[0]
current_sum=0
for i in l:
    current_sum+=i
    max_final=max(max_final,current_sum)
    if current_sum<0:
        current_sum=0
print(max_final)