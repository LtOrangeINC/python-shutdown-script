import os
import math


a = " "
x = float(input("HOURS TO SHUTDOWN:"))
y = float(input("Minutes to Shutdown:"))
c = "3600"
#Minutes
if y == "0":
    pass
if y != "0":
    m = "60"
    mi = int(m)* y
    u = math.floor(mi)
    r = str(u) 
#Hours
result = int(c)* x
t = math.floor(result)
t = str(t)
# ADD HOURS AND MINUTES 
e = int(float(t))+int(float(r))
e = str(e)
print(e + "\t" "SECONDS")
os.system("shutdown -s -t " + a + e) 



