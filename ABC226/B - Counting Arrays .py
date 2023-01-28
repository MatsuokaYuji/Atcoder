











N = int(input())

S = set()

for i in range(N):
    l, *A = map(int, input().split())
    A = tuple(A)
    S.add(A)
# print(S)
print(len(S))