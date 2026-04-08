#search for an element in a list and stop when found

list={10,20,30,40,50}
key=int(input("Enter the search elemet:"))

for x in list:
    if x == key:
        print("element found.")
        break
else:
        print("element not found.")
    