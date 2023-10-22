names=["huda", "maryam","jana", "farah"]
for name in names :
    print(f"Hi {name} ,I would like to invite you for dinner")
guest_cant_make_it ="huda"
print (f"\nunfortunately,{guest_cant_make_it}can't make it to dinner.\n")
new_person ="sama"
names[names.index(guest_cant_make_it)]= new_person
for name in names:
     print(f"Hi {name}, I would like to invite you for dinner")




