









N = int(input())

S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

# print(S)
# print(T)

# ・#の個数を確認する関数：count_sharp(X)
# ・90度時計回りに回転する関数：rotate(X)
# ・左上から探索して初めて#が出てくる行番号,列番号を返す関数：first_sharp(X)
# ・下方向へmove_gyou,右方向へmove_retu平行移動する関数：Translation(X,move_gyou,move_retu)
# ・S,Tが一致しているか確認する関数：check(S,T)

def count_sharp(X):
    count = 0
    for i in range(N):
        for j in range(N):
            if X[i][j]=="#":
                count+=1
    return count

def rotate(X):
    rotate_X = [["."] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            rotate_X[j][N-1-i] = X[i][j] 
    return rotate_X


def first_sharp(X):
    for i in range(N):
        for j in range(N):
            if X[i][j]=="#":
                return i,j
    
def Translation(X,move_gyou,move_retu):
    move_X = [["."] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if 0<=move_gyou+i<N and 0<=move_retu+j<N:
                move_X[move_gyou+i][move_retu+j] = X[i][j] 
    return move_X

def check(S,T):
    for i in range(N):
        for j in range(N):
            if S[i][j] != T[i][j]:
                return False
    return True

if count_sharp(S)!=count_sharp(T):
    print("No")
    exit()

for i in range(4):
    S = rotate(S)
    S_1_gyou,S_1_retu = first_sharp(S)
    T_1_gyou,T_1_retu = first_sharp(T)

    move_gyou = T_1_gyou - S_1_gyou
    move_retu = T_1_retu - S_1_retu

    S_tran = Translation(S,move_gyou,move_retu)

    if check(S_tran,T):
        print("Yes")
        exit()
print("No")