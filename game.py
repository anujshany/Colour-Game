import tkinter
import random

#list of possible colours,
colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score = 0

#the game time left initially 30 seconds
timeleft = 30

#function that will start the game
def startGame(event):
	if timeleft == 30:
		#start the countdown of the timer.
		countdown()
	#run the function to choose the next colour.
	nextColour()

def nextColour():
	#use the globally declared 'score'
	#and 'play' variables above
	global score
	global timeleft

	#if a game is currently in play
	if timeleft > 0:

		#make thr text entry box active
		e.focus_set()

		#to the colour typed is equal to the colour of the text
		if e.get().lower() == colours[1].lower():

			score+=1
		#clear the text entry box.
		e.delete(0, tkinter.END)

		random.shuffle(colours)

		#change the colour to type, by changing the text _and_the colour to a random colour value
		label.config(fg = str(colours[1]), text = str(colours[0]))

		#update the score
		scoreLable.config(text ="Score" + str(score))
def countdown():
	global timeleft

	#if a game is in play
	if timeleft > 0:
		#decrement the timer
		timeleft -=1
		#update the time left label
		timeLabel.config(text = "Time left:" + str(timeleft))
		#run the function again after 1 second.
		timeLabel.after(1000, countdown)
#creating a GUI window
root = tkinter.Tk()
#set the title
root.title("Colour Game")
#set the size
root.geometry("375x200")
#adding a instruction label
instructions = tkinter.Label(root, text = "Type in the colour of the words, and do not type the text:", font=('Helvetica',12))
instructions.pack()
#add a score label
scoreLable = tkinter.Label(root, text = "Press enter to start", font=("Helvetica",12))
scoreLable.pack()
#add a time left label
timeLabel = tkinter.Label(root, text = "Time Left", font=("Helvetica",12))
timeLabel.pack()
#add a label for displaying the colours
label = tkinter.Label(root, font=('Helvetica',60))
label.pack()
#add a text entry box for typing in the colours
e = tkinter.Entry(root)
#run the 'startgame'function when the enter key is pressed
root.bind('<Return>',startGame)
e.pack()
#set focus on the entry box
e.focus_set()
#start the GUI
root.mainloop()
