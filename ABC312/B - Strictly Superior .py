
# s1 = {0, 1}
# s2 = {0, 1, 2, 3}

# print(s1 <= s2)
# # True

# print(s1.issubset(s2))
# # True

N,M = map(int,input().split())
eds=[set() for _ in range(N)]
price = [0] * N
kazu = [0] * N

# 安いか一緒の値段、機能を内包かつ
for i in range(N):
    B = list(map(int, input().split()))
    P,C,A = B[0],B[1],B[2:]
    # print(A)
    price[i] = P
    eds[i] = set(A)
    kazu[i] = C


for i in range(N):
    for j in range(N):
        if price[i]>=price[j]:
            if eds[i] <= eds[j]:
                if price[i]>price[j] or (kazu[j] - kazu[i])>=1:
                    print("Yes")
                    exit()
print("No")