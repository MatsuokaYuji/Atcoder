


N,M = map(int,input().split())


from itertools import product, permutations,combinations

cond = []
for i in range(M):
    a,b = map(int,input().split())
    cond.append((a,b))

K = int(input())
dish = []
for i in range(K):
    c,d = map(int,input().split())
    dish.append((c,d))


ans=0
for bit in product((True, False), repeat=K):
    s = set()
    # print(bit)
    for i in range(K):
        if bit[i]:
            s.add(dish[i][0])
        else:
            s.add(dish[i][1])
    
    tmpans = 0 
    for a,b in cond:
        if a in s and b in s:
            tmpans+=1
    ans = max(ans,tmpans)
            


print(ans)
