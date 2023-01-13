






A,B = map(int,input().split())

taka = [0,0,0]

aoki = [0,0,0]

if A ==1:
    taka[0]=1
if B ==1:
    aoki[0]=1


if A ==2:
    taka[1]=1

if B ==2:
    aoki[1]=1


if A ==3:
    taka[0]=1
    taka[1]=1

if B ==3:
    aoki[0]=1
    aoki[1]=1


if A ==4:
    taka[2]=1

if B ==4:
    aoki[2]=1


if A ==5:
    taka[0]=1
    taka[2]=1

if B ==5:
    aoki[0]=1
    aoki[2]=1


if A ==6:
    taka[1]=1
    taka[2]=1

if B ==6:
    aoki[1]=1
    aoki[2]=1

if A ==7:
    taka[0]=1
    taka[1]=1
    taka[2]=1

if B ==7:
    aoki[0]=1
    aoki[1]=1
    aoki[2]=1

ans= 0
ten= [1,2,4]
for i in range(3):
    if taka[i] ==1 or aoki[i] ==1:
        ans+=ten[i]
print(ans)

