








N = int(input())


s = ord("a")
ans = ""


while 1:
    N-=1
    b = N%26
    N//=26
    ans+=chr(s+b)
    if N==0:
        break
# print(ans)
print(ans[::-1])