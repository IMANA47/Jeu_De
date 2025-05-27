import random
from tkinter import *
from PIL import ImageTk, Image


#les fonction
def jouer_de():
    pass


jeu = Tk()
jeu.title("Jeu De")
jeu.geometry('400x500+500+100')

# Label pour entrez valeurs

label1 = Label(jeu, text="Choisire un chiffre entre 1 et 6",bg="gray", fg="white",padx=10, pady=10, font=('Arial', 13, 'bold'))
label1.grid(column=1, row=1, columnspan=2)

#Champ text
numero_choisi = Entry(jeu)
numero_choisi.grid(column=1, row=2, columnspan=2, padx=10, pady=10)

# liste des image a recuperer
liste_images = ['images/de1.png', 'images/de2.png', 'images/de3.png', 'images/de4.png','images/de5.png' , 'images/de6.png' ]

# pour afficher les image et recuperer de maniere aleatoire
image_de = ImageTk.PhotoImage(Image.open(random.choice(liste_images)))
label_image = Label(jeu, image=image_de)
label_image.image = image_de
label_image.grid(column=1, row=3, columnspan=2)

# Boutton pour lancer le jeu
bouton_lancer = Button(jeu, text="Lance De", fg="yellow",bg="black", width=15, height=3,command= jouer_de)
bouton_lancer.grid(column=1, row=4,padx=10, pady=10)

# Boutton pour quitter le jeu
bouton_lancer = Button(jeu, text="Quitter", fg="white",bg="red", width=15, height=3,command=jeu.quit)
bouton_lancer.grid(column=2, row=4,padx=10, pady=10)

#Pour afficher le resultat

label_resultat = Label(jeu, text="allo", fg="black",pady=20, width=15, height=3)

label_resultat.grid(column=1, row=5, columnspan=2)


jeu.mainloop()