





from itertools import product, permutations,combinations


N = input()
ans=0

for pro in product((0,1), repeat=len(N)):
    first = []
    second = []
    for i,b in enumerate(pro):
        if b==1:
            first.append(N[i])
        else:
            second.append(N[i])
    if len(first) ==0 or len(second) ==0:
        continue
    first.sort(reverse=True)
    second.sort(reverse=True)
    a=int("".join(first))
    b=int("".join(second))
    ans=max(ans,a*b)
print(ans)


# print(pro)
# print(i,b)
# (0, 0, 0, 0)
# 0 0
# 1 0
# 2 0
# 3 0
# (0, 0, 0, 1)
# 0 0
# 1 0
# 2 0
# 3 1
# (0, 0, 1, 0)
# 0 0
# 1 0
# 2 1
# 3 0
# (0, 0, 1, 1)
# 0 0
# 1 0
# 2 1
# 3 1
# (0, 1, 0, 0)
# 0 0
# 1 1
# 2 0
# 3 0
# (0, 1, 0, 1)
# 0 0
# 1 1
# 2 0
# 3 1
# (0, 1, 1, 0)
# 0 0
# 1 1
# 2 1
# 3 0
# (0, 1, 1, 1)
# 0 0
# 1 1
# 2 1
# 3 1
# (1, 0, 0, 0)
# 0 1
# 1 0
# 2 0
# 3 0
# (1, 0, 0, 1)
# 0 1
# 1 0
# 2 0
# 3 1
# (1, 0, 1, 0)
# 0 1
# 1 0
# 2 1
# 3 0
# (1, 0, 1, 1)
# 0 1
# 1 0
# 2 1
# 3 1
# (1, 1, 0, 0)
# 0 1
# 1 1
# 2 0
# 3 0
# (1, 1, 0, 1)
# 0 1
# 1 1
# 2 0
# 3 1
# (1, 1, 1, 0)
# 0 1
# 1 1
# 2 1
# 3 0
# (1, 1, 1, 1)
# 0 1
# 1 1
# 2 1
# 3 1
# 1312