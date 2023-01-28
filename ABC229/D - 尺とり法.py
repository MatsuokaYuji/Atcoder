


from collections import deque


S = input()
K = int(input())

s = list(S)
from collections import Counter
count=Counter(s)

# print(count)
# print(count["."])

d = count["."]

if K>=d:
    print(len(S))
    exit()

ans,score = 0,0
q = deque()
rem = K

for char in S:
    score+=1
    if char == ".":
        q.append(1)
        rem-=1
    else:
        q.append(0)
    while rem<0:
        rem+=q.popleft()
        score-=1
        

    ans = max(ans, score) ## dequeに入っている要素の積がK以下になるまで区間を縮めた。

print(ans)