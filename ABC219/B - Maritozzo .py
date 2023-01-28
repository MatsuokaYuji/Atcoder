










S1= input()
S2 = input()
S3 = input()
T = input()

ans = ""

for i in range(len(T)):
    t = int(T[i])
    if t==1:
        ans+=S1
    elif t==2:
        ans+=S2
    else:
        ans+=S3
print(ans)


# T = T.replace('1', S1)  # replaceはT自体が変化するのではなく、Tを変化したものを返すので、T = T.replace('1', S1) と書く必要があります
# T = T.replace('2', S2)
# T = T.replace('3', S3)
# print(T)