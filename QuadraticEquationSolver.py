""""
Step 1: Start
Step 2: Declare variables a, b, c, D, x1, x2, rp and ip;
Step 3: Calculate discriminant
         D ← b2-4ac
Step 4: If D ≥ 0
              r1 ← (-b+√D)/2a
              r2 ← (-b-√D)/2a 
              Display r1 and r2 as roots.
        Else     
              Calculate real part and imaginary part
              rp ← -b/2a
              ip ← √(-D)/2a
              Display rp+j(ip) and rp-j(ip) as roots
Step 5: Stop 
"""

# a = int(input())
# b = int(input())
# c = int(input())

# D = pow(b,2) - 4*a*c

# if D>=0:
    # r1 = -b+pow(D,0.5)
    # r2 = -b-pow(D,0.5)
    # print(f"The roots are {r1} and {r2}")

# else:
    # rp = -b/2*a
    # ip = pow(D,0.5)/(2*a)
    # print(f"The roots are {rp} + {ip}j")
    
# Prints today's date with help
# of datetime library
import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")
