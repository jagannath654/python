#Stop printing  anumber when a specific number is found

stop=int(input("Enter the number to stop:"))

for i in range(1, 101):
    if i == stop:
        break
    print(i)