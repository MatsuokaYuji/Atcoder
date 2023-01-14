



s = list(input().split())
s1,s2,s3 = (s[0],s[1],s[2])
t = list(input().split())
t1,t2,t3 = (t[0],t[1],t[2])

count = 0

if s1==t1:
    count+=1

if s2==t2:
    count+=1

if s3==t3:
    count+=1
if count==0 or count==3:
    print("Yes")
else:
    print("No")
    
