import mouse
import time
import keyboard

UP = "\x1B[4A"
CLR = "\x1B[0K"

def autoClicker():
	print("Cliquer sur l'emplacement que vous voulez sauvegarder")
	emplacement = getPosition();
	print("Emplacement sauvegardé :", emplacement)
	print("Pour commencer à cliquer: [Clic mollette]")
	print("Pour pause/unpause le clic : [p]")
	print("Pour liberer/restreindre le deplacement de la souris : [m]")
	print("Pour sortir de l'application : [ECHAP]")
	isClicking = False

	mouse.wait(button='middle', target_types=('up', 'down', 'double'))
	clicker(emplacement)



def getPosition():
	mouse.wait(button='left',target_types=('up', 'down', 'double'))
	return mouse.get_position()

def clicker(pos):
	nbClick = 0
	canMove = False
	isClicking = True
	mouse.move(pos[0], pos[1], absolute=True)
	time.sleep(1)
	print("Début du clicking...")

	print("\n\n\n\n")
	while not keyboard.is_pressed("escape"):

		if(keyboard.is_pressed("p")):
			isClicking = not isClicking
			time.sleep(0.5)


		if(keyboard.is_pressed("m")):
			canMove = not canMove
			time.sleep(0.5)

		if isClicking:
			mouse.click(button='left')
			time.sleep(0.05)
			nbClick +=1

		if not canMove:
			if(mouse.get_position() != pos):
				mouse.move(pos[0], pos[1], absolute=True)

		print(f"{UP}Nombre de clic(s): {nbClick}{CLR}\nStatus:\n\tisClicking:{isClicking}{CLR}\n\tcanMove: {canMove}{CLR}")


autoClicker()
