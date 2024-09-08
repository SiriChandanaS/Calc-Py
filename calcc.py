import tkinter as tk
from tkinter import *
total=""
def one():
    e1.insert(tk.END,"1")
def three():
    e1.insert(tk.END,"3")
def two():
    e1.insert(tk.END,"2")
def four():
    e1.insert(tk.END,"4")
def five():
    e1.insert(tk.END,"5")
def six():
    e1.insert(tk.END,"6")
def seven():
    e1.insert(tk.END,"7")
def eight():
    e1.insert(tk.END,"8")
def nine():
    e1.insert(tk.END,"9")
def zero():
    e1.insert(tk.END,"0")
def addn():
    e1.insert(tk.END,"+")
def subn():
    e1.insert(tk.END,"-")
def muln():
    e1.insert(tk.END,"*")
def divn():
    e1.insert(tk.END,"/")
def dott():
    abc=e1.get()
    if abc:
        e1.delete(len(abc)-1)
def dot():
    e1.insert(tk.END,".")
def solvee():
    a=e1.get()
    aa=eval(a)
    l1.config(text=aa)

root=Tk()
e1=Entry(root)
e1.grid(row=0,columnspan=4)
l1=Label(root)
l1.grid(row=1,columnspan=4)
b1=Button(root,text="1",command=one,bg='#ffffff', activebackground='#ADD8E6')
b2=Button(root,text="2",command=two,bg='#ffffff', activebackground='#ADD8E6')
b3=Button(root,text="3",command=three,bg='#ffffff', activebackground='#ADD8E6')
b4=Button(root,text="4",command=four,bg='#ffffff', activebackground='#ADD8E6')
b5=Button(root,text="5",command=five,bg='#ffffff', activebackground='#ADD8E6')
b6=Button(root,text="6",command=six,bg='#ffffff', activebackground='#ADD8E6')
b7=Button(root,text="7",command=seven,bg='#ffffff', activebackground='#ADD8E6')
b8=Button(root,text="8",command=eight,bg='#ffffff', activebackground='#ADD8E6')
b9=Button(root,text="9",command=nine,bg='#ffffff', activebackground='#ADD8E6')
b0=Button(root,text="0",command=zero,bg='#ffffff', activebackground='#ADD8E6')
ba=Button(root,text="+",command=addn,bg='#ffffff', activebackground='#ADD8E6')
bs=Button(root,text="-",command=subn,bg='#ffffff', activebackground='#ADD8E6')
bm=Button(root,text="*",command=muln,bg='#ffffff', activebackground='#ADD8E6')
bd=Button(root,text="/",command=divn,bg='#ffffff', activebackground='#ADD8E6')
bss=Button(root,text=".",command=dot,bg='#ffffff', activebackground='#ADD8E6')
btn=Button(root,text="<-",command=dott,bg='#ffffff', activebackground='#ADD8E6')
btns=Button(root,text="Solve",command=solvee,bg='#ffffff', activebackground='#ADD8E6')
btns.grid(row=6,columnspan=4)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)
ba.grid(row=2,column=3)
b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)
bs.grid(row=3,column=3)
b7.grid(row=4,column=0)
b8.grid(row=4,column=1)
b9.grid(row=4,column=2)
bm.grid(row=4,column=3)
bd.grid(row=5,column=3)
bss.grid(row=5,column=2)
b0.grid(row=5,column=0)
btn.grid(row=5,column=1)

root.mainloop()