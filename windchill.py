import math
import sys
print("Computing windchill for given values")
t=int(sys.argv[1])
v=int(sys.argv[2])
v=pow(v,0.16)
w=35.74+0.6215*t+(0.4275*t-35.75)*v
print(w)