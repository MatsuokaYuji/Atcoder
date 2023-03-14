









S = input()

l = len(S)

if l<=2:
    if int(S) %8 == 0 or int(S[::-1]) % 8 ==0:
        print("Yes")
    else:
        print("No")
    exit()

from collections import Counter
cnt = Counter(S)

# for i in range(112,1001,8):
#     if not Counter(str(i))-cnt:
#         print("Yes")
#         exit()
# print("No")


for i in range(112,1001,8):
    cur = Counter(str(i))
    ok = True
    # val　要求量
    for key,val in cur.items():
        #  cnt[key]...持ってる量
        if val > cnt[key]:
            ok = False
    if ok:
        print("Yes")
        exit()
print("No")