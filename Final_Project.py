#the games:
#اكمل النمط سواء كان عدد او اشكال 
#اضرب العامود في الصف ويطلع لي عدد(النجوم )
#ايموجيات اذا حزين يواسيه وينصحه واذا سعيد يعطيه اقضو حوائجكم بالكتمان(شينة ما تنفع)
#⥊ ⥋ ⥌ ⥍ ⥎ ⥏ ⥐ ⥑ ⥒ ⥓ ⥔ ⥕ ⥖ ⥗ ⥘ ⥙ ⥚ ⥛ ⥜ ⥝ ⥞ ⥟ ⥠ ⥡
#print('the name :{:>7} and the ID:{}'.format(name,age))#string الي بعده ينحدف
#game of 🥳
#i do not know how to stop the runng all code and the break did not work i am losing my mind
#finallu it's working
#?-----------the games functions-------------


def Q1():
   print("\n🎊 Welcome to the Easy Level 🎊")
   def easy_game():
      #!To start the game:
      print('\nTry to find the number of the stars in 5 second')

      start=input('write go to start:')
      
      try:
         if start=='go':
            pass
         else:
            print('you can try another game')
      except Exception as a:
         print('')
      #finally:
         #print("game over")
         #!the stars 
      import random as r
      row = r.randint(2,5) 
      colums = r.randint(2,5)
      symbol = '*'
      for i in range(row):
         for i in range(colums):
            print(symbol, end='')#راح يطبعها جمب بعض
         print()#مهمة عشان يطبعها تحت بعض فا تصير مربع بدال سطر
         
     #!Time counter
      import time
      for i in range(1,6):
         print(i, '...🕐')
         time.sleep(2)
         # print('find the number of the stars\n')
         # print(time_speed())
  
      #!Count the number of stars
      answer=int(input('The answer: '))
      try:
         x= row*colums
         if answer == x :
            print("Excelent, you beat Sonic's speed⚡")
            go_next= input('go to the next level? (yes or no)')
            if go_next == 'yes':
               Q2()
            elif go_next=='no':
               Q4()
            else:
               print('nothing')
            

         elif answer != x:
            print('wrong answer, the correct answer is: ',x )
            Q4()
      except ValueError as e:
         print("sorry not correct,only numbers are available\n")
  # except ValueError as c:
  #   print("sorry not correct,only numbers are available")
  # except ZeroDivisionError as v:
  #   print("sorry not correct,only numbers are available\n" , v)
   easy_game()
   


  
   # try_again = input("Do you want to try again? (yes/no) : ")
   # if try_again.lower() == "yes":
   #  for _ in range(2):  # Allow the user to try again twice
   #     easy_game()
   #     Q4()

   # elif try_again.lower() == 'no':
   #  print(Q4())
   # else:
   #    print('nothing')
       
    
def Q2():
    print("\n🎊 Welcome to the Medium Level 🎊")
    import random

    def generate_pattern():
       pattern = []
       start_num = random.randint(1, 10)
       difference = random.randint(1, 5)
       length = random.randint(5, 10)
       for i in range(length):
          pattern.append(start_num + (i * difference))
       return pattern
    
    def play_game():
      pattern = generate_pattern()
      missing_index = random.randint(0, len(pattern) - 1)
      missing_number = pattern[missing_index]
      pattern[missing_index] = "🤔?"
      print("\nComplete the number pattern:\n")
      pattern_string = ' '.join(str(num) for num in pattern)
      print(pattern_string)
      answer = input("Enter your answer: ")
      
     # Check if the user's answer matches the missing number

      if answer == str(missing_number):
         print("🌟Congratulations! Einstein would be proud of you🌟.")
         go_next= input('\ngo to the next level? (yes or no)')
         if go_next == 'yes':
            Q3()
         elif go_next=='no':
            Q4()
         else:
            print('nothing')
      else:
           #print("😞Oh no, wrong answer.\nThe correct answer is: ", missing_number, '\n👍Do not worry, you can try again')
           print("😞Oh no, wrong answer.\n The correct answer is: ", missing_number )
           Q4()
          # return False
    # def play_again():
    #    play_count = 0
    #    while True:
    #     play_count += 1
    #     if play_count <= 3:
    #         play_more = input("👍 Do you want to play again? (yes/no): ")
    #         if play_more.lower() == "yes":
    #             #print("Let's play again!")
    #                 if play_game():
    #                    break
    #                 else:
    #                    print("Thank you for playing! see you soon 👋")
    #                    break
    #         else:
    #            #print("You have reached the maximum number of attempts.\nThank you for playing!")
    #            break

    # def All_function_in_medium():
    generate_pattern()
    play_game()
    #play_again()
    

def Q3():
   #difficult game
   print("\n🎊 Welcome to the Difficult Level 🎊")

   print('\n🧨 Notice: Many people could not solve this game 🧨')
   
   def sure():
      s=input('\n🫨 Are you sure you want to play? [yes / no]: ')
      if s=='yes':
         difficult_game()
         # pass# to start the game
      elif s=='no':
         print('Unacceptable, you must try 😉\n')
    #
      else:
         print("please Enter yes or no")

   

   def difficult_game():
      import random
      random_num = random.randint(1, 100)
      max_att= 4
      att_left = max_att


      while att_left > 0:
         guess = int(input("Guess the number between 1 and 100: "))
         
         if guess == random_num:
            print('WoooW Congratulations! You guessed the correct number in ', max_att - att_left +1  ,'attempts.')
            print('You are the best in this Game Center 🥳\n Your gift is:\n * دعوة صادقة من القلب *')
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
   #    play_again = input("Do you want to play again? (yes/no): ")
   #    if play_again == 'yes':
   #       difficult_game()
   #    elif play_again == 'no':
   #       print('see you soon, good buy 👋')
   #    else:
   #       print('opps invalid', play_again)
        
   sure()
   difficult_game()
   # pl_ag()


# def Q4():
#    print('***Game Over***\nThank you, see you soon ')



#?------------start the main game------------
print('◕‿◕  🥳 ')
print('Welcome to the funny games club 🕹️')

counter =1
#?if i put int here it will be a small error
level = int(input("Choose a level\n1.easy\n2.medium\n3.difficult\nYour choice: "))
def play_game():
   try:
    if level == 1:
        #print("ypu are playing the game at the easy level." ,Q1())
        Q1()
    elif level == 2:
        #print("Playing the game at the medium level.")
        Q2()
    elif level == 3:
        #print("Playing the game at the difficult level.")
        Q3()
    else:
       print("opps sorry Invalid level" )
       
   except ValueError as e :
      print("opps sorry Invalid level, try again pleas" )

def Q4():
   print('\n***Game Over***\nThank you, see you soon 👋 ')
play_game()
























