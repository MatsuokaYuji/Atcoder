

N = int(input())


# 例えば201**5-200*5　= 328080400001
# 1違うだけで10**9よりも大きい差分なので、
# A,B共に200を超えるパターンは調べなくても良い

for a in range(-200,200):
    for b in range(-200,200):
        if a**5-b**5 ==N:
            print(a,b)
            exit()