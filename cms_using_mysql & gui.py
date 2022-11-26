from tkinter import *
from tkinter import messagebox
import pymysql

con = pymysql.connect(host='localhost', user='root', password='root123', database='customers')
cur = con.cursor()


def addbtn_click():
    newid = int(varid.get())
    newname = str(varname.get())
    newage = int(varage.get())
    newmob = int(varmob.get())

    qry = f"insert into cus value({newid},'{newname}',{newage},{newmob})"
    cur.execute(qry)
    con.commit()
    con.close()
    messagebox.showinfo("CMS","Customer Added Succesfully")
    varid.set("")
    varname.set("")
    varage.set("")
    varmob.set("")


def searchbtn_click():
    searchid = int(varid.get())
    qry = f"select * from cus where id = {searchid}"
    cur.execute(qry)
    data = cur.fetchall()

    searchcus = Tk()
    searchcus.title("Search Customer")
    searchid = Label(searchcus, text="ID", font=("Times New Roman", 15), width=10)
    searchid.grid(row=0, column=0)
    searchname = Label(searchcus, text="Name", font=("Times New Roman", 15), width=10)
    searchname.grid(row=0, column=1)
    searchage = Label(searchcus, text="Age", font=("Times New Roman", 15), width=10)
    searchage.grid(row=0, column=0)
    searchmob = Label(searchcus, text="Mobile", font=("Times New Roman", 15), width=10)
    searchmob.grid(row=0, column=3)

    for id,name,age,mob in data:
        searchid1 = Label(searchcus, text=f"{id}", font=("Times New Roman", 15), width=10)
        searchid1.grid(row=1, column=0)
        searchname1 = Label(searchcus, text=f"{name}", font=("Times New Roman", 15), width=10)
        searchname1.grid(row=1, column=1)
        searchage1 = Label(searchcus, text=f"{age}", font=("Times New Roman", 15), width=10)
        searchage1.grid(row=1, column=0)
        searchmob1 = Label(searchcus, text=f"{mob}", font=("Times New Roman", 15), width=10)
        searchmob1.grid(row=1, column=3)

    con.close()
    varid.set("")
    varname.set("")
    varage.set("")
    varmob.set("")


def updatebtn_click():
    updateid = int(varid.get())
    updatename = str(varname.get())
    updateage = int(varage.get())
    updatemob = int(varmob.get())
    qry = f"update cus set name = '{updatename}',age = {updateage},mobile = {updatemob} where id = {updateid}"
    cur.execute(qry)
    con.commit()
    con.close()
    messagebox.showinfo("CMS","Customer updated succesfully")
    varid.set("")
    varname.set("")
    varage.set("")
    varmob.set("")



def deletebtn_click():
    delid = int(varid.get())
    qry = f"delete from cus where id = {delid}"
    cur.execute(qry)
    con.commit()
    con.close()
    messagebox.showinfo("CMS", "Customer Deleted Succesfully")
    varid.set("")
    varname.set("")
    varage.set("")
    varmob.set("")




def viewbtn_click():

    qry = f"select * from cus"
    cur.execute(qry)
    data = cur.fetchall()
    con.close()
    viewcus = Tk()
    viewcus.title("View All Customers")
    viewid = Label(viewcus, text="ID", font=("Times New Roman", 15), width=10)
    viewid.grid(row=0, column=0)
    viewname = Label(viewcus, text="Name", font=("Times New Roman", 15), width=10)
    viewname.grid(row=0, column=1)
    viewage = Label(viewcus, text="Age", font=("Times New Roman", 15), width=10)
    viewage.grid(row=0, column=0)
    viewmob = Label(viewcus, text="Mobile", font=("Times New Roman", 15), width=10)
    viewmob.grid(row=0, column=3)


    i = 1
    for id,name,age,mob in data:
        viewid1 = Label(viewcus, text=f"{id}", font=("Times New Roman", 15), width=10)
        viewid1.grid(row=i, column=0)
        viewname1 = Label(viewcus, text=f"{name}", font=("Times New Roman", 15), width=10)
        viewname1.grid(row=i, column=1)
        viewage1 = Label(viewcus, text=f"{age}", font=("Times New Roman", 15), width=10)
        viewage1.grid(row=i, column=0)
        viewmob1 = Label(viewcus, text=f"{mob}", font=("Times New Roman", 15), width=10)
        viewmob1.grid(row=i, column=3)
        i += 1


def exitbtn_click():
    root.destroy()


root = Tk()
root.geometry("800x300")
root.title("CMS")


lbl1 = Label(root, text = "Enter Id: ",font = ("Times New Roman",20))
lbl1.grid(row = 0,column = 0)

lbl2 = Label(root, text = "Enter Name: ",font = ("Times New Roman",20))
lbl2.grid(row = 1,column = 0)

lbl3 = Label(root, text = "Enter Age: ",font = ("Times New Roman",20))
lbl3.grid(row = 2,column = 0)

lbl4 = Label(root, text = "Enter Mobile: ",font = ("Times New Roman",20))
lbl4.grid(row = 3,column = 0)


varid = StringVar()
entrid = Entry(root,font = ("Times New Roman",20),textvariable = varid)
entrid.grid(row = 0, column = 1)

varname = StringVar()
entrname = Entry(root,font = ("Times New Roman",20),textvariable = varname)
entrname.grid(row = 1, column = 1)

varage = StringVar()
entrage = Entry(root,font = ("Times New Roman",20),textvariable = varage)
entrage.grid(row = 2, column = 1)

varmob = StringVar()
entrmob = Entry(root,font = ("Times New Roman",20),textvariable = varmob)
entrmob.grid(row = 3, column = 1)


addbtn = Button(root,text = "Add Customer",font = ("Times New Roman",20), command = addbtn_click)
addbtn.grid(row = 4,column = 0)

searchbtn = Button(root,text = "Search Customer",font = ("Times New Roman",20) , command = searchbtn_click)
searchbtn.grid(row = 4,column = 1)

updatebtn = Button(root,text = "Update Customer",font = ("Times New Roman",20), command = updatebtn_click)
updatebtn.grid(row = 4,column = 2)

deletebtn = Button(root,text = "Delete Customer",font = ("Times New Roman",20), command = deletebtn_click)
deletebtn.grid(row = 5,column = 0)

viewbtn = Button(root,text = "View Customers",font = ("Times New Roman",20), command = viewbtn_click)
viewbtn.grid(row = 5,column = 1)

exitbtn = Button(root,text = "Exit",font = ("Times New Roman",20), command = exitbtn_click)
exitbtn.grid(row = 5,column = 2)







root.mainloop()