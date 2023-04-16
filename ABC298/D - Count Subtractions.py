# q = int(input())
# s = 1
# ans = []
# ad = [1]
# la = 1
# p = 0
# for _ in range(q):
#     query = list(map(int,input().split()))
#     if query[0] == 1:
#         s = (s*10 + query[1]) % 998244353
#         ad.append(query[1])
#         la += 1
#     elif query[0] == 2:
#         s = (s - ad[p]*pow(10,(la - p - 1), 998244353)) % 998244353
#         p += 1
#     else:
#         ans.append(s % 998244353)

# for i in ans:
#     print(i)


# MOD=998244353
# M=600010
# p10=[1]*M
# for i in range(1,M):
#   p10[i]=p10[i-1]*10%MOD

# S=[1]
# pos=0
# val=1
# Q=int(input())
# for _ in range(Q):
#   q=input()
#   if q[0]=='1':
#     d=int(q[2])
#     S.append(d)
#     val=(val*10+d)%MOD
#   elif q[0]=='2':
#     L=len(S)-pos-1
#     val=(val-S[pos]*p10[L])%MOD
#     pos+=1
#   else:
#     print(val)


MOD = 998244353
Q = int(input())
M = 6*10**5+2
p10 = [1]*M
# 10**Xを前処理
for i in range(1,M):
    p10[i] = p10[i-1]*10%MOD
# print(p10)

S = [1]
pos = 0
ans = 1

for _ in range(Q):
    q = input()
    if q[0]=="1":
        d = int(q[2])
        S.append(d)
        ans=(ans*10+d)%MOD
    elif q[0]=="2":
        L = len(S)-pos-1
        # print(S[pos],p10[L])
        ans = (ans-S[pos]*p10[L])%MOD
        pos+=1
    else:
        # print(q)
        print(ans)


