
# 簡単なやり方
def judge():
    S = input()
    # すべて英小文字からなるかを判定
    b1 = not S.islower()
    # 英大文字が含まれるかどうか
    b2 = not S.isupper()
    # 種類数が同じかどうか
    b3 = len(S) == len(set(S))
    return b1 and b2 and b3


print("Yes" if judge() else "No")



# import string
# #アルファベットの大文字小文字の出力
# alpha = string.ascii_letters
# #アルファベットの小文字のみの出力
# lowerAlpha = string.ascii_lowercase
# #アルファベットの大文字のみの出力
# upperAlpha = string.ascii_uppercase

# import collections



# S = input()

# flag1 = False
# for i in range(len(S)):
#   if S[i] in lowerAlpha:
#     flag1 = True
  

# flag2 = False
# for i in range(len(S)):
#   if S[i] in upperAlpha:
#     flag2 = True
  
# s = list(S)
# flag3 = True
# c = collections.Counter(s)
# k = list(c.values())
# k.sort(reverse=True)
# # print(k)

# if k[0]>1:
#   flag3 = False

# if flag1 and flag2 and flag3:
#   print("Yes")
# else:
#   print("No")

  
