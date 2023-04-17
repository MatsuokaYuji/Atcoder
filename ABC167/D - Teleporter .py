









N = int(input())


S = input()
s = list(S)

W=[]
R=[]

for i in range(N):
    if s[i]=="R":
        R.append(i)
    else:
        W.append(i)
R.sort(reverse=True)

Rl = len(R)
Wl = len(W)

if Rl ==0 or Wl==0:
    print(0)
    exit()
Rm = R[0] 
Wm = W[0]

ans = 0
r = 0
w = 0
while Rm>Wm:
    ans+=1
    r+=1
    w+=1
    if r>=Rl or w>=Wl:
        print(ans)
        exit()
    Rm = R[r]
    Wm = W[w]
print(ans)
