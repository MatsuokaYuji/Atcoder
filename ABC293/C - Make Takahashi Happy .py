






import sys
sys.setrecursionlimit(10 ** 6)


H,W = map(int,input().split())
grid = [list(map(int, input().split())) for _ in range(H)]



def dfs(i,j,visited):
    visited.add(grid[i][j])
    if i ==H-1 and j == W-1:
        if len(visited) == H+W-1:
            return 1
        else:
            return 0
    if i <H-1:
        res += dfs(i+1,j,visited.copy())
    if j <W-1:
        res += dfs(i,j+1,visited.copy())
    return res


print(dfs(0,0,set()))