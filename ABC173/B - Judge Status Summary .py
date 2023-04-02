


# N = int(input())

# a,b,c,d = 0,0,0,0

# for i in range(N):
#     S = input()
#     if S=="AC":
#         a+=1
#     if S=="WA":
#         b+=1
#     if S=="TLE":
#         c+=1
#     if S=="RE":
#         d+=1
# print("AC"+" "+ "x" +" "+ str(a))
# print("WA"+" "+ "x" +" "+ str(b))
# print("TLE"+" "+ "x" +" "+ str(c))
# print("RE"+" "+ "x" +" "+ str(d))


N = int(input())

S = [input() for i in range(N)]

for v in ['AC', 'WA', 'TLE', 'RE']:
    print('{0} x {1}'.format(v,S.count(v)))
    

