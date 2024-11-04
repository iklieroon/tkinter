from tkinter import *
root=Tk()
root.geometry('1000x1000')
#btn=Button(root,text='click me',bd='100',background='black',foreground='white',font=('bahnschrift',40,'normal'),command=root.destroy)
#btn.pack(side='left')
root.title('login')
root.config(background='red')
userlabel=Label(root,text='username').place(x=75,y=75)
userentry=Entry(root,width=30).place(x=160,y=75)
passlabel=Label(root,text='password').place(x=75,y=110)
passentry=Entry(root,show='*',width=30).place(x=160,y=110)
btn1=Button(root,text='click me',bd=50,background='black',foreground='white',font=('bahnschrift',40,'normal')).place(x=75,y=220)
spinbox=Spinbox(root,from_=0,to=10,bd=50,font=('bahnschrift',40,'normal')).place(x=75,y=450)









































































root.mainloop()