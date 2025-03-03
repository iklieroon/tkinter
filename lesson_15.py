from tkinter import *
from tkinter.ttk import *
root=Tk()
size=StringVar(value='s')
def order():
    orderlabel.config(text=f'You ordered: {quantitycombobox.get()} {pizzacombobox.get()} {size.get()}')
titlelabel=Label(root,text='Welcome to Pizza Hut')
pizzalabel=Label(root,text='Select your Pizza')
quantitylabel=Label(root,text='Select how many Pizzas')
pizzaoptions=['Margerita','Pepperoni','BBQ Chicken','Veg']
pizzacombobox=Combobox(root,values=pizzaoptions,width=20)
quantityoptions=[1,2,3,4,5,6,7,8,9,10]
quantitycombobox=Combobox(root,values=quantityoptions)
orderbutton=Button(root,text='Order',command=order)
r1=Radiobutton(root,text='S',variable=size,value='Small Pizza(s)')
r2=Radiobutton(root,text='M',variable=size,value='Medium Pizza(s)')
r3=Radiobutton(root,text='L',variable=size,value='Large Pizza(s)')
orderlabel=Label(root,text='')
titlelabel.grid(row=0,column=1)
pizzalabel.grid(row=1,column=0)
quantitylabel.grid(row=2,column=0)
pizzacombobox.grid(row=1,column=1)
quantitycombobox.grid(row=2,column=1)
r1.grid(row=1,column=2)
r2.grid(row=2,column=2)
r3.grid(row=3,column=2)
orderbutton.grid(row=4,column=1)
orderlabel.grid(row=5,column=1)
mainloop()