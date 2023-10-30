alien_colors=['green', 'red', 'blue']
alien_color=[0]
if alien_color=='green':
  print("congratulation!You just earned 5 points for shooting the green alien.")
else:
  print("congratulation! you just earned 10 points")


#Version 1: Running the if block

alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the green alien.")
else:
    print("Congratulations! You just earned 10 points.")


#Version 2: Running the else block

alien_color = 'red'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the green alien.")
else:
    print("Congratulations! You just earned 10 points for shooting the non-green alien.")
