# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 20:19:57 2022

@author: Keviweto
"""

from tkinter import *
import random

root = Tk()
root.title("Testing random function")
root.geometry("600x700")

password_input = Entry(root)
password_guess = Label(root)
password_generated = Label(root)

array_3d = [[["1","2","3","4","a","A","b"",B"],["ps2ie","Hunter#","No#1df","win/lose2"],["!","@","#","$","&","y.s"]]]
print(array_3d[0][2][3])

def password():
    random_no1 = random.randint(0,7)
    random_no2 = random.randint(0,3)
    random_no3 = random.randint(0,5)
    
    letter1 = array_3d[0][0][random_no1]
    letter2 = array_3d[0][1][random_no2]
    letter3 = array_3d[0][2][random_no3]
    
    password_guess["text"] = "Guessed Password : " + password_input.get()
    password_generated["text"]= "Generated Password : " + letter1 + letter2 + letter3


btn = Button(root, text = "New Password", command = password)
btn.place(relx = 0.5, rely =0.5, anchor = CENTER)

password_input.place(relx = 0.5, rely = 0.3 , anchor = CENTER)
password_guess.place(relx = 0.5, rely = 0.4, anchor = CENTER)
password_generated.place(relx = 0.5, rely = 0.7 ,anchor = CENTER)
root.mainloop()
