

from math import gcd



#最小公倍数LはA * B // gcd(A,B)で求める


N,A,B = map(int,input().split())

def sum_seq(a1,d,n):
    result = a1 * n + n * ((n-1) * d) // 2
    return result


def calc(x):
    return sum_seq(x,x,N//x)

lcm = (A * B) // gcd(A,B)
ans = sum_seq(1,1,N) - calc(A) -calc(B) + calc(lcm) 

print(ans)