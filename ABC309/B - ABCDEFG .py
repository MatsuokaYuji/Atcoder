



S = input().split()


s = list('ABCDEFG')

p = S[0]
q = S[1]
# print(p,q)

d = s.index(p)
e = s.index(q)
# print(d,e)
G = [0,3,4,8,9,14,23]

print(abs(G[e]-G[d]))