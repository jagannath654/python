#Write a program to find the factorial of a program 
n=int(input("Enter a factorial number:"))
fact=1
for i in range(1, n+1):
    fact *=i
    print("Factorial=", fact)
