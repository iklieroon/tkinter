from tkinter import *
root=Tk()
def converter():
    gram=float(entry1.get())*1000
    pounds=float(entry1.get())*2.2046
    ounces=float(entry1.get())*35.274
    text1.delete('1.0',END)
    text1.insert('1.0',gram)
    text2.delete('1.0',END)
    text2.insert('1.0',pounds)
    text3.delete('1.0',END)
    text3.insert('1.0',ounces)
label1=Label(root,text='Enter the weight in Kg:')
entry1=Entry(root,width=30)
button1=Button(root,text='Convert',bd=0,background='grey',command=converter)
label2=Label(root,text='Gram')
label3=Label(root,text='Pounds')
label4=Label(root,text='Ounce')
text1=Text(root,height=1,width=20)
text2=Text(root,height=1,width=20)
text3=Text(root,height=1,width=20)
label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
button1.grid(row=0,column=2)
label2.grid(row=1,column=0)
label3.grid(row=1,column=1)
label4.grid(row=1,column=2)
text1.grid(row=2,column=0)
text2.grid(row=2,column=1)
text3.grid(row=2,column=2)
root.mainloop()