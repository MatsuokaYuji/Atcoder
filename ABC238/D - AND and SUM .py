


# ANDをmin,ORをmaxで置き換えると(x AND y)+ (x OR y) = x+yが成り立つ
# よって問題文はa<=sかつ(x OR y) = s-aを満たすx,yが存在すること
# xANDy=a
# xORy=s−a

# ここで小さい方がa[i],大きい方がb[i]となるようなbitの組みが存在すれば良い-①
# ①をまとめるとmin(a[i],b[i]) = a[i]で全てのビットについてまとめると
# a AND b = aなので a AND (s-a) = aとなれば良い

T = int(input())


for i in range(T):
    a,s = map(int,input().split())
    b = s-a
    if b<0:
        print("No")
        continue
    if (a & b) == a:
        print("Yes")
    else:
        print("No")

# t=int(input())

# def check(x,y):
#   if y<0:
#     return 1
#   while x>0 or y>0:
#     if x%2==1 and y%2==1:
#       return 1
#     x//=2
#     y//=2
#   return 0

# for i in range(t):
#   a,s=map(int,input().split())
#   print("YNeos"[check(a,s-2*a)::2])