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
color=["red","yellow","black"]
r1=c.create_rectangle(2,2,66,66,outline='#fb0')
for x in range(0,30):
    for y in range(0,15):
        k=c.create_rectangle(2+x*66,2+y*66,2+((x+1)*66),2+((y+1)*66),outline='#fb0')
        c.itemconfig(k,fill=color[random.randint(0,2)])
        c.pack()
# c.itemconfig(r1,fill='red')
# c.pack()
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

