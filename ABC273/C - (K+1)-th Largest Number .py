import bisect
n = int(input())
a = list(map(int,input().split()))
 
b = list(set(a))
b.sort()
m = len(b)
 
# 各Aiについてそれがsetで言うと何番目なのかを二分探索で求める。そいつをans配列に入れる
ans = [0] * n
for i in range(n):
	ans[m-bisect.bisect_right(b,a[i])] += 1
print(*ans,sep="\n")


# map使う。確実に解きたい問題
N = int(input())
A = list(map(int, input().split(' ')))

A_dict ={}

for n in A:
    if n not in A_dict:
        A_dict[n] = 1
    else:
        A_dict[n] += 1

A_sorted = sorted(A_dict.items(),reverse = True)

for i in A_sorted:
    print(i[1])

for i in range(N-len(A_sorted)):
    print("0")