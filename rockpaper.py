import random

print("Rock, Paper, Scissors")

user_choice = input('Pick one of the above: ')

user_choice = user_choice.capitalize()
print(user_choice)

com_choice = random.randint(1,3)
if com_choice == 1:
    com_choice = 'Rock'

if com_choice == 2:
    com_choice = 'Paper'

if com_choice == 3:
    com_choice = 'Scissors'

if user_choice == 'Rock' and com_choice == 'Scissors':
	print('YOU WIN!')

elif user_choice == 'Rock' and com_choice == 'Paper':
	print('YOU LOSE')

elif user_choice == 'Rock' and com_choice == 'Rock':
	print('TIE...')

elif user_choice == 'Paper' and com_choice == 'Rock':
	print('YOU WIN!')

elif user_choice == 'Paper' and com_choice == 'Scissors':
	print('YOU LOSE')

elif user_choice == 'Paper' and com_choice == 'Paper':
	print('TIE...')

elif user_choice == 'Scissors' and com_choice == 'Paper':
	print('YOU WIN!')

elif user_choice == 'Scissors' and com_choice == 'Rock':
	print('YOU LOSE')

elif user_choice == 'Scissors' and com_choice == 'Scissors':
	print('TIE...')