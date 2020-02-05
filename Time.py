sec = int(input('Enter seconds: '))
d = (sec // 3600) * 24
h = ((sec // 3600)) % 24
m = (sec // 60) % 60
s = sec % 60

print("%d:%d:%02d:%02d" % (d, h, m, s))




