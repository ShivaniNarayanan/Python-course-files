a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
small = min(a,b)
for i in range (1,small+1):
    if((a%i==0)and(b%i==0)):
        gcd = i
print("Greatest of common divisor is",gcd)

    
        