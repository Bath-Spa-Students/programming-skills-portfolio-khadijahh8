salary = float(input("Enter salary:"))
year_income = 0
if salary > 100:
   year_icome= 1200
else:
   year_icome= 0 
   print ("your year_icome: "+str(year_icome))




earning =int(input("Enter your earning per year:"))
work_experence= float(input("Enter your work  experience:"))

if earning > 300:
 if work_experence >=2:
        print("You are elegibile for loan")
 else :
        print("Soory your work experience is less than 2 years")
else :
        print("Your earning is less than 300")