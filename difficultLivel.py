#difficult game
print('Notice: Many people could not solve this game')

def sure():
  s=input('🫨 Are you sure you want to play?\n[yes / no]: ')
  if s=='yes':
    difficult_game()
    # pass# to start the game
  elif s=='no':
    print('Unacceptable, you must try 😉')
    #
  else:
    print("please Enter yes or no")

import random

def difficult_game():
    random_num = random.randint(1, 100)
    
    max_att= 4
    att_left = max_att
    
    while att_left > 0:
        
        guess = int(input("Guess the number between 1 and 100: "))
        
        if guess == random_num:
            print('WoooW Congratulations! You guessed the correct number in ', max_att- att_left +1  ,'attempts.')
            break
        elif guess < random_num:
            print("Too low! Try again. Attempts left: ", att_left - 1)
        else:
            print("Too high! Try again. Attempts left: ", att_left - 1)
          
        att_left -= 1


      
    
    if att_left == 0:
        print("Sorry, you're out of attempts. The correct number was ",random_num)
    
    # play_again = input("Do you want to play again? (yes/no): ")
    # if play_again == 'yes':
    #     difficult_game()
    # elif play_again == 'no':
    #     print('see you soon, good buy')
    #     print('********************************')
    # else:
    #     print('opps invalid', play_again)
      
# def pl_ag():
#   play_again = input("Do you want to play again? (yes/no): ")
#   if play_again == 'yes':
#      difficult_game()
#   elif play_again == 'no':
#      print('see you soon, good buy 👋')
#   else:
#      print('opps invalid', play_again)
        
sure()
difficult_game()
# pl_ag()
