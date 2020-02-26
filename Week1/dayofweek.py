import sys
print("The entered values are")
m=int(sys.argv[1])
d=int(sys.argv[2])
y=int(sys.argv[3])
day = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
y0 = y - (14 - m) // 12
x = y0 + y0//4 - y0//100 +y0//400
m0 = m + 12 * ((14 - m) // 12) - 2
d0 =(d + x + 31 * m0 // 12) % 7
print(d0)
print(day[d0])