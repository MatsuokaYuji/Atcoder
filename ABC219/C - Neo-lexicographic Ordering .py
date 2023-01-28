


X = input()
N = int(input())
D = dict()
A= []

for i in range(26):
    nxt = chr(i + ord("a"))
    D[X[i]] = nxt

for i in range(N):
    S = input()
    T = ""
    for char in S:
        T+=D[char]
    A.append((T,S))
A.sort()

for _,i in A:
    print(i)
