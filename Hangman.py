# Hangman Game
# Cameron Savage

import string
import random
from HMGraphics import HangingMan

# Global Variables
sWordChoice = ""

#-----------------------------FUNCTIONS------------------------------------#


#Chooses word length
def fDifficulty():
	global sWordChoice
	iDifficulty = 0
	newWords = []
	words = []
	#sWordChoice = ""
	
	#choose difficulty prompt
	print "Choose a difficulty:"
	print """
1 Simple: 4 letters
2 Easy: 5 - 6 letters
3 Medium: 7 - 8 letters
4 Hard: 9 - 10 letters
5 Very Hard: 11+ letters
"""

	iDifficulty = input("Enter the corresponding number to choose a difficulty: ")

	words = open("dictionary-large.txt").read().strip("\n").split(" ")
	
	#Go through the text file, find words in correct range, add to a list, choose one
	#All length(char) values are adjusted by +1 b/c every word has an extra space, increasing its character count by 1, this is stripped after the word is chosen
	#Simple 3-4 letters
	if iDifficulty == 1 :
		for char in words :
			if len(char) == 5 :
				newWords.append(char) 
	#~ #Easy 5-6
	elif iDifficulty == 2 :
		for char in words :
			if len(char) == 6 or len(char) == 7 :
				newWords.append(char) 
	#Medium 7-8
	elif iDifficulty == 3 :
		for char in words :
			if len(char) == 8 or len(char) == 9 :
				newWords.append(char) 
	#Hard 9-10
	elif iDifficulty == 4 :
		for char in words :
			if len(char) == 10 or len(char) == 11 :
				newWords.append(char) 
	#Very Hard 11+
	elif iDifficulty == 5 :
		for char in words :
			if len(char) >= 12:
				newWords.append(char) 
	#If user enters a non-existent difficulty
	elif fDifficulty > 6 or fDifficulty < 1 :
		print
		print "Invalid input, enter a number from 1 to 5"
		print
		fDifficulty()
	
	#assigns correct word length to sWordChoice
	sWordChoice = random.choice(newWords)
	sWordChoice = sWordChoice.strip(" ").strip("\n")
	#remove for final game
	#print sWordChoice
	
	fGameLoop()


#Main function, runs the gameplay
def fGameLoop():

	# Local variable declarations
	sWrong = ""
	sCorrect = ""
	sGuess = ""
	iErrors = 0
	sBlanks = ""
	sFinal = ""
	
	#Converts word into underscores
	sBlanks = (len(sWordChoice)) * "_ "
	

	#Main loop
	while iErrors < 8 :

		#Prints gallows, information
		print
		print "Attempts left:", (8 - iErrors)
		print HangingMan[iErrors]
		#print sWordChoice
		print
		print sBlanks
		print
		print "Correct Letters: ", sCorrect
		print "Incorrect letters: ", sWrong
		print

		sGuess = ""
		sGuess = raw_input("Guess a letter: ")
		sGuess = sGuess.lower()

		#Determines if sGuess is correct or incorrect, stores the letter in the correct string
		if sGuess in sWordChoice :
			if sGuess not in sCorrect :
				sCorrect += sGuess
			elif sGuess in sCorrect :
				print "Already guessed that letter"
		elif sGuess not in sWordChoice :
			if sGuess in "abcdefghijklmnopqrstuvwxyz" :
				if sGuess not in sWrong :
					sWrong += sGuess
					iErrors += 1
				elif sGuess in sWrong :
					print "Already guessed that letter"
			elif sGuess not in "abcdefghijklmnopqrstuvwxyz" :
				print "Invalid character, try again"


		#Detects length of sGuess, determines if the user is trying to guess the whole word
		#Replaces underscores with correct letters
		sBlanks = ""
		for char in sWordChoice :
			#Checks if letter is in Correct Letters Guessed string, adds correct letter or underscore
			if char in sCorrect.lower() :
				sBlanks += char + " "
			else :
				sBlanks += "_ "


		#Copies sBlanks w/o spaces, when full of correct letters and no underscores, then the user has guessed all of the letters or the full word
		for char in sBlanks :
			if char != " " :
				sFinal = sFinal + char


		#Win/lose detection
		#Detects how many letters in user's guess
		#If more than one, detects if user should win
		if (len(sGuess)) == 1 and iErrors != 8 :
			if sWordChoice in sFinal :
				iErrors = 8
				print
				print "You correctly guessed:", sWordChoice
				print
				
		elif iErrors == 8 :
			print HangingMan[iErrors]
			print
			print "You lost, your word was:", sWordChoice
			print

		elif (len(sGuess)) > 1 and sWordChoice in sFinal :
			iErrors = 8
			print
			print "You correctly guessed:", sWordChoice 
			print
			
		elif (len(sGuess)) > 1 and sWordChoice not in sFinal :
			iErrors = 8
			print sBlanks
			print HangingMan[8]
			print "You guessed wrong, you were hanged"
			print
			print "Your word was:", sWordChoice
			print

	#Once iErrors reach 8, loop stops, fReplay is called
	fReplay()


#Prompts user to replay the game
def fReplay() :
	
	sReplay = raw_input("Would you like to play again? Y/N   " )
			
	if sReplay.lower() == "y" :
		fIntro()
		print
	elif sReplay.lower() == "n" :
		print
		quit
	else :
		print "Invalid input, try again"
		fReplay()


#Displays Rules
def fRules():
	#Rules list
	print
	print "Once you've chosen a difficulty, enter letters to guess letters in the word"
	print "The number of underscores represents the length of your word"
	print "Once you've made 8 mistakes, you lose"
	print "You can keep track of your attempts by looking at the hangman or the counter above it"
	print "You can attempt to guess the entire word by entering more than one character"
	print "However, if you get it wrong, you will lose instantly"
	print
	print "Press enter/return to continue"
	raw_input()
	fIntro()


#Introductory message, user choses fDifficulty/fRules
def fIntro():
	print
	print "Welcome to Hangman"
	print
	print "Press 1 to play, 2 to view the rules"
	print
	iUserChoice = input("Enter a number: ")
	print
	if iUserChoice == 1 :
		#Run fDifficulty
		fDifficulty()
	elif iUserChoice == 2 :
		#Run fRules
		fRules()
	else :
		print "Error, invalid input"
		fIntro()

#------------------Initial Code (Run at first startup)---------------------#

fIntro()


