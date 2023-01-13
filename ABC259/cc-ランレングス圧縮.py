



from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

S = input()
T = input()

s = runLengthEncode(S)
t = runLengthEncode(T)

# print(s)
# print(t)

# [('a', 1), ('b', 2), ('a', 2), ('c', 1)]
# [('a', 1), ('b', 4), ('a', 3), ('c', 1)]

if len(s) !=len(t):
    print("No")
    exit()

for i in range(len(s)):
    sMoji = s[i][0]
    tMoji = t[i][0]
    # print(sMoji)
    # print(tMoji)
    sCount = s[i][1]
    tCount = t[i][1]

    if sMoji != tMoji:
        print("No")
        exit()
    elif sCount ==1 and sCount < tCount:
        print("No")
        exit()
    elif sCount > tCount:
        print("No")
        exit()
print("Yes")


