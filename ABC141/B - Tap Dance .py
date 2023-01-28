





S = input()

S = list(S)
for i in range(len(S)):
    
    if i%2==1:
        if not (S[i]=="L" or S[i]=="U" or S[i]=="D"):
            print("No")
            exit()
    if i%2==0:
        if not (S[i]=="R" or S[i]=="U" or S[i]=="D"):
            print("No")
            exit()
print("Yes")

