#project: Text based game:


answer = input("Would you like to play (yes/no)?")

if answer.lower().strip() == "yes":
  
  answer = input("You reach a crossroad, Where you like to go left or right?").lower().strip()

  if answer == "left":
    answer = input("You encountered a monster, would you like to run or attack?")

    if answer == "attack":
      print("That was not a great idea, You lost...")
    else:
      print("Great choice, You've made it safely...")

      answer = input("You see a car and plane. Which one would you like to take (car/plane)?")
        
      if answer == "plane":
          print("Unfortunately You do not know how to fly...So GAME OVER FOR YOU!!")
      else:
          print("drive the car as far as you can...YOU WON!!")

      answer = input("You see a police and a soldier. Which one would you choose (police/soldier)?")

      if answer == "police":
        print("He's a thief actually, You've lost>>>")
      else:
        print("This soldier will take you home directly...!!!")
      

    
  elif answer == "right":
      print("You walk aimlessly to the right and fall into the patch of ice. You injure you leg and cannot continue to walk.")
  

else:
  print("That's too bad")
