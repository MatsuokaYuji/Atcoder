




S = input()
T = input()

t = len(T)

for i in range(t):
    if S==T[:i+1]:
        print("Yes")
        exit()
print("No")