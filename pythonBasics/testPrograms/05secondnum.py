# WAP to find the second largest number in a list.


listsize = int(input("Enter the list size: "))

mylist = []

for i in range(1, listsize+1):
    element = int(input("Enter the element: "))
    mylist.append(element)

mylist.sort()

print("Second largest element is: ", mylist[listsize-2])
