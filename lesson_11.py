from tkinter import *
from gtts import gTTS
import os
def convert():
    audio=gTTS(text=wordentry.get(),lang='cn',slow=False)
    audio.save('pyaudio.wav')
    os.system('pyaudio.wav')
root=Tk()
titlelabel=Label(root,text='Text to Speech Converter')
titlelabel.pack(padx=5,pady=5)
wordentry=Entry(root,width=50)
wordentry.pack(padx=5,pady=10)
submitbutton=Button(root,text='Submit',command=convert)
submitbutton.pack(padx=5,pady=10)
mainloop()