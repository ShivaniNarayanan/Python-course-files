n = int(input("Enter the number:"))
for i in range (n):
    for j in range (n-i-1):
        print(" ",end="")
    for z in range(2*i+1):
        print("*",end="")
    print()
        