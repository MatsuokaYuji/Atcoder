
N = int(input())


# O(N*N*4方向)なので全探索で十分間に合う
def judge(sr,sc,dr,dc):
    row,col = sr,sc
    # 黒のカウント
    bl = 0
    for i in range(6):
        # はみ出すやつは除外
        if not (0<=row<N and 0<=col<N):
            return False
        bl += S[row][col]
        row += dr
        col += dc
    return bl>=4


pat = [(1,0),(0,1),(1,-1),(1,1)]
S = [[1 if i=="#" else 0 for i in input()] for _ in range(N)]

for i in range(N):
    for j in range(N):
        for a,b in pat:
            if judge(i,j,a,b):
                print("Yes")
                exit()
print("No")