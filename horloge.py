from tkinter import *
import time

root = Tk()
root.title("horloge")

def current_time():
    string = time.strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, current_time)

def afficher_heure(heure_tuple):
    heure_formattee = '{:02d}:{:02d}:{:02d}'.format(*heure_tuple)
    label.config(text=heure_formattee)

label = Label(root, font=('arial', 80), foreground="cyan", background="black")
label.pack(anchor="center")

current_time()

heure_a_afficher = (12, 30, 45)  
afficher_heure(heure_a_afficher)

mainloop()
