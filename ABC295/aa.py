



N = int(input())
S = input().split()

s = set(S)

for i in s:
    if i=="and" or i== "not" or i== "that" or i== "the" or i=="you":
        print("Yes")
        exit()
print("No")