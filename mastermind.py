import random

# the .randrange() function generates
# a random number within the specified range.
NUM_TRIES = 10
NUM_DIGITS = 4
def welcome():
	print("\n")
	print("*"*15, "Welcome to MasterMind", "*"*15)
	print(f"""  *** RULES ***
  Computer has thought of a {NUM_DIGITS} digit number
  You have {NUM_TRIES} tries to guess it
   => Press q or x to exit
   => Press n to reset & start a new game
   """)
	print("*"*53)

def get_user_input():
	while True:
		user_input = input(f"Guess the {NUM_DIGITS} digit number: ")
		if user_input in ['q', 'Q', 'x', 'X']:
			print("Sorry to see you go")
			exit(0)
		# elif user_input in ['n', 'N']:
		# 	new_game()
		elif validate(user_input):
			return user_input

def validate(user_input):
	try:
		user_guess = int(user_input)
		if user_guess < pow(10, NUM_DIGITS - 1) or user_guess > pow(10, NUM_DIGITS):
			print(f"Provide {NUM_DIGITS} digit number only")
			return False
		else:
			return True
	except Exception as e:
		print("Try again, input is invalid:", e)

def new_game():
	num = random.randrange(pow(10, NUM_DIGITS - 1), pow(10, NUM_DIGITS))
	# print("random number", num)
	play_game(num)

def play_game(num):
	tries = 0
	while True:
		user_input = get_user_input()
		tries += 1
		# print(user_input)
		correct_digits = compare(user_input, num)
		if  correct_digits == NUM_DIGITS:
			print(f"Guessed it right. You took just {tries} attempts")
			break
		elif tries >= NUM_TRIES and correct_digits == 0:
			print(f'Oh, too many attempts. How about starting afresh?')
			print('Computer number was', num)
			new_game()

def compare(user_guess, computer_num):
	if (user_guess == computer_num):
		return len(str(user_guess))

	str_user_guess = str(user_guess)
	str_computer_num = str(computer_num)
	index = 0
	correct = 0
	print_matching = list()
	digit_found = list()
	while index < len(str_user_guess):
		if str_user_guess[index] != str_computer_num[index]:
			print_matching.append('_')
		else:
			print_matching.append(str_user_guess[index])
			correct += 1
		if str_user_guess[index] in str_computer_num:
			digit_found.append(str_user_guess[index])
		index += 1
	if correct > 0:
		print("Your number matches partially:", ''.join(print_matching))
	else:
		print("None of the digits match")
	if len(digit_found) > 0:
		print("These digits are common to both numbers:", ','.join(digit_found))
	return correct

def main():
	welcome()
	new_game()

if __name__ == "__main__":
	main()
