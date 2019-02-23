from Tkinter import *
import tkMessageBox
import mysql.connector


top=Tk()
top.title("login")
top.config(bg="aqua")
top.geometry("1600x800+0+0")
def cancel():
    top.destroy()
    
def submit():
    top.destroy()
    

    conn=mysql.connector.connect(user="root",password="",host="localhost",database="login")
    cursor=conn.cursor()

    if(e1.get()==("") or e2.get()==("")):
        tkMessageBox.showinfo("alert","fill all entities")

    elif(e1.get()==("arpit") and e2.get()==("123456")):
        top.destroy()
        import trainandtrack

    else:
        
        cursor.excecute("select * from  where userid="+e1.get()+ "' and password="'+e2.get()+""')

        if(cursor.fetchone()):
           top.destroy()
           

        else:
           tkMessageBox.showinfo("alert","login unsuccessful")
     
    
l1=Label(top,text="MEDICAL HELP",bg="light blue",fg="white",font=("castellar",(50),"bold","italic"),width=1600,height=2)
l1.pack()
l2=Label(top,text="User Id",fg="red",bg="aqua",font=("times new roman",(25),"bold"),bd=6)
l2.place(x=400,y=180)
e1=Entry(top,width=30,font=("times new roman",(15)))
e1.place(x=600,y=200)

l3=Label(top,text="Password",fg="red",bg="aqua",font=("times new roman",(25),"bold"),bd=6)
l3.place(x=400,y=250)
e2=Entry(top,width=30,font=("times new roman",(15)))
e2.place(x=600,y=270)

b1=Button(top,text="Login",command=submit,font=("times new roman",(15),"bold"),padx=6,pady=3,bd=5)
b1.place(x=600,y=340)

b2=Button(top,text="Cancel",command=cancel,font=("times new roman",(15),"bold"),padx=6,pady=3,bd=5)
b2.place(x=750,y=340)

top.mainloop()

