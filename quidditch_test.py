import hp_items as hpi
import hp_classes as hpc
import random
import time

player_options = ['chaser', 'beater', 'keeper', 'seeker']
test_team_1 = {'chaser': [100, 150, 200],
				'beater': [175, 125],
				'keeper': [100, 150, 200],
				'seeker': [13]}
test_team_2 = {'chaser': [100, 150, 200],
				'beater': [135, 165],
				'keeper': [100, 150, 200],
				'seeker': [7]}

def quidditch_match(team1, team2):
	global player_options
	in_progress = True
	team1_score = 0
	team1_snitch_score = 0
	team2_score = 0
	team2_snitch_score = 0

	offense = team2
	defense = team1
	while in_progress:
		player1 = random.choice(player_options)
		player2 = random.choice(player_options)
		# seekers in play
		if player1 == 'seeker' or player2 == 'seeker':
			seeker_match = random.randrange(0,31)
			if team1['seeker'][0] == seeker_match:
				print(f'''
***
		Team 1's seeker has caught the snitch!
	''')
				team1_snitch_score += 150
				in_progress = False
				break
			elif team2['seeker'][0] == seeker_match:
				print(f'''
***
		Team 2's seeker has caught the snitch!
	''')
				team2_snitch_score += 150
				in_progress = False
				break
			else:
				print(f'''
***
		One of the seekers has seen the snitch!

		The Team1 and Team2 seekers race towards a glint
		of gold in the air, but it quickly disappears.
		Play resumes.
	''')
		# chaser v. keeper
		elif player1 == 'chaser' and player2 == 'keeper':
			player1_value = random.choice(team1[player1])
			player2_value = random.choice(team2[player2])
			if player1_value >= player2_value:
				team1_score += 10
				print(f'''
***
		Team1's chaser throws the quaffle past the keeper
		and scores!
		Team1's score: {team1_score}
	''')
			elif player2_value > player1_value:
				print(f'''
***
		Team1's chaser throws the quaffle, but the Team2
		keeper makes an excellent save!
		Play resumes.
	''')
		elif player2 == 'chaser' and player1 == 'keeper':
			player2_value = random.choice(team1[player1])
			player1_value = random.choice(team2[player2])
			if player2_value >= player1_value:
				team1_score += 10
				print(f'''
***
		Team2's chaser throws the quaffle past the keeper
		and scores!
		Team2's score: {team2_score}
	''')
			elif player1_value > player2_value:
				print(f'''
***
		Team2's chaser throws the quaffle, but the Team1
		keeper makes an excellent save!
		Play resumes.
	''')
		# beaters.
		if player1 == 'beater' or player2 == 'beater':
			player1_value = random.choice(team1[player1])
			player2_value = random.choice(team2[player2])
			# team1 beater
			if player1 == 'beater' and player1_value >= player2_value:
				team1_score += 10
				print(f'''
***
		Team1's beater knocks a bludger toward Team2's
		{player2}. The bludger knocks the {player2} off
		track, allowing Team1's chaser to score a goal!
		Team1's score: {team1_score}
	''')
			elif player1 == 'beater' and player2_value > player1_value:
				team2_score += 10
				print(f'''
***
		Team1's beater tries to knock Team2 off course,
		but the referee calls a foul on the play. During
		the foul shot, Team2 scores!
		Team2's score: {team2_score}
	''')
			elif player2 == 'beater' and player2_value >= player1_value:
				team2_score += 10
				print(f'''
***
		Team2's beater knocks a bludger toward Team1's
		{player2}. The bludger knocks the {player1} off
		track, allowing Team2's chaser to score a goal!
		Team2's score: {team2_score}
	''')
			else:
				team1_score += 10
				print(f'''
***
		Team2's beater tries to knock Team1 off course,
		but the referee calls a foul on the play. During
		the foul shot, Team1 scores!
		Team1's score: {team1_score}
	''')
		else:
			print(f'''
***
		Player 1: {player1}
		Player 2: {player2}
	''')
	# adding house points
	if team1_score > team2_score:
		winner = 'Team1'
	elif team2_score > team1_score:
		winner = 'Team2'
	else:
		winner = 'Tied game!'
	print(f'''
***
		End result:
		Team1: {team1_score + team1_snitch_score}
		Team2: {team2_score + team2_snitch_score}

		Winner: {winner}
	''')
	return [team1_score, team2_score]

game_1 = quidditch_match(test_team_1, test_team_2)
hpc.house_points['Gryffindor'] += game_1[0]
hpc.house_points['Slytherin'] += game_1[1]

print(hpc.display_points())