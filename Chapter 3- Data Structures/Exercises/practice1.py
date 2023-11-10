List1 = [5, 20, 15, 20, 25, 50, 20]

#use IF-else statment to check if 20 is in list
if 20 in List1:
    while 20 in List1:
        List1.remove(20)
    print ("List after removing all 20:",List1)
else:
    print("Item 20 not found in list.")