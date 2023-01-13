


import string
S = input()

s = list(S)
import collections

c = collections.Counter(s)


d = string.digits 

for i in d:
    if i not in s:
        print(i)
