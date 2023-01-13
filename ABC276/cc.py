import itertools

n = int(input())



P = list(map(int, input().split()))



def nextPermutation(nums):
    # ステップ1：kを求める
    k = -1
    i = len(nums) - 2
    while i >= 0:
        if nums[i] > nums[i + 1]:
            k = i
            break
        i -= 1
# # kがなかったら、配列は逆順にソートされているので、反転して終了
#     if k == -1:
#         nums.reverse()
#         return

    # ステップ2：lを求め、nums[k]とnums[l]を入れ替える
    l = k + 1
    i = len(nums) - 1
    while i > k + 1:
        if nums[k] > nums[i]:
            l = i
            break
        i -= 1

    tmp = nums[k]
    nums[k] = nums[l]
    nums[l] = tmp

    # ステップ3：nums[k]より右側の要素を反転させる
    nums[k+1:] = reversed(nums[k+1:])
    return nums

d = nextPermutation(P)
for i in range(len(d)-1):
    print(d[i],end=" ")
print(d[-1])