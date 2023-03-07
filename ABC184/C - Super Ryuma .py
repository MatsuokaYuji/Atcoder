




a,b = map(int,input().split())
c,d = map(int,input().split())


def solve():
    if a==c and b==d:
        return 0
    if a+b ==c+d or a-b==c-d or abs(a-c)+abs(b-d)<=3:
        return 1
    if abs(a-c)+abs(b-d)<=6:
        return 2
    if (abs(a-c)+abs(b-d)) %2 ==0:
        return 2
    if abs(a+b-c-d)<=3 or abs(a-b-c+d)<=3:
        return 2
    return 3


print(solve())