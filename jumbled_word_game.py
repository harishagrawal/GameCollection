# Python program for jumbled words game.

# import random module
import random

# Global scope
players = list()
score = dict()


# function for choosing random word.
def choose_a_word():
	# list of word
	words = ['rainbow', 'computer', 'science', 'programming',
			'mathematics', 'player', 'condition', 'reverse',
			'water', 'board', 'geeks']

	# choice() method randomly choose
	# any word from the list.
	pick = random.choice(words)
	return pick


# Function for shuffling the
# characters of the chosen word.
def jumble_it(word):
	# sample() method shuffling the characters of the word
	random_word = random.sample(word, len(word))

	# join() method join the elements
	# of the iterator(e.g. list) with particular character .
	jumbled = ''.join(random_word)
	return jumbled

# Function for declaring winner
def check_win():
	winner = ''
	winner_score = 0
    # # hits = [ v for v in score.values() ]
	# # biggest_hit = hits.sort(reverse=True)[0]
	# winners = list()
	for (player, strike) in score.items():
		if strike < winner_score:
			winner_score = strike
			winner = player
		# if strike == biggest_hit:
		# 	winners.append(player)
	if winner == '':
		print('Nobody won')
	else:
		print(f'{winner} won with {winner_score} hits')
	# print(','.join(winners), 'got the highest score', biggest_hit)



# Function for showing final score.
def thank_you_all():
	# print("Thanks to ", ",".join(players))
	winning_score = 0
	per_score = dict()
	for p in players:
		print(f"{p}'s score is {score[p]}")
		if not per_score.get(score[p]):
			per_score[score[p]] = [p]
		else:
			per_score[score[p]].append(p)
		if score[p] > winning_score:
			winning_score = score[p]
	
	print(f'Winning score is {winning_score}')
	print('And the winner(s) are', ','.join(per_score[winning_score]))


	# check_win() function calling
	# check_win()
	print('Thanks for playing !!!', ",".join(players).upper())

def ask(player_name, turn, picked_word):
	# print(f'"{player_name}", it is your Turn.')
	ans = input(f" * [Word:{turn}] {player_name}, what do you think, it is? =>")
	return (ans == picked_word)

def get_player_turn(player_list, turn):
    return (len(player_list) % turn)

def continue_playing():
	user_response = input("""Ready to PLAY JUMBLED WORDS !!!      ===>  (press 'x' to quit ...) <=== 
""")
	if user_response and user_response.upper() == 'X':
		return False
	else:
		return True

def play_turn(turn, picked_word):
		num_players = len(players)
		original_chance = turn % num_players
		player_position = original_chance

		player_order = players[player_position:] + players[:player_position]
		got_it = False
		for player in player_order:
			if (ask(player, turn, picked_word)):
				print(f'You got it right, {player}')
				score[player] += 1
				got_it = True
				break
		
		if not got_it:
			print("Better luck next time...correct word is :", picked_word)

def play_game():
	# variable for counting turn
	turn = 0
	while continue_playing():
		picked_word = choose_a_word()
		scrambled = jumble_it(picked_word)
		print("jumbled word is :", scrambled)
		# original_chance = get_player_turn(players, turn)
		play_turn(turn, picked_word)
		turn += 1
	print(f'Played {turn} scrambled words')

# Function for playing the game.
def setup_game():
	while True:
		user_txt = input("Enter Player Name OR xx to finish adding players:")
		if user_txt.lower() == 'xx':
			break
		elif user_txt != '':
			if user_txt not in players:
				players.append(user_txt)
	
	num_players = len(players)
	if num_players > 0:
		print('Players:', players)
		for p in players:
			score[p] = 0
	else:
		print("Sorry, can't play without players")
		return

	# Play the game, now that we have players
	play_game()
	
	# Exit by showing all the scores and winner(s)
	thank_you_all()

# Driver code
if __name__ == '__main__':
	setup_game()
