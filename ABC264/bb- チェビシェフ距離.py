


black = "black"
white = "white"

a,b = map(int,input().split())


c = max(abs(8-a),abs(8-b))

if c%2 == 0:
    print(white)
else:
    print(black) 


