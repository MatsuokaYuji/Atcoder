



S = input()

d = "-1"

import collections


c = collections.Counter(S)
# print(c)
# print(c.most_common())
# [('p', 2), ('o', 1)]

for i in c.most_common():
    if i[1] == 1:
        print(i[0])
        exit()
print(d)

