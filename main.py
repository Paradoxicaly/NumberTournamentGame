import time, random
def HitTheTarget():
  num1 = random.randint(0,9)
  num2 = random.randint(0,9)
  num3 = random.randint(0,9)
  num4 = random.randint(0,9)
  target = random.randint(0,100)
  return("Your Numbers Are: " + str(num1) + " " + str(num2) + " " + str(num3) + " " + str(num4) + " Your Target Is: " + str(target))
def TwentyFour():
  num1 = random.randint(0,6)
  num2 = random.randint(0,6)
  num3 = random.randint(0,6)
  num4 = random.randint(0,6)
  return("Your Numbers Are: " + str(num1) + " " + str(num2) + " " + str(num3) + " " + str(num4) + " Try To Hit 24")
def Smash():
  num1 = random.randint(0,9)
  num2 = random.randint(0,9)
  num3 = random.randint(0,9)
  return("Your Numbers Are: " + str(num1) + " " + str(num2) + " " + str(num3))
while True:
  print("What game would you like you play?")
  time.sleep(1)
  print("Enter 1 To Play Hit The Target")
  time.sleep(1)
  print("Enter 2 To Play 24")
  time.sleep(1)
  print("Enter 3 to Play Smash")
  game_choice = int(input(""))
  if(game_choice == 1):
    print(HitTheTarget())
    print("It Will Notify You Once Timer Has Expired.")
    time.sleep(90)
    print("TIMES UP!!!!!")
    print("Please Review Your Equations To Make Sure They Are Correct.")
    print("Press 1 To Play Again ")
    print("Press 2 To Exit")
    play_again = int(input(""))
    if(play_again == 1):
      continue
    else:
      print("Thank You For Playing")
      exit()
  elif(game_choice == 2):
    print(TwentyFour())
    print("It Will Notify You Once Timer Has Expired.")
    time.sleep(90)
    print("TIMES UP!!!!!")
    print("Please Review Your Equations To Make Sure They Are Correct.")
    print("Press 1 To Play Again ")
    print("Press 2 To Exit")
    play_again = int(input(""))
    if(play_again == 1):
      continue
    else:
      print("Thank You For Playing")
      exit()
  elif(game_choice == 3):
    while True:
      print(Smash())
      another = int(input("Press 1 for 3 more numbers: "))
      if(another == 1):
        continue
      else:
        print("Press 1 To Play Again ")
        print("Press 2 To Exit")
        play_again = int(input(""))
        if(play_again == 1):
          continue
        else:
          print("Thank You For Playing")
          exit()
