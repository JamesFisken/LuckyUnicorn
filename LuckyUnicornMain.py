#plan

#create a function to ask the player the initial amount of money they want to add
#create a function that takes away 1$ from the init_money and activates the game
#pick a (definitly) random animal each round and plus/minus the winnings/loses to their init_money
#repeat these steps till either they want to stop playing or their bank runs out of money 

#imports and modules
import random #for picking the random animals
import time #adds delays for suspense
import os
#variables and lists
playing = True
total_money = 0
balance = 0
animals = ["donkey", "horse", "zebra", "unicorn"]

green = "\u001b[32m"
grey = "\u001b[0m"
red = "\u001b[31m"
yellow = "\u001b[33m"

unicorn = []
Donkey = []
Horse = []
Zebra = []
#functions


f = open("UnicornToken.txt", "r")
f2 = open("HorseToken.txt", "r")
f3 = open("DonkeyToken.txt", "r")
f4 = open("ZebraToken.txt", "r")

unicornlines = f.readlines()
Horselines = f2.readlines()
Donkeylines = f3.readlines()
Zebralines = f4.readlines()

for lines in unicornlines:
	unicorn.append(lines)
for lines in Donkeylines:
	Donkey.append(lines)
for lines in Horselines:
	Horse.append(lines)
for lines in Zebralines:
	Zebra.append(lines)

f.close()
f2.close()
f3.close()
f4.close()




def addlines(num): #function that adds lines for readibility
	for x in range(num):
		print("")
		
def askformoney(): #function that asks for the amount of money someone wants to invest and checks whether their total has exceeded 10 dollars
	global total_money
	invest_money = None
	while invest_money == None:
		try:
			invest_money = int(input("how much money do you want to invest: "))
			total_money += invest_money
			addlines(2)
			if total_money > 10:
				print("sorry you have invested over the limited of $10,")
				total_money -= invest_money
				
				if total_money > 0:
					addlines(1)
					print("the maximum amount that you can now invest is $", 10 - total_money)
				invest_money = None
				
			else:
				addlines(3)
				return invest_money
		except:
			print("not a valid amount")

def printanimal(animal):
	if animal == "donkey":
		for x in Donkey:
			print(red, x)
	elif animal == "zebra":
		for x in Zebra:
			print(yellow, x)
	elif animal == "unicorn":
		for x in unicorn:
			print(green, x)		
	elif animal == "horse":
		for x in Horse:
			print(yellow, x)
			
	print(grey)
def turn():
	global balance
	global animals
	input("press enter to start")
	print("balance -1")
	balance -= 1
	time.sleep(2)
	for x in range(20):
		
		printanimal(animals[random.randint(0,3)])
		
		time.sleep(x/40)
		os.system("cls")
	animal = animals[random.randint(0,3)]
	printanimal(animal)
	addlines(2)
	time.sleep(1)
	if animal == "donkey":
		print("unfortunately you got the donkey, $-1 balance")
		balance -= 1
	elif animal == "zebra":
		print("you got the zebra $+0.5 balance")
		balance += 0.5
	elif animal == "unicorn":
		print("Congrats, you got the unicorn +$5")
		balance += 5	
	elif animal == "horse":
		print("you got the horse $+0.5 balance")
		balance += 0.5


#startup
print("Lucky Unicorns")
addlines(2)

#main loop
while playing:
	balance += askformoney()
	
	if balance > 1:
		turn()
	else:
		print("you do not have enough money($", balance, "), you can either invest more money or stop playing")
		time.sleep(2)
		
	print("Balance: ", balance)
	answer = input("do you want to keep playing?(y/n)")
	if answer.lower == "y" or answer.lower == "y"
	time.sleep(3)
	
	




