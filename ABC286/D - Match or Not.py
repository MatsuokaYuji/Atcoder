s = input()
t = input()
tl = len(t)

front_count = 0
for i in range(tl):
    if s[i] == t[i] or s[i] == "?" or t[i] == "?":
        front_count += 1
    else:
        break

back_count = 0
for i in range(tl):
    if s[-1-i] == t[-1-i] or s[-1-i] == "?" or t[-1-i] == "?":
        back_count += 1
    else:
        break

print(front_count, back_count)
for x in range(tl+1):
    if front_count >= x and back_count >= tl - x:
        print("Yes")
    else:
        print("No")
