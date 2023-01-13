from itertools import combinations

C = [list(input()) for _ in range(9)]

pawns = set()
for i in range(9):
    for j in range(9):
        if C[i][j] == "#":
            pawns.add((i, j))

cnt = 0
# 4点から2点を選ぶ。異なる2点を選んだ時の長さのしゅりは正方形なら2であるはず
for sq in combinations(pawns, 4):
    len_set = set()
    for p1, p2 in combinations(sq, 2):
        len_set.add((abs(p1[0] - p2[0])) ** 2 + (abs(p1[1] - p2[1])) ** 2)

    if len(len_set) == 2:
        cnt += 1

print(cnt)
