from tkinter import *
from time import strftime
import random
root=Tk()
root.title('clock')
def time():
    #colors=['red','blue','green','orange','yellow','pink','purple']
    colors=f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'
    string=strftime('%I:%M:%S %p  %d/%m/%y')
    label1.config(text=string)
    label1.config(background=(colors))
    label1.after(1000,time)
label1=Label(root,font=('bahnschrift',40,'normal'),background='red',foreground='black')
label1.pack()
time()
mainloop()