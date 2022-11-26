from tkinter import *
from cms_oop import *
from tkinter import messagebox



def addbtn_click():
    cus = Customer()
    cus.id = varid.get()
    cus.name = varname.get()
    cus.age = varage.get()
    cus.mob = varmob.get()
    cus.addCustomer()
    messagebox.showinfo("Customer Added Succesfully")
    varid.set("")
    varname.set("")
    varage.set("")
    varmob.set("")



def searchbtn_click():
    try:
        cus = Customer()
        cus.id = varid.get()
        cus1 = cus.searchCustomer()
        searchcus = Tk()
        searchcus.title("Search Customer")
        searchid = Label(searchcus,text = "ID",font = ("Times New Roman",15),width = 10)
        searchid.grid(row = 0,column = 0)
        searchname = Label(searchcus, text="Name", font=("Times New Roman", 15), width=10)
        searchname.grid(row = 0,column = 1)
        searchage = Label(searchcus, text="Age", font=("Times New Roman", 15), width=10)
        searchage.grid(row = 0,column = 0)
        searchmob = Label(searchcus, text="Mobile", font=("Times New Roman", 15), width=10)
        searchmob.grid(row = 0,column = 3)

        searchid1 = Label(searchcus,text = f"{cus1.id}",font = ("Times New Roman",15),width = 10)
        searchid1.grid(row = 1,column = 0)
        searchname1 = Label(searchcus, text= f"{cus1.name}", font=("Times New Roman", 15), width=10)
        searchname1.grid(row = 1,column = 1)
        searchage1 = Label(searchcus, text=f"{cus1.age}", font=("Times New Roman", 15), width=10)
        searchage1.grid(row = 1,column = 0)
        searchmob1 = Label(searchcus, text=f"{cus1.mob}", font=("Times New Roman", 15), width=10)
        searchmob1.grid(row = 1,column = 3)

        varid.set("")
        varname.set("")
        varage.set("")
        varmob.set("")
    except AttributeError:
        messagebox.showinfo("Customer not found")
        varid.set("")
        varname.set("")
        varage.set("")
        varmob.set("")
        searchcus.destroy()

    except Exception as err:
        messagebox.showinfo(err)
        varid.set("")
        varname.set("")
        varage.set("")
        varmob.set("")
        searchcus.destroy()



def updatebtn_click():
    cus = Customer()
    cus.id = varid.get()
    cus.name = varname.get()
    cus.age = varage.get()
    cus.mob = varmob.get()
    var = cus.updateCustomer()

    if var == 1:
        messagebox.showinfo("CMS","Customer Updated Succesfully")
        varid.set("")
        varname.set("")
        varage.set("")
        varmob.set("")
    else:
        messagebox.showinfo("CMS","Customer not found")
        varid.set("")
        varname.set("")
        varage.set("")
        varmob.set("")


def deletebtn_click():
    cus = Customer()
    cus.id = varid.get()
    var = cus.deleteCustomer()
    if var == 1:
        messagebox.showinfo("CMS","Customer Deleted Succesfully")
    else:
        messagebox.showinfo("Customer not found")

def viewbtn_click():
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
    for cus in Customer.cus_list:
        viewid1 = Label(viewcus, text=f"{cus.id}", font=("Times New Roman", 15), width=10)
        viewid1.grid(row=i, column=0)
        viewname1 = Label(viewcus, text= f"{cus.name}", font=("Times New Roman", 15), width=10)
        viewname1.grid(row=i, column=1)
        viewage1 = Label(viewcus, text= f"{cus.age}", font=("Times New Roman", 15), width=10)
        viewage1.grid(row=i, column=0)
        viewmob1 = Label(viewcus, text= f"{cus.mob}", font=("Times New Roman", 15), width=10)
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