# #try to find the pattern

# import random

# def generate_pattern():
#     # Generate a random pattern
#     pattern = []
#     start_num = random.randint(1, 10)
#     difference = random.randint(1, 5)
#     length = random.randint(5, 10)
#     for i in range(length):
#         pattern.append(start_num + (i * difference))
#     return pattern

# def play_game():
#     pattern = generate_pattern()
#     print("Complete the number pattern:")
#     print(pattern)
#     answer = input("Your answer: ")
#     answer = answer.replace(" ", "")  # Remove any spaces in the answer

#     # Check if the user's answer matches the pattern
#     expected_answer = ''.join([str(num) for num in pattern])
#     if answer == expected_answer:
#         print("Congratulations! You are the winner.")
#     else:
#         print("Oh no, wrong answer. You can try again.")
#         play_game()

# play_game()  






# import random


# def generate_pattern():
#     # Generate a random pattern
#     pattern = []
#     start_num = random.randint(1, 10)
#     difference = random.randint(1, 5)
#     length = random.randint(1, 6)
#     for i in range(length):
#         pattern.append(start_num + (i * difference))
#     return pattern

# def play_game():
#     pattern = generate_pattern()
#     print("Complete the number pattern:")
#     print(pattern)
#     answer = input("Your answer: ")
#     answer = answer.replace(" ", "")  # Remove any spaces in the answer

#     # Check if the user's answer matches the pattern
#     expected_answer = ''.join([str(num) for num in pattern])
#     if answer == expected_answer:
#         print("Congratulations! You are smarter than Einstein.")
#     else:
#         print("Oh no, wrong answer.")
#         print("The correct answer is:", expected_answer)
#         try_again = input("Do you want to try again? (yes/no): ")
#         if try_again.lower() == "yes":
#             for _ in range(2):  # Allow the user to try again twice
#                 play_game()
#         else:
#             print("Thank you for playing!")

# play_game()


import random
def generate_pattern():
    import random
    

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

    print("Complete the number pattern:")
    pattern_string = ' '.join(str(num) for num in pattern)
    print(pattern_string)

    answer = input("Enter your answer: ")

    # Check if the user's answer matches the missing number
    if answer == str(missing_number):
        print("🌟Congratulations! Einstein would be proud of you🌟.")
    else:
        #print("😞Oh no, wrong answer.\nThe correct answer is: ", missing_number, '\n👍Do not worry, you can try again')
        print("😞Oh no, wrong answer.\nThe correct answer is: ", missing_number)

    # return False

def play_again():
    play_count = 0

    while True:
        play_count += 1
        if play_count <= 3:
            play_more = input("👍 Do you want to play again? (yes/no): ")
            if play_more.lower() == "yes":
                #print("Let's play again!")
                if play_game():
                    break
            else:
                print("Thank you for playing! see you soon 👋")
                break
        else:
            #print("You have reached the maximum number of attempts.\nThank you for playing!")
            
            break

def All_function_in_medium():
    generate_pattern()
    play_game()
    play_again()
    


    
play_game()
play_again()