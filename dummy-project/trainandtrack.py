from Tkinter import *
import ttk
import tkMessageBox
import mysql.connector
root=Tk()
root.title("mdical help")
root.geometry("1600x800+0+0")
root.config(bg="aqua")


    
def train():
    root.destroy()
    import deases

   

def test():
    root.destroy()
    import symtoms    



l1=Label(root,text="MEDICAL HELP",bg="light blue",fg="white",font=("castellar",(50),"bold","italic"),width=1300,height=1)
l1.pack()     



b1=Button(root,text="train",command=train,font=("times new roman",(25),"bold"))
b1.place(x=195,y=147)

b2=Button(root,text="test",command=test,font=("times new roman",(25),"bold"))
b2.place(x=1200,y=147)

    




root.mainloop()
