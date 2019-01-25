# WAP to merge two lists and sort it.

mylist1 = []
mylist2 = []

listsize1 = int(input("Enter list size for list 1: "))
for i in range(1, listsize1+1):
    element1 = int(input("Enter elements for list 1: "))
    mylist1.append(element1)


listsize2 = int(input("Enter list size for list 2: "))
for i in range(1, listsize2+1):
    element2 = int(input("Enter list element for list 2: "))
    mylist2.append(element2)

mergeList = mylist1 + mylist2

mergeList.sort()

print("Your new sorted list is: ", mergeList)
