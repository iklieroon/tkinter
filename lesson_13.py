from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.config(background='black')
root.title('Jumbled word game')
jumbledwordlabel=Label(root,text='',bg='black',fg='white',font=('arial',20))
wordlist=['python','table','elephant','speaker','switch','station','plane','closet','monkey','guitar']
score=0
qnum=0
s=''
scorelabel=Label(root)
jumblelist=[]
for i in wordlist:
    jumble=random.sample(i,len(i))
    jumblelist.append(''.join(jumble))
num=random.randint(0,len(jumblelist)-1)
jumbledwordlabel.config(text=jumblelist[num])
def reset():
    num=random.randint(0,len(jumblelist)-1)
    jumbledwordlabel.config(text=jumblelist[num])
    answerentry.delete(0,END)
def check():
    global score,qnum,s,scorelabel
    qnum+=1
    answer=answerentry.get()
    if answer==wordlist[num]:
        messagebox.showinfo(message='Your answer was correct')
        score+=1
    else:
        messagebox.showinfo(message='Your answer was incorrect')
    s='Score='+str(score)+'/'+str(qnum)
    scorelabel.forget()
    scorelabel=Label(root,text=s,font=('arial',15),background='black',foreground='white')
    scorelabel.pack(side=LEFT,pady=5)
    reset()
titlelabel=Label(root,text='JUMBLED WORD GAME',font=('arial',20),background='black',foreground='white')
answerentry=Entry(root,width=30)
checkbutton=Button(root,text='Check',command=check)
resetbutton=Button(root,text='Reset',command=reset)
titlelabel.pack(pady=5,padx=10)
jumbledwordlabel.pack(pady=5)
answerentry.pack(pady=5)
checkbutton.pack(pady=5)
resetbutton.pack(pady=5)
mainloop()