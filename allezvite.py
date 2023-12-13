from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk

#*************************************************************************************
def add(id,name,role,gender,status):
    conn=sqlite3.connect('myDb.db')
    cur=conn.cursor()
    cur.execute("create table if not exists compte(id TEXT,name TEXT,role TEXT,gender TEXT,status TEXT)")
    cur.execute("insert into compte(id,name,role,gender,status) values (?,?,?,?,?,?)",(id,name,role,gender,status))
    conn.commit()
def Afficher():
    conn = sqlite3.connect('myDb.db')
    cur = conn.cursor()
    cur.execute("create table if not exists compte(id TEXT,name TEXT,role TEXT,gender TEXT,status TEXT)")
    data=cur.execute("select * from compte").fetchall()
    conn.commit()
    return data

def update(id,n,r,g,s):
    conn = sqlite3.connect('myDb.db')
    cur = conn.cursor()
    cur.execute("create table if not exists compte(id TEXT,name TEXT,role TEXT,gender TEXT,status TEXT)")
    data = cur.execute("update compte set id=?,name=?,role=?,gender=? where status=?", (id, n, r, g, s))
    conn.commit()

def delete(idToDel):
    conn = sqlite3.connect('myDb.db')
    cur = conn.cursor()
    cur.execute("create table if not exists compte(num TEXT,prop TEXT,SI TEXT,type TEXT,ti TEXT,md TEXT)")
    data = cur.execute("delete from compte  where num=?", (str(idToDel),))
    conn.commit()

def Vider():
    conn = sqlite3.connect('myDb.db')
    cur = conn.cursor()
    cur.execute("create table if not exists compte(num TEXT,prop TEXT,SI TEXT,type TEXT,ti TEXT,md TEXT)")
    data = cur.execute("delete from compte")
    conn.commit()
    RechargerTree()
#*************************************************************************************
def ClearFields():
    textn1.delete(0,END)
    textn2.delete(0,END)
    textn3.delete(0,END)
    Op.delete(0,END)
    textn5.delete(0,END)

def RechargerTree():
    for data in tv.get_children():
        tv.delete(data)
    for result in Afficher():
        tv.insert(parent='', index='end', text="", values=(result), tag='orow')

def display(evt):
    ClearFields()
    selectedItem=tv.selection()[0]
    n1.config(text=tv.item(selectedItem)['values'][0])
    n2.insert(0,tv.item(selectedItem)['values'][1])
    n3.insert(0,tv.item(selectedItem)['values'][2])
    n4.insert(0,tv.item(selectedItem)['values'][3])
    n5.insert(0,tv.item(selectedItem)['values'][4])
    btn3.config(state=NORMAL)

def add_compte():
    id=textn1.get()
    name=textn2.get()
    role=textn3.get()
    gender=Op.get()
    status=textn5.get()
    if(id=="" or name=="" or role=="" or status==""):
        messagebox.showwarning('warning',"Tous les champs sont obligatoires !!!!")
    else:
        add(id,name,role,gender,status)
        messagebox.showinfo('info','inserted successfully !!!!')
        RechargerTree()
        ClearFields()
def Afficher_all():
    RechargerTree()

def edit_compte():
    rowToUpdate=tv.selection()[0]
    idToEdit=tv.item(rowToUpdate)["values"][0]
    name=textn2.get()
    role=textn3.get()
    gender=Op.get()
    status=textn5.get()
    update(idToEdit,name,role,gender,status)
    messagebox.showinfo('info', 'updated successfully !!!!')
    RechargerTree()
    ClearFields()

def delete_compte():
    if len(tv.selection())==0:
        messagebox.showwarning('warning','Vous devez sélectionner un compte !!!!')
    else:
        rowToUpdate = tv.selection()[0]
        idToDel = tv.item(rowToUpdate)["values"][0]
        delete(idToDel)
        messagebox.showinfo('info', 'deleted successfully !!!!')
        RechargerTree()
        ClearFields()

#*************************************************************************************
c = Tk()
c.geometry('800x300')
c.config(bg="black")
c.title("Employee Management System")

#*************************************************************************************


n1 = Label(c, text="ID :", bg="black", fg="white", pady=10).grid(row=0, column=0)
textn1 = Entry(c, font=('cursive', 12, 'bold'), bg='white', fg='black', width=12)
textn1.grid(row=0, column=1)

n2 = Label(c, text="Name :", bg="black", fg="white", pady=10).grid(row=1, column=0)
textn2 = Entry(c, font=('cursive', 12, 'bold'), bg='white', fg='black', width=12)
textn2.grid(row=1, column=1)

n3 = Label(c, text="Role :", bg="black", fg="white", pady=10).grid(row=2, column=0)
textn3 = Entry(c, font=('cursive', 12, 'bold'), bg='white', fg='black', width=12)
textn3.grid(row=2, column=1)

listg = ["Female", "Male", "Prefer not to say"]
val = StringVar(c)
val.set("Choose here")
n4 = Label(c, text="Gender :", bg="black", fg="white", pady=10).grid(row=3, column=0)
Op = OptionMenu(c, val, *listg)

Op.grid(row=3, column=1)

n5 = Label(c, text="Status :", bg="black", fg="white", pady=10).grid(row=4, column=0)
textn5 = Entry(c, font=('cursive', 12, 'bold'), bg='white', fg='black', width=12)
textn5.grid(row=4, column=1)

#*************************************************************************************

btn1=Button(c,text="Add Employee",bg="Green",fg="white",width=20,command=add_compte).place(x=15,y=210)
btn2=Button(c,text="Show Employees",bg="black",fg="white",width=20,command=Afficher_all).place(x=15,y=250)
btn3=Button(c,text="Update Employee",bg="black",fg="white",width=20,command=edit_compte).place(x=200,y=250)
btn4=Button(c,text="Delete Employee",bg="red",fg="white",width=20,command=delete_compte).place(x=390,y=250)

#*************************************************************************************






area=('ID', 'Name', 'Role', 'Gender', 'Status')
ac=('id','n','r','g','s')
tv=ttk.Treeview(c,columns=ac,show='headings',height=10)
for i in range(5):
    tv.column(ac[i],width=120,anchor='e')
    tv.heading(ac[i],text=area[i])
tv.place (x= 180, y =8)

tv.bind("<<TreeviewSelect>>", display)

c.mainloop()
