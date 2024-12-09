from tkinter import *
import random
import tkinter.messagebox
root=Tk()
root.geometry('350x150')
root.title('Guess the number game!')
guessnumber=random.randint(1,20)
def messagebox1():
    name=entry1.get()
    tkinter.messagebox.showinfo(message=f'Welcome{name}, I have a game for you, I am thinking of a number from 1-20, take a guess!')
def gamewin():
    guess=int(entry2.get())
    if guess>guessnumber:
        tkinter.messagebox.showinfo(message='You lose! My number was lower than your number!')
    elif guess<guessnumber:
        tkinter.messagebox.showinfo(message='You lose! My number was higher than your number!')
    elif guess==guessnumber:
        tkinter .messagebox.showinfo(message='Well done! You guessed my number correctly!')
label1=Label(root,text='Welcome to our game!').pack()
frame=Frame(root)
frame.pack()
label2=Label(frame,text="What's your name?").grid(row=1,column=0)
entry1=Entry(frame,width=20)
entry1.grid(row=2,column=0)
label0=Label(frame,text='                      ').grid(row=2,column=1)
button1=Button(frame,text='OK',command=messagebox1).grid(row=2,column=2)
label00=Label(frame,text=' ').grid(row=3,column=0)
label3=Label(frame,text='Take a guess:').grid(row=4,column=0)
entry2=Entry(frame,width=5)
entry2.grid(row=5,column=0)
button2=Button(frame,text='Guess',command=gamewin).grid(row=5,column=2)
mainloop()