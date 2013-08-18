import random, easygui
secret = random.randint(1, 100)
guess = 0
tries = 0
bowserfilepath = "C:\\Documents and Settings\\Owner\\Desktop\\Python Programs\\"
bowserFirst = bowserfilepath + "bowser.jpg"
bowserLose = bowserfilepath + "mario.gif"
tooLow = bowserfilepath + "Bowserinchair.jpg"
tooHigh = bowserfilepath + "fire.png"
mariofilepath = bowserfilepath + "mario\\"
youLose = mariofilepath + "SadMario.jpeg"


easygui.msgbox("""HEY! I'm Bowser, and I have a secret!"
 "It is a number from 1 to 99. I'll give you 6 tries.""","Bowser's Guessing Game","BLAMMO!",bowserFirst)

while guess != secret and tries < 6:
	guess = int(easygui.enterbox("What's your guess? "))
	if not guess: break
	if guess < secret:
		easygui.msgbox(str(guess) + " is too low, Mario!","Bowser's Guessing Game","BLAMMO!",tooLow)
	elif guess > secret:
		easygui.msgbox(str(guess) + " is too high, Luigi!","Bowser's Guessing Game","BLAMMO!",tooHigh)
	tries = tries + 1
if guess == secret:
	 easygui.msgbox("ROAR! You got it! Darn you Mario!","Bowser's Guessing Game","BLAMMO!",bowserLose)
else:
	easygui.msgbox("No more guesses! Bye, Mario!","Bowser's Guessing Game","BLAMMO!",youLose)
	