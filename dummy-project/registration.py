from Tkinter import *
import ttk
import tkMessageBox
import mysql.connector


top=Tk()
top.title("registration")
top.config(bg="aqua")
top.geometry("1600x800+0+0")
def cancel():
    top.destroy()
    
def signup():
    top.destroy()
    

    conn=mysql.connector.connect(user="root",password="",host="localhost",database="registration")
    cursor=conn.cursor()

    if(e1.get()==("") or e2.get()==("") or e3.get()==("") or e4.get()==("") or e5.get()==("") or e6.get()==("")):
        tkMessageBox.showinfo("alert","fill all entities")


    elif(e4.get()!=e5.get()):
         tkMessageBox.showinfo("Alert","enter correct password")   

   

    else:   
         cursor.execute("insert into signup(name,emailid,password,gender,age) values('"+e1.get()+"','"+e2.get()+"','"+e3.get()+"','"+e4.get()+"','"+e6.get()+"')")
         conn.commit()
         top.destroy()
         import medicaloginl   
     
    
l1=Label(top,text="MEDICAL HELP",bg="light blue",fg="white",font=("castellar",(50),"bold","italic"),width=1200,height=1)
l1.pack()
l2=Label(top,text="name",fg="red",bg="aqua",font=("times new roman",(25),"bold"),bd=6)
l2.place(x=400,y=180)
e1=Entry(top,width=30,font=("times new roman",(15)))
e1.place(x=600,y=200)

l3=Label(top,text="emailid",fg="red",bg="aqua",font=("times new roman",(25),"bold"),bd=6)
l3.place(x=400,y=250)
e2=Entry(top,width=30,font=("times new roman",(15)))
e2.place(x=600,y=270)

l4=Label(top,text="password",fg="red",bg="aqua",font=("times new roman",(25),"bold"),bd=6)
l4.place(x=400,y=310)
e3=Entry(top,width=30,font=("times new roman",(15)))
e3.place(x=600,y=330)

l5=Label(top,text="confirm pass.",fg="red",bg="aqua",font=("times new roman",(25),"bold"),bd=6)
l5.place(x=400,y=360)
e4=Entry(top,width=30,font=("times new roman",(15)))
e4.place(x=600,y=380)

l6=Label(top,text="age",fg="red",bg="aqua",font=("times new roman",(25),"bold"),bd=6)
l6.place(x=400,y=410)
e5=Entry(top,width=15,font=("times new roman",(15)))
e5.place(x=600,y=430)


l7=Label(top,text="gender",fg="red",bg="aqua",font=("times new roman",(25),"bold"),bd=6)
l7.place(x=400,y=460)
e5=Entry(top,width=15,font=("times new roman",(15)))
e5.place(x=600,y=480)




b1=Button(top,text="signup",command=signup,font=("times new roman",(15),"bold"),padx=6,pady=3,bd=5)
b1.place(x=400,y=600)

b2=Button(top,text="Cancel",command=cancel,font=("times new roman",(15),"bold"),padx=6,pady=3,bd=5)
b2.place(x=750,y=600)













top.mainloop()
