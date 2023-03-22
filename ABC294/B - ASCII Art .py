





import string

#アルファベットの大文字のみの出力
upperAlpha = string.ascii_uppercase




h,w = map(int,input().split())


S = [input().split() for _ in range(h)]


for i in range(h):
    ans = []
    for j in S[i]:
        if j=="0":
            ans.append(".")
        else:
            ans.append(upperAlpha[int(j)-1])
    print("".join(ans))
