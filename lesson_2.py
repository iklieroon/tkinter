from tkinter import *
#from tkinter.ttk import *
root=Tk()
root.geometry()
'''root.title('menu')
menubar=Menu(root)
#adding the file menu and their commands
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=file)
file.add_command(label='New File',command=None)
file.add_command(label='Open',command=None)
file.add_command(label='Save',command=None)
file.add_separator()
file.add_command(label='Exit',command=None)

edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=edit)
edit.add_command(label='Undo',command=None)
edit.add_command(label='Redo',command=None)
edit.add_separator()
edit.add_command(label='Cut',command=None)
edit.add_command(label='Copy',command=None)
edit.add_command(label='Paste',command=None)

root.config(menu=menubar)

#progress bar widget
progress=Progressbar(root,orient=HORIZONTAL,length=100,mode='determinate')
def bar():
    import time
    progress['value']=20
    root.update_idletasks()
    time.sleep(1)
    progress['value']=40
    root.update_idletasks()
    time.sleep(1)
    progress['value']=60
    root.update_idletasks()
    time.sleep(1)
    progress['value']=80
    root.update_idletasks()
    time.sleep(1)
    progress['value']=100
progress.pack()
startbtn=Button(root,text='Start',command=bar)
startbtn.pack()'''

#frame
label1=Label(root,text='Chocos and Ice Cream',font='40').pack()
frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack(side=BOTTOM)

btn1=Button(frame1,text='Choco',fg='red',bg='white')
btn2=Button(frame1,text='Dark Choco',bg='white',fg='brown')
btn3=Button(frame1,text='White Choco',bg='white',fg='blue')
btn4=Button(frame2,text='Tiramisu',bg='blue',fg='green')
btn5=Button(frame2,text='Cake',bg='pink',fg='green')
btn6=Button(frame2,text='Pastry',bg='yellow',fg='green')
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack(side=TOP)
btn5.pack(side=TOP)
btn6.pack(side=TOP)

mainloop()