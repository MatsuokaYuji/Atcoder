

# N = int(input())

# S = input()
# s =list(S)

# t = 0
# d = 0
# for i in range(N):
#     if s[i]=="|":
#         t =1
#         if d==1:
#             print("in")
#             exit()
#     if s[i]=="*" and t==1:
#         d=1
# print("out")


N = int(input())
S = input()

v_first = S.index('|')
s = S.index('*')
v_second = S.rindex('|')

if v_first < s < v_second:
    print('in')
else:
    print('out')
