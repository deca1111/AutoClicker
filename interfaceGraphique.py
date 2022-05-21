from tkinter import *

from tkinter import ttk

maFenetre = Tk()

maFenetre.title("AutoClicker")
maFenetre.geometry("720x480")
maFenetre.minsize(720,480)
maFenetre.iconbitmap("images/b_pointer.ico")
maFenetre.config(background='#424549')



#creation frame
frameTitre = Frame(maFenetre, bg='#424549', bd =3, relief='raised')

#titre
title = Label(frameTitre, text="AutoClicker", font=("Bahnschrift SemiBold",50), bg='#424549', fg='#ffffff')
title.grid(row=0,column=0,columnspan=2,sticky='ew')
#sous-titre
subTitle = Label(frameTitre, text="Tout est bon pour pas réviser", font=("Bahnschrift SemiLight",15), bg='#424549', fg='#ffffff')
subTitle.grid(row=0,column=1)

#bouton = Button(frame, text="Selectionner le point d'ancrage de la souris", font=("Bahnschrift SemiLight",12), bg='#424549', fg='#ffffff', command = function)

frameTitre.pack(fill='both',side='bottom')
maFenetre.mainloop()
