import oxo_logic

menu = ["Start new game",
		"Resume saved game", 
		"Display help",
		"Quit"]

def getMenuChoice(aMenu):
	if not aMenu:
		raise ValueError('No Menu Content')

	while True:
		print("\n\n")
		for index, item in enumerate(aMenu, start=1):
			print(index, '\t', item)

		try:
			choice = int(input("\nChoose a menu option: "))
			if 1 <= choice <= len(aMenu):
				return choice
			else:
				print("Choose a number between 1 and", len(aMenu))
		except ValueError:
			print("Choose the number of a menu option")

def startGame():
	return oxo_logic.newGame()

def resumeGame():
	return oxo_logic.restoreGame()

def displayHelp():
	print('''
		Start new game: Starts a new game of tick tack toe
		Resume saved game: restores the last game
		Display help: shows this page
		Quit: exits the game
		''')
def quit():
	print('Goodbye...')
	raise SystemExit

def executeChoice(choice):
	dispatch = [startGame, resumeGame, displayHelp, quit]
	game = dispatch[choice -1]()
	if game:
		playGame(startGame())

def printGame(game):
	display = '''
	1 | 2 | 3		{} | {} | {}
	---------		------------
	4 | 5 | 6		{} | {} | {}
	---------		------------
	7 | 8 | 9		{} | {} | {} '''
	print(display.format(*game))

def playGame(game):
	result = ""
	while not result:
		printGame(game)
		choice = input("Cell[1-9 or q to quit]: ")
		if choice.lower()[0] == 'q':
			saves = input("Save game before quitting?[y/n] ")
			if save.lower()[0] == 'y':
				oxo_logic.saveGame(game)
			quit()
		else:
			try:
				cell = int(choice) -1
				if not (0 <= cell <=8):
					raise ValueError
			except ValueError:
				print("Choose a number between 1 and 9 or 'q' to quit ")
				continue

			try:
				result = oxo_logic.userMove(game,cell)
			except ValueError:
				print("Choose an empty cell")
				continue

			if not result:
				result = oxo_logic.computerMove(game)
			if not result:
				continue
			elif result == 'D':
				printGame(game)
				print("Its a draw")
			else:
				printGame(game)
				print("Winner is", result, '\n')


def main():
	while True:
		choice = getMenuChoice(menu)
		executeChoice(choice)

if __name__ == '__main__':
	main()

