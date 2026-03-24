from tkinter import *
window = Tk()

#Interface Graphique Utilisateur (GUI) est un type d'interface
# qui permet aux utilisateurs d'interagir avec des appareils électroniques à travers des
# éléments graphiques tels que des boutons, des fenêtres et des icônes,
# plutôt que des commandes textuelles.
# L'interface graphique rend les logiciels plus conviviaux pour les utilisateurs moyens.


window.geometry("420x420")
window.title("titre GUI")


#changer icone
icone = PhotoImage(file='icone.png')
window.iconphoto(True,icone)
window.config(background = "#969939")
photo=PhotoImage(file='img.png')

label = Label(window,     #Un Label est un widget (composant d'interface)
              # dans tkinter utilisé pour afficher du texte non modifiable ou des images à l'écran.
              text="Hello IA102",
              font=("Arial", 20,'bold'),
              fg="black",
              bg="#969939",
              relief=RAISED,#tlaa
              borderwidth=1,#largeur de la bordure!!
              bd=9,
              padx=20,  #ajouter des pixels between
              pady=20,#y part
              image=photo,
              compound='bottom')
label.pack(pady=20)
label.pack(pady=20)


count=0
def click():
    global count
    count += 1
    label.config(text=count)
    print(count)
    print(" Welcome to T-k=inter's world!")
button = Button(window,text="Click me!!!" )
button.config(command=click)
button.config(font=("Arial", 15,'bold'))
button.config(activebackground="#7f9939")

button.pack(pady=20)
 
window.mainloop()

#apperance 