





T = input().split()
S = T[0]
K = int(T[1])
from itertools import permutations
s = "add"
st = set()
for it in permutations(S):
    st.add("".join(it))
ans = sorted(st)
print(ans[K-1])