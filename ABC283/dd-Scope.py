


S = input()
ANS =[]

res = -1

for i in range(len(S)):
    if S[i].isalpha():
        if S[i] in ANS:
            res = 0
        else:
            ANS.append(S[i])

    elif S[i] == ')':
        ANS = []

print( 'Yes' if res == -1 else 'No')





import string

S = input()

#現在の集合を管理
a = set("")

#削除するやつを管理
c = set()
alphaList = string.ascii_lowercase


# 前回の)の箇所sと、(の箇所tを記憶してsまでとtより前を調べれば良い
# 削除するsetも管理
s = 0
t = 0

for i in range(len(S)):
    if S[i] in alphaList:
        a-c
        if S[i] in a:
            print("No")
            exit()
        else:
            a.add(S[i])
    elif S[i]=="(":
        continue
    else:
        #iから逆に見ていって初めて"("が出たときの番号、そして
        #　そこまでに出た英語は全て記録してsetから削除する
        b =set()
        for j in range(i,-1,-1):
            if S[j] ==")":
                c|b
                a-b
                break
            if S[j] =="(":
                c|b
                a-b
                break
            if S[j] in alphaList:
                b.add(S[j])
        
        b = set()
        for k in range(t,-1,-1):
            if S[j] ==")":
                c|b
                a-b
                break
            if S[j] =="(":
                c|b
                a-b
                break
            if S[j] in alphaList:
                b.add(S[j])
print("Yes")
