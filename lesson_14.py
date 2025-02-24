from tkinter import *
from tkinter.colorchooser import askcolor
class paint:
    def __init__(self):
        self.root=Tk()
        self.pen=Button(self.root,text='Pen')
        self.color=Button(self.root,text='Color')
        self.eraser=Button(self.root,text='Eraser')
        self.slider=Scale(self.root,from_=1,to=10,orient=HORIZONTAL,label='Pen width=')
        self.canvas=Canvas(self.root,bg='white',width=600,height=600)
        self.pen.grid(row=0,column=0)
        self.color.grid(row=0,column=1)
        self.eraser.grid(row=0,column=2)
        self.slider.grid(row=0,column=3)
        self.canvas.grid(row=1,columnspan=4)
        self.setup()
        self.root.mainloop()
    def setup(self):
        self.x=None
        self.y=None
        self.penwidth=self.slider.get()
        self.color='black'
        self.activebutton=self.pen
        self.canvas.bind('<B1-Motion>',self.paint)
        self.canvas.bind('<ButtonRelease-1>',self.reset)
    def activatebutton(self,button):
        self.activebutton.config(relief=RAISED)
        button.config(relief=SUNKEN)
        self.activebutton=button
    def penactivate(self):
        self.activatebutton(self.pen)
    def eraseractivate(self):
        self.activatebutton(self.eraser)
    def colorchoice(self):
        self.color=askcolor(color=self.color)[1]
    def paint(self,event):
        self.penwidth=self.slider.get()
        if self.activebutton==self.eraser:
            self.color='white'
        else:
            self.color
        if self.x and self.y:
            self.canvas.create_line(self.x,self.y,event.x,event.y,width=self.penwidth,fill=self.color)
        self.x=event.x
        self.y=event.y
    def reset(self,event):
        self.x,self.y=None
paint()