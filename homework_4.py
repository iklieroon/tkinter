from tkinter import *
from time import strftime
import random
root=Tk()
root.title('clock')
def time():
    string=strftime('%I:%M:%S %p  %d %B %Y (%Z)')
    label1.config(text=string)
    label1.after(1000,time)
label1=Label(root,font=('bahnschrift',40,'normal'),background='red',foreground='black')
label1.pack()
time()
mainloop()