#Write a program to check wheather a charecter is an alphabet, digi or special chareceter
ch=input("Enter the Charecter:")

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special charecter")