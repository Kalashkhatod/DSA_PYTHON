def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

print(gcd(15,50))

# a x b = gcd(a,b) x lcm(a,b) 
# gcd of (15,50) = 5 
# lcm of (15,50) = 150 if we multi 10 into 15 & 3 into 50 it becomes 150
# so 150 x 5 = 750

def lcm(a,b):
    return a*b/gcd(a,b)

print(lcm(30,60))
    