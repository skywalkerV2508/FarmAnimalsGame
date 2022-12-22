# Defining constants
MINSIZE = 1000, 800
STARTINGWINSIZE = 1000, 800
STARTINGWINX, STARTINGWINY = STARTINGWINSIZE

MAXFPS = 60
TITLE = "Farm Animals"
FOREGROUND_VISIBILITY = False

AMMOUNT_OF_COINS = 20

#QUESTIONS_FOR_ROUND1 = ["cat", "cow", "horse", "duck", "sheep", "dog", "pig", "kitten", "puppy"]
#QUESTIONS_FOR_ROUND1 = ["cat", "horse", "duck", "sheep", "dog", "pig", "kitten"]
QUESTIONS_FOR_ROUND1 = ["cat", "horse", "duck", "duck", "puppy", "puppy", "puppy", "puppy", "puppy", "puppy", "puppy", "puppy", "puppy", "puppy", "puppy"]

QUESTIONS_FOR_ROUND2 = ["rabbit", "hen", "goat", "chick", "donkey", "goose", "cock"]
QUESTIONS_FOR_ROUND3 = QUESTIONS_FOR_ROUND1.copy()
QUESTIONS_FOR_ROUND3.extend(QUESTIONS_FOR_ROUND2)

AMMOUNT_OF_BUTTONS_FR1 = len(QUESTIONS_FOR_ROUND1)
AMMOUNT_OF_BUTTONS_FR2 = len(QUESTIONS_FOR_ROUND2)
AMMOUNT_OF_BUTTONS_FR3 = len(QUESTIONS_FOR_ROUND3)

# Colors
CP_COLOR = (0, 0, 0, 150)
HP_COLOR = (0, 0, 0, 100)
TEXTLESSONCOLOR = "black"
TEXTROUNDCOLOR = "black"
