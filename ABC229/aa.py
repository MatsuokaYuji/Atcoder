



S = input()
T = input()

if S.count("#") >=2 or T.count("#") >=2:
    print("Yes")
    exit()
if (S[0] == "#" and T[1] == "#") or (S[1] == "#" and T[0] == "#"):
    print("No")
else:
    print("Yes")