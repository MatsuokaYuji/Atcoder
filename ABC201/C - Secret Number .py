

S = input()

ok = set()
ng = set()
for i in range(10):
    if S[i] == "o":
        ok.add(str(i))
    elif S[i] == "x":
        ng.add(str(i))

def judge(s):
    for i in ok:
        if i not in s:
            return False
    for i in ng:
        if i in s:
            return False
    return True

ans = 0
for i in range(10000):
    s = str(i).zfill(4)
    if judge(s):
        ans+=1
print(ans)