import random
# item list
item_list = ['rock','paper','scissor']

# user inputs
user_choice = input('enter your move = rock, paper or scissor : ')
computer_choice = random.choice(item_list)
print(f'user choice = {user_choice}, computer choice = {computer_choice}')

if user_choice == computer_choice:
    print('Both chooses same = Match Tie')
elif user_choice == "rock":
    if computer_choice == 'paper':
        print("paper covers rock = Computer win")
    else:
        print("rock breaks scissor = User win")

elif user_choice == 'paper':
    if computer_choice == 'scissor':
        print("scissor cuts the paper = computer win")
    else:
        print("paper covers the rock = user win")

elif user_choice == 'scissor':
    if computer_choice == 'paper':
        print("scssor cuts the paper = user win")
    else:
        print('rock smashes scissor = computer win')

        
