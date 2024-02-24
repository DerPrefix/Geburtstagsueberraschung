import datetime
import time
from PIL import Image
from tkinter import messagebox
from tkinter import *
import tkinter as tk

import pygame

# Variable, um den Status der Aktion zu verfolgen
aktion_ausgefuehrt = False

now = datetime.datetime.now()


        
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Alles Gute zum Geburtstag!")
        self.master = master

        self.pack()
        # fullscreen
        self.master.attributes('-fullscreen', True)
        self.master.attributes("-topmost", True)
        
        self.create_widgets()

        self.master.lift()

                        


    def create_widgets(self):
        # ein Text Label
        self.label = tk.Label(self, text="Alles Gute zum Geburtstag!", font=("Arial", 100))
        self.label.pack()

        self.label = tk.Label(self, text="Du bist jetzt 50 Jahre alt! 👴", font=("Arial", 100))
        self.label.pack()

                # musik abspielen
        pygame.mixer.init()
        pygame.mixer.music.load("birthday.mp3")

        pygame.mixer.music.play()
        


                
                
                
                




            
root = tk.Tk()
app = Application(master=root)

app.mainloop()
        
                


aktion_ausgefuehrt = True

    



    # Warten Sie 1 Sekunde, bevor Sie den nächsten Check durchführen
time.sleep(1)
