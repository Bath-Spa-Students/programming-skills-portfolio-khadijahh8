# Using a while loop to find the largest number among user-input values
largest_number = None

while True:
    user_input = input("Enter a number (enter '0' to exit): ")
    
    # Check if the user wants to exit
    if user_input == '0':
        break
    
    # Convert user input to a number
    current_number = float(user_input)
    
    # Update the largest_number if the current number is greater
    if largest_number is None or current_number > largest_number:
        largest_number = current_number

print("The largest number entered is:", largest_number)
