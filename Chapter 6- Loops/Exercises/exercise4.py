# list of sandwiches 
sandwich_orders=["Chicken", "Tuna","Turkey"]

#Empty list 
finishes_sandwices=[]

#loop and print massage
while sandwich_orders:
    current_order=sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich.")

    # add from current order to finished sandwiches list
    finishes_sandwices.append(current_order)
print ("\n List of finished_sandwiches: ")
for sandwich in finishes_sandwices:
 print (sandwich)

