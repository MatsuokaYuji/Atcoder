



S = input()

a = ["Sunny","Cloudy","Rainy"]

for i in range(len(a)):
    if a[i] ==S:
        print(a[(i+1)%3])
        exit()
