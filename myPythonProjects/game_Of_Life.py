from tkinter import *
import random
w=Tk()
w.title('Game Of Life')
w.geometry('1920x1080')
w.config(bg='#fff',)
c=Canvas(
w,
height=1080,
width=1920,
)
rectangles=[]
color=["red","yellow","black"]
for x in range(0,30):
    for y in range(0,15):
        k=c.create_rectangle(2+x*66,2+y*66,2+((x+1)*66),2+((y+1)*66),outline='#fb0')
        c.itemconfig(k,fill=color[random.randint(0,2)])
        rectangles.append(k)

def colorChange():
    for a in rectangles:  
        if(c.itemcget(a,'fill')=='red'):
            c.itemconfig(a,fill='yellow')
        elif(c.itemcget(a,'fill')=='yellow'):
            c.itemconfig(a,fill='black')
        elif(c.itemcget(a,'fill')=='black'):
            c.itemconfig(a,fill='red')   
        c.pack()

def rectangleFlick():
    c.after(500,rectangleFlick)  
    colorChange()

rectangleFlick()

# def colorChange():
#     c.after(500,colorChange)   
#     if(c.itemcget(r1,'fill')=='red'):
#         c.itemconfig(r1,fill='yellow')
#     elif(c.itemcget(r1,'fill')=='yellow'):
#         c.itemconfig(r1,fill='black')
#     elif(c.itemcget(r1,'fill')=='black'):
#         c.itemconfig(r1,fill='red')   
# colorChange()

w.mainloop()

