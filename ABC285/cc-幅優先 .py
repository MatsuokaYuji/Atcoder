



















S = input()

l = len(S)

import string

alphabets = string.ascii_uppercase
# alphabets.index("D") + 1
ans = 0
for i in range(l):
    d = S[i]
    f = alphabets.index(d) + 1
    ans += 26**(l-i-1) * f
print(ans)


