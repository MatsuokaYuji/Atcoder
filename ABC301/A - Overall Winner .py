



N = int(input())
S = input()

t = S.count("T")
a = S.count("A")

if t>a:
    print("T")
elif t<a:
    print("A")
else:
    count = t
    ct = 0
    ca = 0
    for i in range(N):
        if S[i]=="T":
            ct+=1
        if S[i]=="A":
            ca+=1
        if ct == count:
            print("T")
            exit()
        if ca == count:
            print("A")
            exit()
            

