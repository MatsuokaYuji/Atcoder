



S = input()

# 0:倒れている想定
c = [0,0,0,0,0,0,0]

# 7,4,28,15,39,6,10,どっちかが立っているなら1

if S[6] == "1":
    c[0] = 1
if S[3] == "1":
    c[1] = 1
if S[1] == "1" or S[7] == "1":
    c[2] = 1
if S[0] == "1" or S[4] == "1":
    c[3] = 1
if S[2] == "1" or S[8] == "1":
    c[4] = 1
if S[5] == "1":
    c[5] = 1
if S[9] == "1":
    c[6] = 1

if S[0] == "1":
    print("No")
    exit()
else:
    for i in range(len(c)):
        if c[i] == 1:
            for j in range(i+1,len(c)):
                if c[j]==0:
                    for k in range(j+1,len(c)):
                        if c[k]==1:
                            print("Yes")
                            exit()
print("No")
