import tkinter as tk
import random
from PIL import ImageTk, Image
import requests
from io import BytesIO
from tkinter import messagebox
import pymongo

root = tk.Tk()
root.config(bg= "#000000")
root.title("Sten - Sax - Påse")
options = ("sten", "sax", "påse")
spelarval = ""

# Frame

frame = tk.LabelFrame(root, bg="#ffffff", padx=50, pady=50)
frame.pack(padx=5, pady=10)

start_label = tk.Label(frame, bg="#ffffff", font=("Arial", 20), text="VÄLKOMMEN ATT SPELA\nSTEN - SAX - PÅSE")
start_label.grid(row=0, column=0, columnspan=3, padx=5, pady=10)
instruktion = tk.Label(frame, bg="#ffffff", font=("Arial", 14), text="Markera ditt val och tryck SPELA:")
instruktion.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
resultat = tk.Label(frame, bg="#ffffff", font=("Arial", 14), text="")
resultat_dator = tk.Label(frame, bg="#ffffff")
resultat_dator.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

def play(spelarval):
    global resultat
    global image_sten
    global image_sax
    global image_bag
    resultat.config(text="")
    spelare = spelarval
    dator = random.choice(options)

    if spelare == "":
        messagebox.showwarning("VARNING!", "Du måste välja sten, sax eller påse för att spela!")
    
    elif spelare == dator:
        resultat.config(text="Det är oavgjort! Datorn valde också:")

        if dator == "sten":
            resultat_dator.config(image=small_sten)
            resultat_dator.image = small_sten
        elif dator == "sax":
            resultat_dator.config(image=small_sax)
            resultat_dator.image = small_sax
        else:
            resultat_dator.config(image=small_bag)
            resultat_dator.image = small_bag

        resultat.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
        spelare = None
        frame.config(bg="#666967")
        start_label.config(bg="#666967")
        instruktion.config(bg="#666967")
        resultat.config(bg="#666967")
        resultat_dator.config(bg="#666967")

    elif spelare == "sten" and dator == "sax":
        resultat.config(text="DU VANN! Datorn valde:")
        resultat_dator.config(image=small_sax)
        resultat_dator.image = small_sax
        resultat.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
        spelare = None
        frame.config(bg="#0f8a3e")
        start_label.config(bg="#0f8a3e")
        instruktion.config(bg="#0f8a3e")
        resultat.config(bg="#0f8a3e")
        resultat_dator.config(bg="#0f8a3e")


    elif spelare == "påse" and dator == "sten":
        resultat.config(text="DU VANN! Datorn valde:")
        resultat_dator.config(image=small_sten)
        resultat_dator.image = small_sten
        resultat.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
        spelare = None
        frame.config(bg="#0f8a3e")
        start_label.config(bg="#0f8a3e")
        instruktion.config(bg="#0f8a3e")
        resultat.config(bg="#0f8a3e")
        resultat_dator.config(bg="#0f8a3e")

    elif spelare == "sax" and dator == "påse":
        resultat.config(text="DU VANN! Datorn valde:")
        resultat_dator.config(image=small_bag)
        resultat_dator.image = small_bag
        resultat.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
        spelare = None
        frame.config(bg="#0f8a3e")
        start_label.config(bg="#0f8a3e")
        instruktion.config(bg="#0f8a3e")
        resultat.config(bg="#0f8a3e")
        resultat_dator.config(bg="#0f8a3e")
    else:
        resultat.config(text=f"Du förlorade! Datorn valde:")
        
        if dator == "sten":
            resultat_dator.config(image=small_sten)
            resultat_dator.image = small_sten
        elif dator == "sax":
            resultat_dator.config(image=small_sax)
            resultat_dator.image = small_sax
        else:
            resultat_dator.config(image=small_bag)
            resultat_dator.image = small_bag

        resultat.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
        spelare = None
        frame.config(bg="#d10f22")
        start_label.config(bg="#d10f22")
        instruktion.config(bg="#d10f22")
        resultat.config(bg="#d10f22")
        resultat_dator.config(bg="#d10f22")
    

def button_click(bakgrundsfärg):
    global spelarval
    button_color = bakgrundsfärg
    global resultat
    global resultat_dator
    resultat.config(text="")
    resultat_dator.config(image="")
    resultat_dator.image = None

    if button_color == "sten":
        button_sten.config(bg="#348feb")
        button_sax.config(bg="#000000")
        button_bag.config(bg="#000000")
        spelarval = "sten"
    
    elif button_color == "sax":
        button_sax.config(bg="#348feb")
        button_sten.config(bg="#000000")
        button_bag.config(bg="#000000")
        spelarval = "sax"
    
    else:
        button_bag.config(bg="#348feb")
        button_sax.config(bg="#000000")
        button_sten.config(bg="#000000")
        spelarval = "påse"

# Hämta bilden från nätet
url1 = "https://systrarnasmat.com/onewebmedia/sten.png"
response1 = requests.get(url1)
image1 = Image.open(BytesIO(response1.content))
image1_small = image1.resize((100, 100))


url2 = "https://systrarnasmat.com/onewebmedia/sax.png"
response2 = requests.get(url2)
image2 = Image.open(BytesIO(response2.content))
image2_small = image2.resize((100, 100))

url3 = "https://systrarnasmat.com/onewebmedia/bag.png"
response3 = requests.get(url3)
image3 = Image.open(BytesIO(response3.content))
image3_small = image3.resize((100, 100))

# Gör bilden kompatibel med Tkinter
image_sten = ImageTk.PhotoImage(image1)
small_sten = ImageTk.PhotoImage(image1_small)
image_sax = ImageTk.PhotoImage(image2)
small_sax = ImageTk.PhotoImage(image2_small)
image_bag = ImageTk.PhotoImage(image3)
small_bag = ImageTk.PhotoImage(image3_small)


#buttons

button_sten = tk.Button(frame, bg="#000000", image=image_sten, fg="#ffffff", width=200, height=200, font=("Arial", 14), command=lambda: button_click("sten"))
button_sax = tk.Button(frame, bg="#000000", image=image_sax, fg="#ffffff", width=200, height=200, font=("Arial", 14), command=lambda: button_click("sax"))
button_bag = tk.Button(frame, bg="#000000", image=image_bag, fg="#ffffff", width=200, height=200, font=("Arial", 14), command=lambda: button_click("påse"))
button_play = tk.Button(frame, bg="#000000", text="SPELA", fg="#ffffff", padx=40, pady=20, font=("Arial", 14), command=lambda: play(spelarval))
button_exit = tk.Button(frame, bg="#000000", text="Avsluta", fg="#ffffff", padx=5, pady=5, font=("Arial", 10), command=root.quit)

#place the buttons on screen

button_sten.grid(row=2, column=0)
button_sax.grid(row=2, column=1)
button_bag.grid(row=2, column=2)
button_play.grid(row=6, column=1)
button_exit.grid(row=7, column=2, sticky="e")

root.mainloop()