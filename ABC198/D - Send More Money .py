



from itertools import permutations


S = [list(map(ord,input()))[::-1] for i in range(3)]

# print(S)

chars = set(S[0] + S[1] + S[2])
# print(chars)
if len(chars) >10:
    print("UNSOLVABLE")
    exit()

comp = [0] * 256

# 座標圧縮
for i,code in enumerate(chars):
    comp[code] = i
# print(comp)
for i in range(3):
    for j in range(len(S[i])):
        S[i][j] = comp[S[i][j]]
# print(S)

for perm in permutations(list(range(10)),len(chars)):
    # 最上位が0はダメ
    if perm[S[0][-1]] == 0 or perm[S[1][-1]] == 0 or perm[S[2][-1]] == 0:
        continue
    tmp = [0,0,0]
    for i in range(3):
        # jは桁数、このためにSを反転させていた
        for j ,code2 in enumerate(S[i]):
            tmp[i] += perm[S[i][j]] * 10 ** j
    if tmp[0] + tmp[1] == tmp[2]:
        for i in tmp:
            print(i)
        exit()
print("UNSOLVABLE")
