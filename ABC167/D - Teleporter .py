





# 周期、余り

N,K = map(int,input().split())
A = list(map(int, input().split()))


seen = [(-1,0)] *(N+1)
seen[0] = (1,0)
seen[1] = (1,0)
# ループまで何回か
tmp = 0
d = 0
i=0
while K>0:
    # 次の町x
    x = A[i]
    if seen[x][0]==-1:
        tmp+=1
        seen[x] = (1,tmp)
        i = x-1
        if tmp==K:
            print(x)
            exit()
    # ループ突入
    else:
        # d = 今のtmp+1-前回xが出た時のtmp
        nowtmp = tmp+1
        pretmp = seen[x][1]
        d = nowtmp -pretmp 
        # print(nowtmp,pretmp,d)
        K = K-pretmp
        # print(K)
        s = K%d
        # print(s)
        now = A[i]
        for j in range(s):
            nex = A[now-1]
            now = nex
        print(now)
        exit()
            




# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# num = 1
# li = [1]
# flag = [True] * n
# flag[0] = False

# for i in range(k):
#     num = a[num-1]
#     if flag[num-1]:
#         li.append(num)
#         flag[num-1] = False
#     else:
#         break

# d = li.index(num)
# ans = (k-d)%(len(li)-d)+d

# print(li[ans])