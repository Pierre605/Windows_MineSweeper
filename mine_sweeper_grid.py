import random
from colorist import Color, Effect, BrightColor, green, yellow, red, blue, black, cyan, magenta, white
from pics import title

print(title)

def make_empty_ms_grid(n):
	empty_grid = []
	for y in range(n):
		empty_grid.append([])
		for x in range(n):
			empty_grid[y].append(0)
	return (empty_grid)


def put_bombs(nb, empty_grid):	
	bombs = 0
	while bombs < nb:
		bombs = 0
		L = []
		L2 = []
		n = len(empty_grid)

		for y in range(n):
			for x in range(n):
				if empty_grid[y][x] == 9:
					bombs += 1

		for i in range(nb):
			r = random.randint(0, n-1)
			r2 = random.randint(0, n-1)
			L.append(r)
			L2.append(r2)
		for x in range(nb - bombs):
			empty_grid[L[x]][L2[x]] = 9
	
	return (empty_grid)


def cell_numbers(empty_grid):
	n = len(empty_grid)
	for y in range(n):
		for x in range(n):
			if empty_grid[y][x] == 9:
				if (x >= 0 and x <= (n-2)) and (y >= 0 and y <= (n-1)):
					if empty_grid[y][x+1] != 9:
						empty_grid[y][x+1] += 1
					
				if (x >= 0 and x <= (n-1)) and (y >= 0 and y <= (n-2)):
					if empty_grid[y+1][x] != 9:
						empty_grid[y+1][x] += 1
					
				if (x >= 0 and x <= (n-1)) and (y >= 1 and y <= (n-1)):
					if empty_grid[y-1][x] != 9:
						empty_grid[y-1][x] += 1
					
				if (x >= 1 and x <= (n-1)) and (y >= 0 and y <= (n-1)):
					if empty_grid[y][x-1] != 9:
						empty_grid[y][x-1] += 1

				if (x >= 1 and x <= (n-1)) and (y >= 1 and y <= (n-1)):
					if empty_grid[y-1][x-1] != 9:
						empty_grid[y-1][x-1] += 1

				if (x >= 0 and x <= (n-2)) and (y >= 0 and y <= (n-2)):
					if empty_grid[y+1][x+1] != 9:
						empty_grid[y+1][x+1] += 1
					
				if (x >= 0 and x <= (n-2)) and (y >= 1 and y <= (n-1)):
					if empty_grid[y-1][x+1] != 9:
						empty_grid[y-1][x+1] += 1

				if (x >= 1 and x <= (n-1)) and (y >= 0 and y <= (n-2)):
					if empty_grid[y+1][x-1] != 9:
						empty_grid[y+1][x-1] += 1

	for y in range(n):
		for x in range(n):
			if empty_grid[y][x] == 9:
				empty_grid[y][x] = "X"
			elif empty_grid[y][x] == 1:
				empty_grid[y][x] = "1"
			elif empty_grid[y][x] == 2:
				empty_grid[y][x] = "2"
			elif empty_grid[y][x] == 3:
				empty_grid[y][x] = "3"
			elif empty_grid[y][x] == 4:
				empty_grid[y][x] = "4"
			elif empty_grid[y][x] == 5:
				empty_grid[y][x] = "5"
			elif empty_grid[y][x] == 6:
				empty_grid[y][x] = "6"
			elif empty_grid[y][x] == 7:
				empty_grid[y][x] = "7"
			elif empty_grid[y][x] == 8:
				empty_grid[y][x] = "8"
	
	for y in range(n):
		print('')
		for x in range(n):
			if empty_grid[y][x] == 'X':
				print(f"{BrightColor.BLACK}{Effect.BLINK}{empty_grid[y][x]}{Effect.BLINK_OFF}{BrightColor.OFF}", end= ' ')
			elif empty_grid[y][x] == "1":
				print(f"{Color.CYAN}{empty_grid[y][x]}{Color.OFF}", end= ' ')
			elif empty_grid[y][x] == "2":
				print(f"{Color.GREEN}{empty_grid[y][x]}{Color.OFF}", end= ' ')
			elif empty_grid[y][x] == "3":
				print(f"{Color.RED}{empty_grid[y][x]}{Color.OFF}", end= ' ')
			elif empty_grid[y][x] == "4":
				print(f"{Color.BLUE}{empty_grid[y][x]}{Color.OFF}", end= ' ')
			elif empty_grid[y][x] == "5":
				print(f"{Color.YELLOW}{empty_grid[y][x]}{Color.OFF}", end= ' ')
			elif empty_grid[y][x] == "6":
				print(f"{Color.MAGENTA}{empty_grid[y][x]}{Color.OFF}", end= ' ')
			elif empty_grid[y][x] == "7":
				print(f"{BrightColor.RED}{empty_grid[y][x]}{BrightColor.OFF}", end= ' ')
			elif empty_grid[y][x] == "8":
				print(f"{BrightColor.CYAN}{empty_grid[y][x]}{BrightColor.OFF}", end= ' ')
			else:
				print(empty_grid[y][x], end= ' ')

	
def Mine_sweeper(n,nb):
	grid = make_empty_ms_grid(n)
	put_grid = put_bombs(nb, grid)
	cell_numbers(put_grid)
	print('\n')
	input_play_again = input("Une autre grille ? 'o' oui, 'n' non : ")
	if input_play_again == 'o':
		return run_game()
	else:
		return '\nBYE !\n'


def run_game():
	print('\n')

	while True:
		try:
			input_grid_size = int(input("Entrez la longueur de la grille voulue (un nombre entre 1 et 75) : "))
			if input_grid_size >= 1 and input_grid_size <= 75:
				break				
			else:
				print("?????? Tapez un nombre compris entre 1 et 75")
				continue
		except ValueError:
			print("?????? Tapez un nombre")

	while True:
		try:
			input_nb = int(input("Entrez le nombre de bombes dans la grille : "))
			if input_nb >= 0 and input_nb <= (input_grid_size**2):
				return Mine_sweeper(input_grid_size, input_nb)
			else:
				print("?????? Tapez un nombre compris entre 0 et le carr?? de la longueur de la grille que vous avez choisi")
				continue
		except ValueError:
			print("?????? Tapez un nombre")


print(run_game())
