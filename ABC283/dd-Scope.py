


S = input()
ANS =[]

res = -1

for i in range(len(S)):
    if S[i].isalpha():
        if S[i] in ANS:
            res = 0
        else:
            ANS.append(S[i])

    elif S[i] == ')':
        ANS = []

print( 'Yes' if res == -1 else 'No')




s = input()
box = set()
now = [[]]
for c in s:
  if c == ')':
    for v in now[-1]:
      box.remove(v)
    now.pop()
  elif c == '(':
    now.append([])
  else:
    if c in box:
      print('No')
      break
    box.add(c)
    now[-1].append(c)
else:
  print('Yes')
