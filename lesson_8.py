from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title('math calculator')
root.geometry('600x650')
titlelabel=Label(root,text='Math Multiplier').pack()
numlabel=Label(root,text='Select the number:')
numlabel.place(x=20,y=50)
#combobox creation
num=IntVar()
combobox=Combobox(root,textvariable=num,width=5)
combobox['values']=tuple(range(1,101))
combobox.place(x=150,y=50)

multiplylabel=Label(root,text='How many multiples would you like:')
multiplylabel.place(x=250,y=50)
#radiobuttons
num1=IntVar()
r1=Radiobutton(root,text='10',variable=num1,value=10)
r2=Radiobutton(root,text='20',variable=num1,value=20)
r3=Radiobutton(root,text='30',variable=num1,value=30)
r1.place(x=450,y=50)
r2.place(x=450,y=70)
r3.place(x=450,y=90)

def generatetable():
    tables=''
    for i in range(num1.get()+1):
        tables+=str(num.get())+' x '+str(i)+' = '+str(num.get()*i)+'\n'
    table.configure(text=tables)

button=Button(root,text='Multiply',command=generatetable)
button.place(x=250,y=125)
table=Label(root,anchor='center')
table.place(x=250,y=150)
mainloop()
