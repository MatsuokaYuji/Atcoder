



h,m = map(int,input().split())

h = str(h)
m = str(m)


while True:
  h = str(h)
  m = str(m)
  if  len(h) ==1:
    h = "0" + h
  if  len(m) ==1:
    m = "0" + m
  swaph = int(h[0] + m[0])
  swapm = int(h[1] + m[1])
  if 0<=swaph <=23 and 0<=swapm <=59:
    print(h,m)
    exit()
  if m == "59":
    if h =="23":
      h = "00"
      m = "00"
      continue
    else:
      h = int(h) + 1
      m = "00"
      continue
  else:
    m = int(m) + 1
    continue

