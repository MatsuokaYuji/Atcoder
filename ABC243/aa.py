
V,A,B,C = map(int,input().split())

now = V-A

while True:
    if now<0:
        print("F")
        exit()
    now-=B
    if now<0:
        print("M")
        exit()
    now-=C
    if now<0:
        print("T")
        exit()
    now-=A
