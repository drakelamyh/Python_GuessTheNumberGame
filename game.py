import random
jackpot = random.randint(1,99)
print("Secret number generated! Game start!")

lower = 0
upper = 100

guess = 0

while guess != jackpot:

	print("")
	print(f"{lower} - {upper}")
	guess = input("Choose a number!  ")
	
	if guess.isdigit() == False:
		print("Sorry that is not a integer!\n")

	if guess.isdigit():
		guess = int(guess)
		if guess <= lower:
			print("Number selected is too low!")
		if guess >= upper:
			print("Number selected is too high!")
		if guess == jackpot:
			print("JACKPOT!!!")
			print(jackpot)
		if lower < guess < jackpot:
			lower = guess
		if jackpot < guess < upper:
			upper = guess

print("game ends")