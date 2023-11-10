while True :
    age_str= input ("Enter your age (type 'quit' to exit) ")
    if age_str.lower=='quit':
        print("Exiting. Thank you ")
        break
    try:
        age=int( age_str)
        if age < 3:
            print ("your ticket is free. ")
        elif 3 <= age <= 12:
            print ("your ticket is $10. ")
        else:
            print("Your ticket is $15. ")
    except ValueError:
        print (" please enter a valid age or 'quit'. ")

