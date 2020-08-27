from math import  gcd

#LCM and GCD for three numbers

def lcm(x,y,z):
    gcd2 = gcd(y, z)
    gcd3 = gcd(x, gcd2)
    lcm2= y*z // gcd2
    lcm3= x*lcm2 // gcd(x, lcm2)
    return (lcm3, gcd3)

h=input("Press:1 for two numbers LCM Or \n Press:2 for three numbers LCM\n :") 
if h=="2":
    x=int(input("Number 1: "))
    y=int(input("Number 2: "))
    z=int(input("Number 3: "))
    (res1, res2) = lcm(x, y, z)
    print("The LCM and GCD of " + str(x) + " And " + str(y) + " And " + str(z)+"is" ,lcm(x,y,z))
