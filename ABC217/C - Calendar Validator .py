


N,M = map(int,input().split())

A = [list(map(int, input().split())) for _ in range(N)]

start = []
for i in A[0]:
    start.append(i)
if not (0 <= (A[0][0]-1)%7 <= 7-M):
	print("No")
	exit()
if start[0]%7==0 and len(start)>=2:
    print("No")
    exit()
# print(d)
# startからの基準が7*j上がったものであるか、また割った余りがJ+1になってるか
for i in range(N):
    for j in range(M):
        if (A[i][j] !=start[j] + 7*i) or  (A[i][j] != start[0] +7*i +j):
            print("No")
            exit()
print("Yes")
