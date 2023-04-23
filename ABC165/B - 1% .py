




# オーバーフローではなく丸め誤差でしょう
# 974755271730884810
# こういう問題では浮動小数点を使わない


x = int(input())

ans = 0
s = 100

while True:
    if s>=x:
        print(ans)
        break
    s +=  s//100
    ans+=1

