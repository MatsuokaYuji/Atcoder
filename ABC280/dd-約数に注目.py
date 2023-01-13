
import math

T = int(input())

for _ in range(T):
    N = int(input())
    p = -1
    q = -1
    for i in range(2, int(math.sqrt(N)) + 1, 1):
      if N % i == 0:
        # iはNの約数
        if (N // i) % i == 0:
          p = i
          q = int(int(N // i) // i)
        else:
          q = i
          p = int(math.sqrt(int(N // i)))
        break
    print(f"{p} {q}")


# エラストテネス、約数れっきょ、素因数分解要らなかった


# T = int(input())

# # """nを素因数分解"""
# # """2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

# # def factorization(n):
# #     arr = []
# #     temp = n
# #     for i in range(2, int(-(-n**0.5//1))+1):
# #         if temp%i==0:
# #             cnt=0
# #             while temp%i==0:
# #                 cnt+=1
# #                 temp //= i
# #             arr.append([i, cnt])

# #     if temp!=1:
# #         arr.append([temp, 1])

# #     if arr==[]:
# #         arr.append([n, 1])

# #     return arr

# # arr = factorization(3*10**9) 
# ## [[2, 3], [3, 1]] 
# ##  24 = 2^3 * 3^1

# # [[7, 1], [17, 2]]
# # [[3, 2], [7, 1]]
# # [[97711, 1], [104149, 2]]
# import math

# # エラトステネスの篩
# def prime(n):
#     is_prime = [True] * (n + 1)
#     is_prime[0], is_prime[1] = False, False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if is_prime[i]:
#             for j in range(2 * i, n + 1, i):
#                 is_prime[j] = False
#     return is_prime

# # 素数列挙
# N = 3*10**5
# # M以下の整数の素数判定
# prime = prime(N)

# # 素数判定を基に, 素数リストを作成
# prime_list = []
# for i in range(N + 1):
#     if prime[i]:
#         prime_list.append(i)
# B = set(prime_list)  

# P =[]
# for i in prime_list:
#     P.append(i**2)
# # print(P)
# for i in range(T):
#     N = int(input())
   
#     for j in P:
#         if N/j in B:
#             p = math.sqrt(j)
#             q = N/j
#     print(int(p),int(q))
   