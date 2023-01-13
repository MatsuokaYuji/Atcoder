





N = int(input())
from collections import defaultdict

# a[i],a[i+K],a[i+2K],...に出てくる数字をカウントする連想配列
SCount=defaultdict(int)



for i in range(N):
    S = input()
    if SCount[S] ==0:
        print(S)
    else:
        print(S + "("+ str(SCount[S]) + ")")
    
    SCount[S] +=1
