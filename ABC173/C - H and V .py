







from itertools import product

h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]

ans = 0

# 全探索ok
for i in product(range(2),repeat=h):
    for j in product(range(2),repeat=w):
        cnt = 0
        for row in range(h):
            for col in range(w):
                # 元から黒かつ、どちらも選ばれていない==(1and1)
                if c[row][col]=="#" and (i[row] and j[col]):
                    cnt+=1
                    # print(i[row] , j[col])
        if cnt==k:
            ans+=1
print(ans)