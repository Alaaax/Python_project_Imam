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
  finally:
    print("game over")
    
  
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
    else:
     print('wrong answer, the correct answer is: ',x)
  except ValueError as e:
    print("sorry not correct,only numbers are available\n")
  # except ValueError as c:
  #   print("sorry not correct,only numbers are available")
  # except ZeroDivisionError as v:
  #   print("sorry not correct,only numbers are available\n" , v)


#!call the function
easy_game()
easy_game()


  
try_again = input("Do you want to try again? (yes/no) : ")
if try_again.lower() == "yes":
   for _ in range(2):  # Allow the user to try again twice
    easy_game()
   else:
     print("Thank you for playing!, see u soon")
