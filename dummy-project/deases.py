from Tkinter import *
import ttk
import tkMessageBox
import csv
import mysql.connector


top=Tk()
top.title("deases")
top.config(bg="aqua")
top.geometry("1600x800+0+0")
def cancel():
    top.destroy()





res1=StringVar()
res2=StringVar()
res3=StringVar()
res4=StringVar()
res5=StringVar()
res6=StringVar()


def reset():
    res1.set('')
    res2.set('')
    res3.set('')
    res4.set('')
    res5.set('')
    res6.set('')
    
    


    
    
  
    
    conn= mysql.connector.connect(user="root",password="",host="localhost",database="deases")
    cursor=conn.cursor()

    

    

    if(e1.get()==("") or e2.get()==("")or e3.get()==("")or e4.get()==(""))or e5.get()==("")or e6.get()==(""):
        tkMessageBox.showinfo("alert","fill all entities")

    else: 
         
        cursor.execute("insert into upload(fever,min_BP,max_BP, PulseRate,Cold,desease) values('"+e1.get()+"','"+e2.get()+"','"+e3.get()+"','"+e4.get()+"','"+e5.get()+"','"+e6.get()+"')")
        conn.commit()
        csvData=[(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get())]
        with open('update.csv','a+') as csvFile :
             writer=csv.writer(csvFile)
             writer.writerows(csvData)
        csvFile.close()

def submit():
    import symtoms
    
    

   
     
    
l1=Label(top,text="MEDICAL HELP",bg="light blue",fg="white",font=("castellar",(50),"bold","italic"),width=1300,height=1)
l1.pack()
l2=Label(top,text="fever",fg="red",bg="aqua",font=("times new roman",(25),"bold"),bd=6)
l2.place(x=400,y=180)
e1=Entry(top,textvariable=res1,width=10,font=("times new roman",(15)))
e1.place(x=600,y=200)

l3=Label(top,text="min. B.P",fg="red",bg="aqua",font=("times new roman",(25),"bold"),bd=6)
l3.place(x=400,y=250)
e2=Entry(top,textvariable=res2,width=10,font=("times new roman",(15)))
e2.place(x=600,y=270)

l4=Label(top,text="max. B.P",fg="red",bg="aqua",font=("times new roman",(25),"bold"),bd=6)
l4.place(x=400,y=310)
e3=Entry(top,textvariable=res3,width=10,font=("times new roman",(15)))
e3.place(x=600,y=330)

l5=Label(top,text="pulse rate",fg="red",bg="aqua",font=("times new roman",(25),"bold"),bd=6)
l5.place(x=400,y=360)
e4=Entry(top,textvariable=res4,width=10,font=("times new roman",(15)))
e4.place(x=600,y=380)

l6=Label(top,text="cold",fg="red",bg="aqua",font=("times new roman",(25),"bold"),bd=6)
l6.place(x=400,y=410)
e5=Entry(top,textvariable=res5,width=10,font=("times new roman",(15)))
e5.place(x=600,y=430)






l7=Label(top,text="desease",fg="red",bg="aqua",font=("times new roman",(25),"bold"),bd=6)
l7.place(x=400,y=460)
e6=Entry(top,textvariable=res6,width=10,font=("times new roman",(15)))
e6.place(x=600,y=480)


b1=Button(top,text="submit",command=submit,font=("times new roman",(15),"bold"),padx=6,pady=3,bd=5)
b1.place(x=400,y=600)

b2=Button(top,text="Cancel",command=cancel,font=("times new roman",(15),"bold"),padx=6,pady=3,bd=5)
b2.place(x=750,y=600)


b3=Button(top,text="reset",command=reset,font=("times new roman",(15),"bold"),padx=6,pady=3,bd=5)
b3.place(x=900,y=600)















top.mainloop()
