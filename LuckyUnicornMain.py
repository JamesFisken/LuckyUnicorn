#plan

#create a function to ask the player the initial amount of money they want to add
#create a function that takes away 1$ from the init_money and activates the game
#pick a (definitly) random animal each round and plus/minus the winnings/loses to their init_money
#repeat these steps till either they want to stop playing or their bank runs out of money 

#imports and modules----------------
import random #for picking the random animals
import time #adds delays for suspense
import os
#variables and lists---------------
playing = True
total_money = 0
balance = 0
animals = ["donkey", "horse", "zebra", "unicorn"] #keeps a list of animals so they can be picked with animals[random.randint(0,3)]
rigged = True


#asci colors---------------
green = "\u001b[32m"
grey = "\u001b[0m"
red = "\u001b[31m"
yellow = "\u001b[33m"

#list to append asci art to
unicorn = []
Donkey = []
Horse = []
Zebra = []


#opening each file with asci art
f = open("UnicornToken.txt", "r")
f2 = open("HorseToken.txt", "r")
f3 = open("DonkeyToken.txt", "r")
f4 = open("ZebraToken.txt", "r")

#reading each of the files
unicornlines = f.readlines() 
Horselines = f2.readlines()
Donkeylines = f3.readlines()
Zebralines = f4.readlines()

#appending each line in a file to a list for usability
for lines in unicornlines:
	unicorn.append(lines)
for lines in Donkeylines:
	Donkey.append(lines)
for lines in Horselines:
	Horse.append(lines)
for lines in Zebralines:
	Zebra.append(lines)
#closing all the files to reduce lag
f.close()
f2.close()
f3.close()
f4.close()



#functions
def addlines(num): #function that adds lines for readibility
	for x in range(num):
		print("")
		
def askformoney(): #function that asks for the amount of money someone wants to invest and checks whether their total has exceeded 10 dollars
	global total_money
	invest_money = None
	while invest_money == None: #while no money has been invested, keep asking the user to invest 
		try:
			invest_money = float(input("how much money do you want to invest: ")) #asks user for a float
			total_money += invest_money #invested money is added to the total money. 
			addlines(2)
			if total_money > 10: #Total money is checked to see whether it exceeds the limit of $10 
				print("sorry you have invested over the limited of $10,") 
				total_money -= invest_money
				
				if total_money > 0: 
					addlines(1)
					print("the maximum amount that you can now invest is $", 10 - total_money) #tells user the maximum amount they can invest
				invest_money = None #sets invested money back to None so the user doesn't leave the while loop without investing
				
			else:
				addlines(3)
				return invest_money #returns value
		except:
			print("not a valid amount")

def printanimal(animal): #prints animals that have been appended to a list
	if animal == "donkey":
		for x in Donkey:
			print(red, x) #prints Donkey lines red(lose)
	elif animal == "zebra":
		for x in Zebra:
			print(yellow, x) #prints zebra lines yellow(neutral)
	elif animal == "unicorn":
		for x in unicorn:
			print(green, x)	#prints unicorn lines green(win)
	elif animal == "horse":
		for x in Horse:
			print(yellow, x) #prints horse lines yellow(neutral)
			
	print(grey)
def turn():
	
	global balance
	global animals
	
	input("press enter to start") #asks user to press enter
	print("balance -1") #displays to the user the cost of the game
	balance -= 1 
	time.sleep(2) #delay
	for x in range(20): #loops 20 times
		
		printanimal(animals[random.randint(0,3)]) #displays random animal
		
		time.sleep(x/40) #waits x/40 amount of time where x is the number of times looped(delay gets bigger over time)
		os.system("cls") #clears screen to have an animated effect
		
		
	if rigged: #option that the owner of the program can set to True or False
		animal = "donkey" #guarentees loss for the user
	else:
		animal = animals[random.randint(0,3)] #picks animals randomly
		
	printanimal(animal)
	addlines(2)
	time.sleep(1)
	if animal == "donkey":
		print("unfortunately you got the donkey, you win nothing")
		balance += 0
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
	print("your balance is: $", balance)
	if balance > 1:
		turn()
	else:
		print("you do not have enough money($", balance, "), you can either invest more money or stop playing")
		time.sleep(2)
		
	print("Balance: ", balance)
	
	
	answer = None
	while answer == None:
		answer = input("do you want to keep playing?(y/n): ")
		print(answer)
		if answer.lower() == "y" or answer.lower() == "yes":
			pass
		
		elif answer.lower() == "n" or answer.lower() == "no":
			print("you recieve your balance of $", balance)
			balance = 0
			time.sleep(3)
			exit()
		else:
			print("not a valid response")
			
		time.sleep(3)
	
	




