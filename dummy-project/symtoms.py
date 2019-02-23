from Tkinter import *
import ttk
import tkMessageBox
import mysql.connector
root=Tk()
root.title("symtoms")
root.geometry("1600x800+0+0")
root.config(bg="aqua")


var1=StringVar()

res1=StringVar()
res2=StringVar()
res3=StringVar()
res4=StringVar()
res5=StringVar()


def submit():
       
    import numpy as np
    from numpy import genfromtxt
    from sklearn import linear_model
    # Load dataset
    file=(genfromtxt("Book2.csv",delimiter=',',dtype='str'))  


    dic={}
    count=0
    for val in file:
        if val[5] not in dic:
            dic[val[5]]=count
            count+=1



    for val in file:
        val[5]=dic[val[5]]


    trainingset=file
    testingset=file[28:]

    trainingx=trainingset[:,[0,1,2,3,4]]
    trainingx=trainingx.astype(float)
    trainingy=trainingset[:,[5]]

    testingx=testingset[:,[0,1,2,3,4,5]]
    testingx=trainingx.astype(float)
    testingy=testingset[:,[5]]


    lis=[]
    lis.insert(0,int(e1.get()))
    lis.insert(1,int(e2.get()))
    lis.insert(2,int(e3.get()))
    lis.insert(3,int(e4.get()))
    lis.insert(4,int(e5.get()))

    print(lis)
    
    lr=linear_model.LogisticRegression()
    lr.fit(trainingx,trainingy)

   

    a=int(lr.predict([lis]))

    for x in dic:
        if(dic[x]==a):
            var1.set("%s"%x)
    

   



    

    
def reset():
    res1.set('')
    res2.set('')
    res3.set('')
    res4.set('')
    res5.set('')
    var1.set('')
    

    


l1=Label(root,text="MEDICAL HELP",bg="light blue",fg="white",font=("castellar",(50),"bold","italic"),width=1300,height=1)
l1.pack()   
Label(root,text="fever",fg="black",font=3).place(x=195,y=147)
Label(root,text="min. B.P",fg="black",font=3).place(x=195,y=250)
Label(root,text="max. B.P",fg="black",font=3).place(x=195,y=350)
Label(root,text="pulse rate",fg="black",font=3).place(x=195,y=450)
Label(root,text="cold",fg="black",font=3).place(x=195,y=550)
Label(root,text="predicted desease",fg="black",font=3).place(x=195,y=750)



e1=Entry(root,width=15,textvariable=res1,font=("times new roman",(15)))
e1.place(x=400,y=147)



e2=Entry(root,width=15,textvariable=res2,font=("times new roman",(15)))
e2.place(x=400,y=250)



e3=Entry(root,width=15,textvariable=res3,font=("times new roman",(15)))
e3.place(x=400,y=350)





e4=Entry(root,width=15,textvariable=res4,font=("times new roman",(15)))
e4.place(x=400,y=450)








e5=Entry(root,width=15,textvariable=res5,font=("times new roman",(15)))
e5.place(x=400,y=550)



e6=Entry(root,textvariable=var1,width=15,font=("times new roman",(15)))
e6.place(x=400,y=750)






















b1=Button(root,text="submit",command=submit,font=("times new roman",(15),"bold"))
b1.place(x=400,y=600)


b1=Button(root,text="reset",command=reset,font=("times new roman",(15),"bold"))
b1.place(x=700,y=600)




















root.mainloop()
