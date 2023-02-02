


N = int(input())


A = list(map(int, input().split()))


# """AtCoder Beginner Contest 271 C"""
# n = int(input())
# book = [False] * (n + 2)
# for_sale = 0
# for a in map(int, input().split()):
#     if a > n:
#         for_sale += 1
#     elif book[a]:
#         for_sale += 1
#     else:
#         book[a] = True

# left = 1
# right = n
# while True:
#     if left > right:
#         break

#     while book[left]:
#         left += 1

#     if for_sale >= 2:
#         for_sale -= 2
#         book[left] = True
#         left += 1
#     else:
#         while right != 0 and not book[right]:
#             right -= 1

#         if left <= right:
#             for_sale += 1
#             book[right] = False
#             right -= 1

# print(left - 1)

AA = set(A)

now = 0
rem= N

while rem>0:
    if now+1 in AA:
        now+=1
        rem-=1
        
    else:
        if rem>=2:
            rem-=2
            # AA.pop
            now+=1
        else:
            rem-=1
print(now)