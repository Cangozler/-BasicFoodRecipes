from cProfile import label
from cgitb import text
from tkinter import *  
import tkinter as tk

from PIL import ImageTk, Image  



window=tk.Tk()
window.title("Today I'm cooking")
window.geometry("500x500")
img = ImageTk.PhotoImage(Image.open("image.jpg"))






def enter():
  
    mate1=ent1.get()
    mate2=ent2.get()
    mate3=ent3.get()

    if mate1=="chicken" or mate2=="chicken" or mate3=="chicken":
        if mate1=="cream" or mate2=="cream" or mate3=="cream":
            if mate1=="pasta" or mate2=="pasta" or mate3=="pasta":
                f1=tk.Label(text="you can make fettuccine alfredo")
                f1.pack() 
                
    if mate1=="tomato" or mate2=="tomato" or mate3=="tomato":
        if mate1=="spice" or mate2=="spice" or mate3=="spice":
            if mate1=="water" or mate2=="water" or mate3=="water":
                f1=tk.Label(text="You canyou can make tomato soup")
                f1.pack()
    if mate1=="mince" or mate2=="mince" or mate3=="mince":
        if mate1=="cauliflower" or mate2=="cauliflower" or mate3=="cauliflower":
            if mate1=="broccoli" or mate2=="broccoli" or mate3=="broccoli":
                f1=tk.Label(text="You can make Minced Vegetable Meal")
                f1.pack() 
    if mate1=="chicken" or mate2=="chicken" or mate3=="chicken":
        if mate1=="butter" or mate2=="butter" or mate3=="butter":
            if mate1=="yogurt" or mate2=="yogurt" or mate3=="yogurt":
                f1=tk.Label(text="You can make Butter chicken")
                f1.pack() 
                label = Label(window, image = img)
                label.pack()                       

    else:  
        f1=tk.Label(text="you cant anything")  
        f1.pack()        
           

e1=tk.Label(text="Please write the first material",font="Arial 12 bold")
e2=tk.Label(text="Please write the second material",font="Arial 12 bold")
e3=tk.Label(text="Please write the third material",font="Arial 12 bold")

e1.pack()
ent1=tk.Entry(width=30)
ent1.pack()

e2.pack()
ent2=tk.Entry(width=25)
ent2.pack()

e3.pack()
ent3=tk.Entry(width=20)
ent3.pack()


b1=tk.Button(text="Get",bg="black",fg="white",font="Arial 20 bold",command=enter)
b1.pack()

window.mainloop()