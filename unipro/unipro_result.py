import mysql.connector
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

# afficher les informations de la table
def afficher():
    con=pymysql.connect(host="localhost", user="root", password="",database="ma_base")
    cursor=con.cursor()
    cursor.execute("select * from etudiant")
    resultat=cursor.fetchall()
    if len(resultat):
        table.delete(*table.get_children())
        for row in resultat:
            table.insert('', END, values=row)
    con.close()

# creation de connexion avec les fonction
def enregistrer():
    noms=noms_saisi.get()
    prenoms=prenoms_saisi.get()
    classe =classe_saisi.get()
    sexe =sexe_saisi.get()
    licence =licence_saisi.get()
    numero =numero_matricule_saisi.get()

    if(noms=="" or prenoms=="" or classe=="" or
        sexe=="" or licence=="" or numero==""):
        messagebox.showinfo("merci de remplire tous les champs ")
    else:
        con=pymysql.connect(host="localhost", user="root", password="",database="ma_base")
        cursor=con.cursor()
        cursor.execute("insert into etudiant values('"+ noms +"','"+ prenoms +"','"+ classe+"','"+ sexe +"','"+ licence +"','"+ numero +"')")
        cursor.execute("commit")

        #suppression apres l'enregistrement
        noms_saisi.delete(0,'end')
        prenoms_saisi.delete(0, 'end')
        classe_saisi.delete(0, 'end')
        sexe_saisi.delete(0, 'end')
        licence_saisi.delete(0, 'end')
        numero_matricule_saisi.delete(0, 'end')
        messagebox.showinfo("Ajoue etudiant","Etudiant a bien été ajouter")
        con.close()

def supprimer():
    con = pymysql.connect(host="localhost", user="root", password="", database="ma_base")
    cursor = con.cursor()
    cursor.execute("DELETE FROM etudiant WHERE noms=%s",noms_saisi.get())
    cursor.execute("commit")

    afficher()
    con.close()
    messagebox.showinfo("suppression", "supression reussi")

def modifier():
    noms = noms_saisi.get()
    prenoms = prenoms_saisi.get()
    classe = classe_saisi.get()
    sexe = sexe_saisi.get()
    licence = licence_saisi.get()
    numero = numero_matricule_saisi.get()

    con = pymysql.connect(host="localhost", user="root", password="", database="ma_base")
    cursor = con.cursor()
    cursor.execute("update etudiant SET noms='"+ noms +"',prenoms='"+prenoms +"'classe='"+ classe + "'sexe='"+ sexe +"'licence='"+ licence +"' where numero='"+numero+"'")
    cursor.execute("commit")

    noms_saisi.delete(0, 'end')
    prenoms_saisi.delete(0, 'end')
    classe_saisi.delete(0, 'end')
    sexe_saisi.delete(0, 'end')
    licence_saisi.delete(0, 'end')
    numero_matricule_saisi.delete(0, 'end')
    con.close()
    messagebox.showinfo("modifier", "modification reussi")



#En tête de la fenetre
root=Tk()
root.title("UNIPRO resultat")
#root.iconbitmap("logo.ico")
root.config(background='#040F79')
root.geometry("1000x700")
root.resizable(width=False, height=False)

#titre général
lbltitre =Label(root,bd = 20, relief = RIDGE,text = "CONSULTEZ VOS RESULTATS",
font = ("Arial", 30), bg = "darkblue", fg="white")
lbltitre.place(x = 0, y = 0, width = 1000)

#Liste des patients
lblListePatient = Label(root, text = "LISTES DES ETUDIANTS", font = ("Arial", 16), bg = "white", fg="darkblue")
lblListePatient.place(x=380,y=110,width=598)


#formulaires
noms= Label(root, text="NOMS", font = ("Arial", 14) ,bg='#040F79', fg="white")
prenoms= Label(root, text="PRENOMS", font = ("Arial", 14) , bg='#040F79', fg="white")
classe= Label(root, text="CLASSE", font = ("Arial", 14) , bg='#040F79', fg="white")
sexe= Label(root, text="SEXE", font = ("Arial", 14) , bg='#040F79', fg="white")
licence= Label(root, text="LICENCE", font = ("Arial", 14) , bg='#040F79', fg="white")
numero_matricule= Label(root, text="N° MATRICULE", font = ("Arial", 14) , bg='#040F79', fg="white")

#formulaires champ de texte
noms_saisi= Entry(root, bd=4, font=("Arial", 13))
prenoms_saisi=Entry(root, bd=4, font=("Arial", 13))
classe_saisi=Entry(root, bd=4, font=("Arial", 13))
sexe_saisi= Entry(root, bd=4, font=("Arial", 13))
licence_saisi= Entry(root, bd=4, font=("Arial", 13))
numero_matricule_saisi= Entry(root, bd=4, font=("Arial", 13))

#Affichage de champ de texte
noms_saisi.place(x=160, y=150, width=180)
prenoms_saisi.place(x=160, y=200, width=180)
classe_saisi.place(x=160, y=250, width=180)
sexe_saisi.place(x=160, y=300, width=180)
licence_saisi.place(x=160, y=350, width=180)
numero_matricule_saisi.place(x=160, y=400, width=180)

#Affichage de formulaire
noms.place(x=50, y=150)
prenoms.place(x=28, y=200)
classe.place(x=30, y=250)
sexe.place(x=40, y=300)
licence.place(x=30, y=350)
numero_matricule.place(x=16, y=400)

#Les boutons
#Enregistrer
bouton_enregistrer = Button(root, text = "Enregistrer", font = ("Arial", 16),bg = "darkblue", fg = "yellow", command=enregistrer)
bouton_enregistrer.place(x=25, y= 450, width=150)

#modifier
btnmodofier = Button(root, text = "Modifier", font = ("Arial", 16),bg = "darkblue", fg = "yellow", command=modifier)
btnmodofier.place(x=210, y= 450, width=150)

#Supprimer
btnSupprimer = Button(root, text = "Supprimer", font = ("Arial", 16),bg = "darkblue", fg = "yellow", command=supprimer)
btnSupprimer.place(x=25, y= 500, width=150)

#sortir
sortir = Button(root, text = "Afficher", font = ("Arial", 16),bg = "darkblue", fg = "yellow",command=afficher)
sortir.place(x=210, y= 500, width=150)

#Table
table = ttk.Treeview(root, columns=(1,2,3,4,5,6), height = 5, show = "headings")
table.place(x = 380,y = 148, width = 600, height = 510)
#Entete
table.heading(1 , text = "NOM")
table.heading(2 , text = "PRENOM")
table.heading(3 , text = "CLASSE")
table.heading(4 , text = "SEXE")
table.heading(5 , text = "LICENCE")
table.heading(6 , text = "N°")

#definir les dimentions des colonnes
table.column(1,width = 150)
table.column(2,width = 150)
table.column(3,width = 80)
table.column(4,width = 80)
table.column(5,width = 80)
table.column(6,width = 80)


root.mainloop()