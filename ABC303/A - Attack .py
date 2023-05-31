





A,B = map(int,input().split())

ans = A//B

if A%B == 0:
    ans = A//B
else:
    ans = A//B
    ans+=1
print(ans)



# 切り上げ
# print((A+B-1)//B)