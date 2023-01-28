



from itertools import product, permutations,combinations


n,m = map(int, input().split())

ga = [[0] * n for _ in range(n)]
gb = [[0] * n for _ in range(n)]

for i in range(m):
	A,B = map(int,input().split())
	A -=1
	B -=1
	ga[A][B] = ga[B][A] = 1

for i in range(m):
	A,B = map(int,input().split())
	A -=1
	B -=1
	gb[A][B] = gb[B][A] = 1

ans = False

for p in permutations(range(n)):
	isSameShape = True
	for i in range(n):
		for j in range(n):
			if ga[i][j] != gb[p[i]][p[j]]:
				isSameShape = False
	if isSameShape:
		print("Yes")
		exit()
print("No")