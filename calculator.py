#Check wheather a number is positive, negative or zero

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
op=input("Enter the operation(+, -, *, /):")
if op=='+': print("Result=", a+b)
elif op=='-': print("Result=", a-b)
elif op=='*': print("Result=", a*b)
elif op=='/':
    if b!=0: print("Result=", a/b)
    else: print("divisible by zero is not allowed")
else: print("Invalide input from the user")