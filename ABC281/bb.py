



s = input()

l = len(s)

if l<=7 or l>=9:
    print("No")
    exit()

if not s[0].isupper():
    print("No")
    exit()

if not s[-1].isupper():
    print("No")
    exit()

a = s[1:-1]
if a.isdecimal():
    if 100000 <= int(a) <= 999999:
        print("Yes")
        exit()
print("No")