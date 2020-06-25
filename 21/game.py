import sys
import random

deck = ['6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh', 'Ah', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd', 'Ad', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ac', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks', 'As']
random.shuffle(deck)
y_card = []
my_card = []
score = 0
my_score = 0
score_dict = {
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'10': 10,
	'J': 2,
	'Q': 3,
	'K': 4,
	'A': 11
}

def take_card(array):
	array.append(deck[0])
	del deck[0]
	score(array)
	if array == y_card:
		print('Your cards: ' + ', '.join(array) + '.')

def play():
	cont = input("More ?(y/n):" )
	if cont == 'y':
		take_card(y_card)
		play()
	else:
		y_card.insert(0, 'stop')
		score(y_card)
		
def score(array, score = score):
	for i in range(len(array)):
		for key in score_dict:
			if key in array[i]:
				score += score_dict[key]

	if array == y_card:
		if score > 21:
			print('Your cards: ' + ', '.join(array) + '.')
			print('Your score: ' + str(score)+ '. ' + 'You lose')
			sys.exit()

		elif score == 21:
			print('Your cards: ' + ', '.join(array) + '.')
			print('Your score: ' + str(score)+ '. ' + 'You win')
			sys.exit()

		if array[0] == 'stop':
			global my_score
			my_score = score
			del array[0]
			print('Your cards: ' + ', '.join(array) + '.')
			print('Your score: ' + str(score)+ '.')
			take_card(my_card)
			

	if array == my_card and score < my_score and score < 21:
		take_card(my_card)

	if array == my_card and score > 21:
		print('My cards: ' + ', '.join(my_card) + '.')
		print('My score: ' + str(score)+ '. ' + 'Im lose')

	elif array == my_card and score > my_score:
		print('My cards: ' + ', '.join(my_card) + '.')
		print('My score: ' + str(score)+ '. ' + 'Im win')
		
	elif array == my_card and score == my_score:
		print('My cards: ' + ', '.join(my_card) + '.')
		print('My score: ' + str(score)+ '. ' + 'Tie')


start = input("Do you want play ?(y/n):" )
if start == 'y':
	take_card(y_card)
	play()
