import random

while(True):
 n = eval(input("1) Play \n2) Exit \n"))
 if n==1:
  player1 = eval(input("Your choice : 1 - Rock, 2 - Paper, 3 - Ciser --- "))
  print("You choose : ")
  if player1 == 1:
   print("Rock")
  elif player1 == 2:
   print("Paper")
  else:
   print("Ciser")
  print()
  bot = random.randint(1,3)
  print("Bot chooses : ")
  if bot == 1:
   print("Rock")
  elif bot == 2:
   print("Paper")
  else:
   print("Ciser")
  print()
  print("Winner : ")
  print("--------")
  if(bot == player1):
   print("Noone wins.")
  elif (player1 == 1 and bot == 3) or (player1 == 2 and bot == 1) or (player1 == 3 and bot == 2):
   print("Player1 won the match.")
  else:
   print("Bot won the match.")
  print()
 elif n==2:
  print("Bye,Bye.Have a nice day ! See you again.")
  break
print("Thank you for playing this game.")
