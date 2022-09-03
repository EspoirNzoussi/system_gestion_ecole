from  subprocess import call
#from tkinter import ttk
from tkinter import *
from tkinter import messagebox
#import pywhatkit

'''def youtube():
    pywhatkit.playonyt("Tiakola melo soza")'''

#fonction de connexion
def connexion():
    nom_secret = utilisateur_saisi.get()
    mdp_secret = mdp_saisi.get()
    if(nom_secret== "" and mdp_secret== ""):
        messagebox.showerror("","Merci de remplire le formulaire")
        mdp_saisi.delete("0", "end")
        utilisateur_saisi.delete("0", "end")
    elif(nom_secret=="admin" and mdp_secret=="admin"):
        messagebox.showinfo("", "Bienvenue")
        utilisateur_saisi.delete("0", "end")
        mdp_saisi.delete("0", "end")
        root.destroy()
        call(["python", "unipro_result.py"])
    else:
        messagebox.showwarning("Erreur de connexion")
        utilisateur_saisi.delete("0", "end")
        mdp_saisi.delete("0", "end")

#Lancement du programme
root=Tk()
root.title("UNIPRO resultat")
#root.iconbitmap("logo.ico")
root.config(background='#040F79')
root.geometry("400x300")
root.resizable(width=False, height=False)

#titre général
lbltitre =Label(root,bd = 10, relief = RIDGE,text = "Formulaire de connexion", font = ("Arial", 20), bg = "darkblue", fg="white")
lbltitre.place(x = 0, y = 0, width = 400)

#Nom d'utilisateur et le mdp
Nom_utilisateur=Label(root, text="Nom Utilisateur", font = ("Arial", 14), bg="#040F79", fg="white")
mdp=Label(root, text="Mot de Passe", font = ("Arial", 14), bg="#040F79", fg="white")

#cham de saisi
utilisateur_saisi= Entry(root, bd=4, font=("Arial", 13))
mdp_saisi= Entry(root,show="*", bd=4, font=("Arial", 13))

#Affichage des label
Nom_utilisateur.place(x=5 , y=100 ,width=150)
utilisateur_saisi.place(x=150 , y=100, width=200, height=30)
mdp.place(x=5 , y=150 ,width=150)
mdp_saisi.place(x=150 , y=150, width=200, height=30)

#buton de validation
bouton= Button(root, text="Connexion", font=("Arial", 16), bg="#FF0000", fg="yellow", command=connexion)
bouton.place(x=150 , y=200 ,width=200)


root.mainloop()

