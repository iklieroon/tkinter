from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox
root=Tk()
addressbook={}
def clear():
    nameentry.delete(0,END)
    addressentry.delete(0,END)
    mobileentry.delete(0,END)
    emailentry.delete(0,END)
    birthdayentry.delete(0,END)
def add():
    key=nameentry.get()
    if key=='':
        messagebox.showinfo(title='ERROR',message='ERROR, there must be a name.')
    else:
        if key not in addressbook.keys():
            addresslistbox.insert(END,key)
        addressbook[key]=addressentry.get(),mobileentry.get(),emailentry.get(),birthdayentry.get()
        clear()
    print(addressbook)
def edit():
    clear()
    nameselection=addresslistbox.curselection()
    if nameselection:
        nameentry.insert(0,addresslistbox.get(nameselection))
        details=addressbook[nameentry.get()]
        addressentry.insert(0,details[0])
        mobileentry.insert(0,details[1])
        emailentry.insert(0,details[2])
        birthdayentry.insert(0,details[3])
    else:
        messagebox.showinfo(title='ERROR',message='ERROR, you need to select a name from the list')
def delete():
    global addressbook
    selection=addresslistbox.curselection()
    if selection:
        del addressbook[addresslistbox.get(selection)]
        addresslistbox.delete(selection)
        clear()
    else:
        addresslistbox.delete(0,END)
        del addressbook
        clear()
def save():
    savevariable=asksaveasfile(defaultextension='.txt')
    if savevariable is not None:
        for i in addresslistbox.get(0,END):
            print(i,file=savevariable)
def open():
    openfile=askopenfile(title='openfile')
    if openfile is not None:
        items=openfile.readlines()
        for i in items:
            addresslistbox.insert(END,str(i))
def display(event):
    newwindow=Toplevel(root)
    selection=addresslistbox.curselection()
    details=''
    if selection:
        key=addresslistbox.get(selection)
        details='Name:'+key+'\n'
        keyvalues=addressbook[key]
        details+='Address: '+keyvalues[0]+'\n'
        details+='Mobile: '+keyvalues[1]+'\n'
        details+='Email: '+keyvalues[2]+'\n'
        details+='Birthday: '+keyvalues[3]+'\n'
    detaillabel=Label(newwindow,text=details)
    detaillabel.pack()








titlelabel=Label(root,text='My Address Book')
titlelabel.grid(row=0,column=0,columnspan=3)
openbutton=Button(root,text='Open',command=open)
openbutton.grid(row=0,column=4)
addresslistbox=Listbox(root,width=30,height=13)
addresslistbox.grid(row=2,column=0,columnspan=3,rowspan=5,padx=10,pady=10)
addresslistbox.bind('<<ListboxSelect>>',display)
namelabel=Label(root,text='Name:')
namelabel.grid(row=2,column=3)
nameentry=Entry(root,width=25)
nameentry.grid(row=2,column=4,padx=10)
addresslabel=Label(root,text='Address:')
addresslabel.grid(row=3,column=3)
addressentry=Entry(root,width=25)
addressentry.grid(row=3,column=4)
mobilelabel=Label(root,text='Mobile:')
mobilelabel.grid(row=4,column=3)
mobileentry=Entry(root,width=25)
mobileentry.grid(row=4,column=4)
emaillabel=Label(root,text='Email:')
emaillabel.grid(row=5,column=3)
emailentry=Entry(root,width=25)
emailentry.grid(row=5,column=4)
birthdaylabel=Label(root,text='Birthday:')
birthdaylabel.grid(row=6,column=3)
birthdayentry=Entry(root,width=25)
birthdayentry.grid(row=6,column=4)
editbutton=Button(root,text='Edit',command=edit)
editbutton.grid(row=7,column=0,pady=10)
deletebutton=Button(root,text='Delete',command=delete)
deletebutton.grid(row=7,column=1)
addbutton=Button(root,text='Add',command=add)
addbutton.grid(row=7,column=3)
savebutton=Button(root,text='Save',width=20,command=save)
savebutton.grid(row=7,column=4)
mainloop()