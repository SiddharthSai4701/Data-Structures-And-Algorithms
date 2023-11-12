""""
 Program to find the largest number

Step 1: Start
Step 2: Declare variables a,b and c.
Step 3: Read variables a,b and c.
Step 4: If a > b
           If a > c
              Display a is the largest number.
           Else
              Display c is the largest number.
        Else
           If b > c
              Display b is the largest number.
           Else
              Display c is the greatest number.  
Step 5: Stop
"""

a = float(input())
b = float(input())
c = float(input())

if a>b:
    if a>c:
        print("a is the largest number")
    else:
        print("c is the largest number")
        
else:
    if b>c:
        print("b is the largest number")
    else:
        print("c is the largest number")
       