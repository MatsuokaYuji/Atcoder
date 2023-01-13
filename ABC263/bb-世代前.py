N = int(input())


P =[0] + [0]+ list(map(int, input().split()))



i = N

count=1

while P[i]!=1:
    count+=1
    i = P[i]

print(count)