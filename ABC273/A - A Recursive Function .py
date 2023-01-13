




n = int(input())


def cal (x: int):
    if x ==0:
        return 1
    else:
        return x * cal(x-1)

print(cal(n))