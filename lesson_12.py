from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox 
import speech_recognition as sr
import os
def speechconverter():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('READY')
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
        except:
            messagebox.showinfo(message='Sorry, your voice was not recognisable')
        speechtext.delete(1.0,END)
        speechtext.insert(END,text)
def save():
    savevariable=asksaveasfile(defaultextension='.txt')
    if savevariable is not None:
        print(speechtext.get(1.0,END),file=savevariable)
    else:
        messagebox.showinfo(message='Warning, text has not been saved')
root=Tk()
titlelabel=Label(root,text='SPEECH TO TEXT CONVERTER',font=('bahnschrift',30))
titlelabel.grid(row=0,column=0,columnspan=3)
recordbutton=Button(root,text='Click to start recording',command=speechconverter)
recordbutton.grid(row=1,column=0,padx=10,pady=10)
speechtext=Text(root,height=4,width=40)
speechtext.grid(row=1,column=1,padx=10,pady=10)
savebutton=Button(root,text='Save your text', command=save)
savebutton.grid(row=1,column=2,padx=10,pady=10)
mainloop()