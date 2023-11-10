# Using the break statement to exit a for loop
End_number = 15

for number in range(1, 20):
    print(number)
    
    if number == End_number:
        print("End number reached. Exiting the loop.")
        break
