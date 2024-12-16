from tkinter import *
import tkinter.messagebox
import time
root=Tk()
root.geometry('325x300')
root.title('Timer')
hour=StringVar()
minute=StringVar()
second=StringVar()
hour.set('00')
minute.set('00')
second.set('00')
def timerfunction():
    temp=3600*int(hour.get())+60*int(minute.get())+int(second.get())
    while temp>-1:
        m,s=divmod(temp,60)
        h=0
        if m>60:
            h,m=divmod(m,60)
        hour.set('{00:2d}'.format(h))
        minute.set('{00:2d}'.format(m))
        second.set('{00:2d}'.format(s))
        root.update()
        time.sleep(1)
        if temp==0:
            tkinter.messagebox.showinfo(message='Timer Finished')
        temp-=1
hourentry=Entry(root,font=('bahnschrift',15,'normal'),textvariable=hour)
minuteentry=Entry(root,font=('bahnschrift',15,'normal'),textvariable=minute)
secondentry=Entry(root,font=('bahnschrift',15,'normal'),textvariable=second)
hourlabel=Label(root,text='Hours',font=('bahnschrift',15,'normal'))
minutelabel=Label(root,text='Minutes',font=('bahnschrift',15,'normal'))
secondlabel=Label(root,text='Seconds',font=('bahnschrift',15,'normal'))
startbutton=Button(root,text='Start Timer',command=timerfunction)
hourentry.place(x=5,y=50)
minuteentry.place(x=5,y=100)
secondentry.place(x=5,y=150)
hourlabel.place(x=225,y=50)
minutelabel.place(x=225,y=100)
secondlabel.place(x=225,y=150)
startbutton.place(x=130,y=250)
mainloop()