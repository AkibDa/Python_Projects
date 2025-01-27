import random

print("Lets Play Rock-Paper-Scissor")

game = ['Rock','Paper','Scissor']
random_number = random.randrange(0,3)

user_choice = input("Choose Rock-Paper-Scissor ")
comp_choice = game[random_number]

print('You chose',user_choice)
print('Comp chose',comp_choice)

if (user_choice == 'Rock'):
  if(comp_choice == 'Paper'):
    print("You loss");
  elif(comp_choice == 'Scissor'):
    print("You won")
  else:
    print("Draw")
elif (user_choice == 'Paper'):
  if(comp_choice == 'Paper'):
    print("Draw");
  elif(comp_choice == 'Scissor'):
    print("You loss")
  else:
    print("You won")
else:
  if(comp_choice == 'Paper'):
    print("You won");
  elif(comp_choice == 'Scissor'):
    print("Draw")
  else:
    print("You loss")