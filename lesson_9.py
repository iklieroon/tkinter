from tkinter import *
from tkinter.filedialog import * 
root=Tk()
def open():
    openfile=askopenfile(title='openfile')
    if openfile is not None:
        items=openfile.readlines()
        for i in items:
            listbox.insert(END,str(i))
def delete():
    selection=listbox.curselection()
    if selection:
        listbox.delete(selection)
    else:
        listbox.delete(0,END)
def save():
    savevariable=asksaveasfile(defaultextension='.txt')
    if savevariable is not None:
        for i in listbox.get(0,END):
            print(i,file=savevariable)
def add():
    listbox.insert(END,addentry.get())
    addentry.delete(0,END)
savebutton=Button(root,text='SAVE',width=20,command=save).pack(pady=10)
addentry=Entry(root,width=30)
addentry.pack(pady=10)
addbutton=Button(root,text='ADD',width=20,command=add).pack(pady=10)
openbuton=Button(root,text='OPEN',width=20,command=open).pack(side=LEFT,padx=10)
deletebutton=Button(root,text='DELETE',width=20,command=delete).pack(side=RIGHT,padx=10)
scrollbar=Scrollbar(root,orient='vertical')
scrollbar.pack(side=RIGHT,fill=Y)
listbox=Listbox(root,width=70,yscrollcommand=scrollbar.set,background='red')
listbox.pack(pady=10)
for i in range(1,100):
    listbox.insert(END,'LIST '+str(i))
mainloop()