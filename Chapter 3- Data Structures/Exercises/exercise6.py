names=["huda","maryam","jana","farah"]
for name in names:
    print(f"Hey {name}, you're invited to dinner!")
print("\nSorry, the new dinner table won't arrive in time, so I can invite only two people for dinner.\n")

# Use pop() to remove guests until only two names remain
while len (names) > 2:
 removed_name= names.pop()
 print (f"sorry,{removed_name}, I can't invite you to dinner." )
for name in names:
   print(f"Hi {name}, you're still invites to dinner!")
del names [:]
print ("\n The gest list is now empty :", names)

