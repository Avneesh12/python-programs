"""Online Food Order """

import pymysql
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk


#class for customers
class Customers:
    def __init__(self):
        self.con = pymysql.connect(host="localhost", user="root", password="root123", database="food_order")
        self.cur = self.con.cursor()
        self.name = 0
        self.email = 0
        self.mobile = 0
        self.password = 0
        self.repassword = 0
        self.update_name = 0
        self.update_email = 0
        self.update_mobile = 0
        self.update_password = 0
        self.update_repassword = 0

    #method for save the sign up data to database
    def signup_succesfull_click(self):
        self.cus_name = self.name.get()
        self.cus_email = self.email.get()
        self.cus_mobile = self.mobile.get()
        self.cus_password = self.password.get()
        self.cus_repassword = self.repassword.get()
        if len(self.cus_name) < 5 or self.cus_name.isdecimal() == True :
            messagebox.showinfo("Sign up ","Please Enter Valid Name")
        elif len(self.cus_email) < 5 or self.cus_email.startswith('@') == True\
                or  self.cus_email.endswith('@') == True or ('@' in self.cus_email) == False :
            messagebox.showinfo("Sign up ", "Please Enter Valid Email Id")
        elif len(self.cus_mobile) != 10 or self.cus_mobile.isdecimal() == False:
            messagebox.showinfo("Sign up ", "Please Enter Valid Mobile No.")
        elif len(self.cus_password) < 6:
            messagebox.showinfo("Sign up ", "Please Enter Valid Password")
        elif self.cus_password != self.cus_repassword:
            messagebox.showinfo("Sign up ", "Please Check Your Password")
        else:
            self.cur.execute(
                f"insert into customer values('{self.cus_name}','{self.cus_email}',{self.cus_mobile},'{self.cus_password}')")
            self.con.commit()
            self.con.close()
            messagebox._show("Sign up","Sign up Succesfull")


#method for save the forgot password in database
    def forgot_password_succesful_click(self):
        self.cus_name = self.update_name.get()
        self.cus_email = self.update_email.get()
        self.cus_mobile = self.update_mobile.get()
        self.cus_password = self.update_password.get()
        self.cus_repassword = self.update_repassword.get()

        if len(self.cus_name) < 5 or self.cus_name.isdecimal() == True :
            messagebox.showinfo("Forgot Password ","Please Enter Valid Name")
        elif len(self.cus_email) < 5 or self.cus_email.startswith('@') == True\
                or  self.cus_email.endswith('@') == True or ('@' in self.cus_email) == False :
            messagebox.showinfo("Forgot Password", "Please Enter Valid Email Id")
        elif len(self.cus_mobile) != 10 or self.cus_mobile.isdecimal() == False:
            messagebox.showinfo("Forgot Password", "Please Enter Valid Mobile No.")
        elif len(self.cus_password) < 6:
            messagebox.showinfo("Forgot Password ", "Please Enter Valid Password")
        elif self.cus_password != self.cus_repassword:
            messagebox.showinfo("Forgot Password", "Please Check Your Password")
        else:
            self.cur.execute(f"update customer set password = '{self.cus_password}' where name = '{self.cus_name}' and email = '{self.cus_email}'")
            self.con.commit()
            self.con.close()
            messagebox._show("Forgot Password","Sign up Succesfull")




#----------------------------------------------------------------------------------------------------------#


class Order:

    def __init__(self):
        self.meal1 = 0
    def ordernow_indfood(self):
        self.meal1.set("Hello")




#function for retrive the data from database and login
def login_click():
    try:
        login_email = cus_name.get()
        login_pw = cus_password.get()
        con = pymysql.connect(host="localhost", user="root", password="root123", database="food_order")
        cur = con.cursor()
        cur.execute(f"select * from customer ")
        data = cur.fetchall()
        for name,email,mobile,password in data:
            if email == login_email and password == login_pw:
                order()
        con.close()
    except Exception as e:
        print(e)
        return login_email



#----------------------------------------------------------------------------------------------------------#

#signup window function

def signup_click():
    root.destroy()
    cus = Customers()
    signuppage = Tk()
    signuppage.title("Sign Up Window")
    signuppage.geometry("600x500+400+50")
    signuppage.config(bg = "purple")

    lbl_signupinfo = Label(signuppage,text = "SIGN UP",font = ("TIMES NEW ROMAN",30,"bold"),fg = "yellow",bg = "purple")
    lbl_signupinfo.place(x = 200,y = 30)
    lblname = Label(signuppage,text = "Name: ",font = ("TIMES NEW ROMAN",20),bg = "purple",fg = "white")
    lblname.place(x = 60,y = 100)
    cus.name = StringVar()
    entrname = Entry(signuppage,textvariable = cus.name,font = ("TIMES NEW ROMAN",20))
    entrname.place(x = 230,y = 100)
    lblemail = Label(signuppage, text="Email:", font=("TIMES NEW ROMAN", 20),bg = "purple",fg = "white")
    lblemail.place(x=60, y=150)
    cus.email = StringVar()
    entremail = Entry(signuppage, font=("TIMES NEW ROMAN", 20),textvariable = cus.email)
    entremail.place(x=230, y=150)
    lblmobile = Label(signuppage, text="Mobile:  ", font=("TIMES NEW ROMAN", 20),bg = "purple",fg = "white")
    lblmobile.place(x=60, y=200)
    cus.mobile = StringVar()
    entrmobile = Entry(signuppage, font=("TIMES NEW ROMAN", 20),textvariable = cus.mobile)
    entrmobile.place(x=230, y=200)
    lblnewpassword = Label(signuppage, text="Password:   ", font=("TIMES NEW ROMAN", 20),bg = "purple",fg = "white")
    lblnewpassword.place(x=60, y=250)
    cus.password = StringVar()
    entrnewpassword = Entry(signuppage, font=("TIMES NEW ROMAN", 20),show = "*",textvariable = cus.password)
    entrnewpassword.place(x=230, y=250)
    lblre_newpassword = Label(signuppage, text="Re-Enter:  ", font=("TIMES NEW ROMAN", 20),bg = "purple",fg = "white")
    lblre_newpassword.place(x=60, y=300)
    cus.repassword = StringVar()
    entre_newpassword = Entry(signuppage, font=("TIMES NEW ROMAN", 20),show = "*",textvariable = cus.repassword)
    entre_newpassword.place(x=230, y=300)
    btn_pass = Button(signuppage,text = "Sign Up",font=("TIMES NEW ROMAN", 20),width = 15,bg = "yellow",command = cus.signup_succesfull_click)
    btn_pass.place(x=200, y=350)

    signuppage.mainloop()



#----------------------------------------------------------------------------------------------------------#
#forgot password window function

def forgot_click():
    root.destroy()
    f_cus = Customers()
    forgotpage = Tk()
    forgotpage.title("RESET PASSWORD WINDOW")
    forgotpage.geometry("600x500+400+50")
    forgotpage.config(bg="pink")
    lbl_forgotinfo = Label(forgotpage, text="FORGOT PASSWORD", font=("TIMES NEW ROMAN", 30, "bold"), fg="red",
                           bg="pink").place(x=100, y=20)
    lblname = Label(forgotpage, text="Name: ", font=("TIMES NEW ROMAN", 20), bg="pink", fg="brown").place(x=60, y=100)
    f_cus.update_name = StringVar()
    entrname = Entry(forgotpage, font=("TIMES NEW ROMAN", 20),textvariable = f_cus.update_name).place(x=230, y=100)
    lblemail = Label(forgotpage, text="Email:", font=("TIMES NEW ROMAN", 20), bg="pink", fg="brown").place(x=60,
                                                                                                             y=150)
    f_cus.update_email = StringVar()
    entremail = Entry(forgotpage, font=("TIMES NEW ROMAN", 20),textvariable = f_cus.update_email).place(x=230, y=150)
    lblmobile = Label(forgotpage, text="Mobile:  ", font=("TIMES NEW ROMAN", 20), bg="pink", fg="brown").place(x=60,
                                                                                                                 y=200)
    f_cus.update_mobile = StringVar()
    entrmobile = Entry(forgotpage, font=("TIMES NEW ROMAN", 20),textvariable = f_cus.update_mobile).place(x=230, y=200)
    lblnewpassword = Label(forgotpage, text="New Password:   ", font=("TIMES NEW ROMAN", 20), bg="pink",
                           fg="brown").place(x=60, y=250)
    f_cus.update_password = StringVar()
    entrnewpassword = Entry(forgotpage, font=("TIMES NEW ROMAN", 20),show = "*",textvariable = f_cus.update_password).place(x=230, y=250)
    lblre_newpassword = Label(forgotpage, text="Re-Enter:  ", font=("TIMES NEW ROMAN", 20), bg="pink",
                              fg="brown").place(x=60, y=300)
    f_cus.update_repassword = StringVar()
    entre_newpassword = Entry(forgotpage, font=("TIMES NEW ROMAN", 20),show = "*",textvariable = f_cus.update_repassword).place(x=230, y=300)
    btn_pass = Button(forgotpage, text="Submit", font=("TIMES NEW ROMAN", 20), width=15, bg="blue",fg = "white",command = f_cus.forgot_password_succesful_click).place(x=200,
                                                                                                             y=350)

    forgotpage.mainloop()

#----------------------------------------------------------------------------------------------------------#

#indian food price list

def ind_pricelist():
    rootIPL = Tk()
    rootIPL.geometry("400x600+50+20")
    rootIPL.title("Price List")
    rootIPL.config(bg = "#000080")
    lbl_inditem = Label(rootIPL,text = "Item",font = ("sans-serif", 20, "bold"),bg ="#000080" ).place(x = 10,y = 0)
    lbl_inditemPrice = Label(rootIPL,text = "Price(Rs.)",font = ("sans-serif", 20, "bold"),bg ="#000080").place(x = 250,y = 0)
    lbl_inditem1 = Label(rootIPL,text = "Chicken Biryani",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white" ).place(x = 10,y = 40)
    lbl_inditemPrice1 = Label(rootIPL,text = "400",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white").place(x = 250,y = 40)
    lbl_inditem2 = Label(rootIPL,text = "Chicken Pulao",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white" ).place(x = 10,y = 80)
    lbl_inditemPrice2 = Label(rootIPL,text = "300",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white").place(x = 250,y = 80)
    lbl_inditem3 = Label(rootIPL,text = "Chicken Curry",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white" ).place(x = 10,y = 120)
    lbl_inditemPrice3 = Label(rootIPL,text = "300",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white").place(x = 250,y = 120)
    lbl_inditem4 = Label(rootIPL,text = "Chicken Daal",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white" ).place(x = 10,y = 160)
    lbl_inditemPrice4 = Label(rootIPL,text = "400",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white").place(x = 250,y = 160)
    lbl_inditem5 = Label(rootIPL,text = "Checken Palak",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white" ).place(x = 10,y = 200)
    lbl_inditemPrice5 = Label(rootIPL,text = "350",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white").place(x = 250,y = 200)
    lbl_inditem6 = Label(rootIPL,text = "Alu Palak",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white" ).place(x = 10,y = 240)
    lbl_inditemPrice6 = Label(rootIPL,text = "250",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white").place(x = 250,y = 240)
    lbl_inditem7 = Label(rootIPL,text = "Daal Palak",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white" ).place(x = 10,y = 280)
    lbl_inditemPrice7 = Label(rootIPL,text = "500",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white").place(x = 250,y = 280)
    lbl_inditem8 = Label(rootIPL,text = "Daal Tarka",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white" ).place(x = 10,y = 320)
    lbl_inditemPrice8 = Label(rootIPL,text = "150",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white").place(x = 250,y = 320)
    lbl_inditem9 = Label(rootIPL,text = "Mix Vagitable",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white" ).place(x = 10,y = 360)
    lbl_inditemPrice9 = Label(rootIPL,text = "200",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white").place(x = 250,y = 360)
    lbl_inditem10 = Label(rootIPL,text = "Seek Kebab",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white" ).place(x = 10,y = 400)
    lbl_inditemPrice10 = Label(rootIPL,text = "600",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white").place(x = 250,y = 400)
    lbl_inditem11 = Label(rootIPL,text = "Samosa",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white" ).place(x = 10,y = 440)
    lbl_inditemPrice11 = Label(rootIPL,text = "20",font = ("sans-serif", 20, "bold"),bg ="#000080",fg = "white").place(x = 250,y = 440)

    rootIPL.mainloop()


#----------------------------------------------------------------------------------------------------------#


#western food price list

def western_pricelist():
    rootIPL = Tk()
    rootIPL.geometry("400x600+50+20")
    rootIPL.title("Price List")
    rootIPL.config(bg = "#D8BFD8")
    lbl_inditem = Label(rootIPL,text = "Item",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8" ).place(x = 10,y = 0)
    lbl_inditemPrice = Label(rootIPL,text = "Price(Rs.)",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8").place(x = 250,y = 0)
    lbl_inditem1 = Label(rootIPL,text = "Garlic Bread",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 40)
    lbl_inditemPrice1 = Label(rootIPL,text = "400",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 40)
    lbl_inditem2 = Label(rootIPL,text = "Pancakes",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 80)
    lbl_inditemPrice2 = Label(rootIPL,text = "300",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 80)
    lbl_inditem3 = Label(rootIPL,text = "Pizza",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 120)
    lbl_inditemPrice3 = Label(rootIPL,text = "300",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 120)
    lbl_inditem4 = Label(rootIPL,text = "Doughnut",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 160)
    lbl_inditemPrice4 = Label(rootIPL,text = "400",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 160)
    lbl_inditem5 = Label(rootIPL,text = "Fried Chicken",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 200)
    lbl_inditemPrice5 = Label(rootIPL,text = "350",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 200)
    lbl_inditem6 = Label(rootIPL,text = "Waffles",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 240)
    lbl_inditemPrice6 = Label(rootIPL,text = "250",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 240)
    lbl_inditem7 = Label(rootIPL,text = "Pasta",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 280)
    lbl_inditemPrice7 = Label(rootIPL,text = "500",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 280)
    lbl_inditem8 = Label(rootIPL,text = "Burrito",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 320)
    lbl_inditemPrice8 = Label(rootIPL,text = "150",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 320)
    lbl_inditem9 = Label(rootIPL,text = "Chicken Fingers",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 360)
    lbl_inditemPrice9 = Label(rootIPL,text = "200",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 360)
    lbl_inditem10 = Label(rootIPL,text = "Cheesecake",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 400)
    lbl_inditemPrice10 = Label(rootIPL,text = "600",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 400)
    lbl_inditem11 = Label(rootIPL,text = "Tacos",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 440)
    lbl_inditemPrice11 = Label(rootIPL,text = "20",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 440)

    rootIPL.mainloop()


#----------------------------------------------------------------------------------------------------------#


#Chineese food price list

def chineese_pricelist():
    rootIPL = Tk()
    rootIPL.geometry("400x600+50+20")
    rootIPL.title("Price List")
    rootIPL.config(bg = "#D8BFD8")
    lbl_inditem = Label(rootIPL,text = "Item",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8" ).place(x = 10,y = 0)
    lbl_inditemPrice = Label(rootIPL,text = "Price(Rs.)",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8").place(x = 250,y = 0)
    lbl_inditem1 = Label(rootIPL,text = "Kung Pao Chicken",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 40)
    lbl_inditemPrice1 = Label(rootIPL,text = "400",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 40)
    lbl_inditem2 = Label(rootIPL,text = "Sweet and Sour Pork",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 80)
    lbl_inditemPrice2 = Label(rootIPL,text = "300",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 80)
    lbl_inditem3 = Label(rootIPL,text = "Peking Roast Duck",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 120)
    lbl_inditemPrice3 = Label(rootIPL,text = "300",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 120)
    lbl_inditem4 = Label(rootIPL,text = "Mapo Tofu",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 160)
    lbl_inditemPrice4 = Label(rootIPL,text = "400",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 160)
    lbl_inditem5 = Label(rootIPL,text = "Chow Mein",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 200)
    lbl_inditemPrice5 = Label(rootIPL,text = "350",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 200)
    lbl_inditem6 = Label(rootIPL,text = "Chinese Hot Pot",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 240)
    lbl_inditemPrice6 = Label(rootIPL,text = "250",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 240)
    lbl_inditem7 = Label(rootIPL,text = "Spring Rolls",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 280)
    lbl_inditemPrice7 = Label(rootIPL,text = "500",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 280)
    lbl_inditem8 = Label(rootIPL,text = "Wonton Soup",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 320)
    lbl_inditemPrice8 = Label(rootIPL,text = "150",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 320)
    lbl_inditem9 = Label(rootIPL,text = "Chicken Fried Rice",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 360)
    lbl_inditemPrice9 = Label(rootIPL,text = "200",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 360)
    lbl_inditem10 = Label(rootIPL,text = "Char Siu",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white" ).place(x = 10,y = 400)
    lbl_inditemPrice10 = Label(rootIPL,text = "600",font = ("sans-serif", 20, "bold"),bg ="#D8BFD8",fg = "white").place(x = 250,y = 400)

    rootIPL.mainloop()



#----------------------------------------------------------------------------------------------------------#



#order button click



















#----------------------------------------------------------------------------------------------------------#


#food order window

# Indian Food Window
# ----------------------------------------------------------------------------------------------------------

def indian_food_list():

    ord = Order()
    ind_root = Tk()
    ind_root.title("Indian Food")
    width = ind_root.winfo_screenwidth()
    height = ind_root.winfo_screenheight()
    ind_root.geometry("%dx%d" % (width, height))
    ind_root.config(bg="#FFFDD0")

    lbl_orderinfo = Label(ind_root, text="INDIAN FOOD", font=("algerian", 50, "bold"), bg="#FFFDD0",
                          fg="blue").pack()

    lbl_orderitnem1 = Label(ind_root, text="Meal", font=("sans-serif", 25, "bold"), bg="#FFFDD0").place(x=50, y=150)
    lbl_orderquantity1 = Label(ind_root, text="Quantity", font=("sans-serif", 25, "bold"), bg="#FFFDD0").place(x=350,
                                                                                                               y=150)

    lbl_meal1 = Label(ind_root, text="Chicken Biryani", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=50,
                                                                                                             y=200)
    ord.meal1 = StringVar()
    ent_meal1 = Entry(ind_root, font=("sans-serif", 20, "bold"),textvariable = ord.meal1).place(x=350, y=200)

    lbl_meal2 = Label(ind_root, text="Chicken Pulao", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=50,
                                                                                                             y=250)
    ent_meal2 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=350, y=250)

    lbl_meal3 = Label(ind_root, text="Chicken Curry", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=50,
                                                                                                             y=300)
    ent_meal3 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=350, y=300)

    lbl_meal4 = Label(ind_root, text="Chicken Daal", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=50,
                                                                                                             y=350)
    ent_meal4 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=350, y=350)

    lbl_meal5 = Label(ind_root, text="Checken Palak", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=50,
                                                                                                             y=400)
    ent_meal5 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=350, y=400)

    lbl_meal6 = Label(ind_root, text="Alu Palak", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=50,
                                                                                                             y=450)
    ent_meal6 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=350, y=450)

    lbl_orderitnem2 = Label(ind_root, text="Meal", font=("sans-serif", 25, "bold"), bg="#FFFDD0").place(x=700, y=150)
    lbl_orderquantity2 = Label(ind_root, text="Quantity", font=("sans-serif", 25, "bold"), bg="#FFFDD0").place(x=1000,
                                                                                                               y=150)

    lbl_meal7 = Label(ind_root, text="Daal Palak", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=700,
                                                                                                             y=200)
    ent_meal7 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=1000, y=200)

    lbl_meal8 = Label(ind_root, text="Daal Tarka", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=700,
                                                                                                             y=250)
    ent_meal8 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=1000, y=250)

    lbl_meal9 = Label(ind_root, text="Mix Vagitable", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=700,
                                                                                                             y=300)
    ent_meal9 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=1000, y=300)

    lbl_meal10 = Label(ind_root, text="Seek Kebab", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=700,
                                                                                                              y=350)
    ent_meal10 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=1000, y=350)

    lbl_meal11 = Label(ind_root, text="Samosa", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=700,
                                                                                                              y=400)
    ent_meal11 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=1000, y=400)

    btn_pricelist = Button(ind_root, text="Price List", font=("sans-serif", 20, "bold"),bg = "red",fg = "white", command=ind_pricelist).place(
        x=500, y=550)

    btn_ordernow = Button(ind_root, text="Order Now", font=("sans-serif", 20, "bold"),bg = "blue",fg = "white",command = ord.ordernow_indfood).place(x=700, y=550)
    ind_root.mainloop()




# --------------------------------------------------------------------------------------------------
# Western Food Window

def western_food_list():

    ord = Order()
    ind_root = Tk()
    ind_root.title("Indian Food")
    width = ind_root.winfo_screenwidth()
    height = ind_root.winfo_screenheight()
    ind_root.geometry("%dx%d" % (width, height))
    ind_root.config(bg="#FF00FF")

    lbl_orderinfo = Label(ind_root, text="WESTERN FOOD", font=("algerian", 50, "bold"), bg="#FF00FF",
                          fg="blue").pack()

    lbl_orderitnem1 = Label(ind_root, text="Meal", font=("sans-serif", 25, "bold"), bg="#FF00FF").place(x=50, y=150)
    lbl_orderquantity1 = Label(ind_root, text="Quantity", font=("sans-serif", 25, "bold"), bg="#FF00FF").place(x=350,
                                                                                                               y=150)

    lbl_meal1 = Label(ind_root, text="Garlic Bread", font=("sans-serif", 20, "bold"), bg="#FF00FF").place(x=50,
                                                                                                             y=200)
    ord.meal1 = StringVar()
    ent_meal1 = Entry(ind_root, font=("sans-serif", 20, "bold"),textvariable = ord.meal1).place(x=350, y=200)

    lbl_meal2 = Label(ind_root, text="Pancakes", font=("sans-serif", 20, "bold"), bg="#FF00FF").place(x=50,
                                                                                                             y=250)
    ent_meal2 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=350, y=250)

    lbl_meal3 = Label(ind_root, text="Pizza", font=("sans-serif", 20, "bold"), bg="#FF00FF").place(x=50,
                                                                                                             y=300)
    ent_meal3 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=350, y=300)

    lbl_meal4 = Label(ind_root, text="Doughnut", font=("sans-serif", 20, "bold"), bg="#FF00FF").place(x=50,
                                                                                                             y=350)
    ent_meal4 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=350, y=350)

    lbl_meal5 = Label(ind_root, text="Fried Chicken", font=("sans-serif", 20, "bold"), bg="#FF00FF").place(x=50,
                                                                                                             y=400)
    ent_meal5 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=350, y=400)

    lbl_meal6 = Label(ind_root, text="Waffles", font=("sans-serif", 20, "bold"), bg="#FF00FF").place(x=50,
                                                                                                             y=450)
    ent_meal6 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=350, y=450)

    lbl_orderitnem2 = Label(ind_root, text="Meal", font=("sans-serif", 25, "bold"), bg="#FF00FF").place(x=700, y=150)
    lbl_orderquantity2 = Label(ind_root, text="Quantity", font=("sans-serif", 25, "bold"), bg="#FF00FF").place(x=1000,
                                                                                                               y=150)

    lbl_meal7 = Label(ind_root, text="Pasta", font=("sans-serif", 20, "bold"), bg="#FF00FF").place(x=700,
                                                                                                             y=200)
    ent_meal7 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=1000, y=200)

    lbl_meal8 = Label(ind_root, text="Burrito", font=("sans-serif", 20, "bold"), bg="#FF00FF").place(x=700,
                                                                                                             y=250)
    ent_meal8 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=1000, y=250)

    lbl_meal9 = Label(ind_root, text="Chicken Fingers", font=("sans-serif", 20, "bold"), bg="#FF00FF").place(x=700,
                                                                                                             y=300)
    ent_meal9 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=1000, y=300)

    lbl_meal10 = Label(ind_root, text="Cheesecake", font=("sans-serif", 20, "bold"), bg="#FF00FF").place(x=700,
                                                                                                              y=350)
    ent_meal10 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=1000, y=350)

    lbl_meal11 = Label(ind_root, text="Tacos", font=("sans-serif", 20, "bold"), bg="#FF00FF").place(x=700,
                                                                                                              y=400)
    ent_meal11 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=1000, y=400)

    btn_pricelist = Button(ind_root, text="Price List", font=("sans-serif", 20, "bold"),bg = "red",fg = "white", command=western_pricelist).place(
        x=500, y=550)

    btn_ordernow = Button(ind_root, text="Order Now", font=("sans-serif", 20, "bold"),bg = "blue",fg = "white",command = ord.ordernow_indfood).place(x=700, y=550)
    ind_root.mainloop()


# --------------------------------------------------------------------------------------------------
# Chineese Food Window

def chineese_food_list():

    ord = Order()
    ind_root = Tk()
    ind_root.title("Indian Food")
    width = ind_root.winfo_screenwidth()
    height = ind_root.winfo_screenheight()
    ind_root.geometry("%dx%d" % (width, height))
    ind_root.config(bg="#FFFDD0")

    lbl_orderinfo = Label(ind_root, text="CHINESE FOOD", font=("algerian", 50, "bold"), bg="#FFFDD0",
                          fg="blue").pack()

    lbl_orderitnem1 = Label(ind_root, text="Meal", font=("sans-serif", 25, "bold"), bg="#FFFDD0").place(x=50, y=150)
    lbl_orderquantity1 = Label(ind_root, text="Quantity", font=("sans-serif", 25, "bold"), bg="#FFFDD0").place(x=350,
                                                                                                               y=150)

    lbl_meal1 = Label(ind_root, text="Kung Pao Chicken", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=50,
                                                                                                             y=200)
    ord.meal1 = StringVar()
    ent_meal1 = Entry(ind_root, font=("sans-serif", 20, "bold"),textvariable = ord.meal1).place(x=350, y=200)

    lbl_meal2 = Label(ind_root, text="Sweet and Sour Pork", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=50,
                                                                                                             y=250)
    ent_meal2 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=350, y=250)

    lbl_meal3 = Label(ind_root, text="Peking Roast Duck", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=50,
                                                                                                             y=300)
    ent_meal3 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=350, y=300)

    lbl_meal4 = Label(ind_root, text="Mapo Tofu", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=50,
                                                                                                             y=350)
    ent_meal4 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=350, y=350)

    lbl_meal5 = Label(ind_root, text="Chow Mein", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=50,
                                                                                                             y=400)
    ent_meal5 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=350, y=400)



    lbl_orderitnem2 = Label(ind_root, text="Meal", font=("sans-serif", 25, "bold"), bg="#FFFDD0").place(x=700, y=150)
    lbl_orderquantity2 = Label(ind_root, text="Quantity", font=("sans-serif", 25, "bold"), bg="#FFFDD0").place(x=1000,
                                                                                                               y=150)

    lbl_meal7 = Label(ind_root, text="Chinese Hot Pot", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=700,
                                                                                                             y=200)
    ent_meal7 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=1000, y=200)

    lbl_meal8 = Label(ind_root, text="Spring Rolls", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=700,
                                                                                                             y=250)
    ent_meal8 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=1000, y=250)

    lbl_meal9 = Label(ind_root, text="Wonton Soup", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=700,
                                                                                                             y=300)
    ent_meal9 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=1000, y=300)

    lbl_meal10 = Label(ind_root, text="Chicken Fried Rice", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=700,
                                                                                                              y=350)
    ent_meal10 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=1000, y=350)

    lbl_meal11 = Label(ind_root, text="Char Siu", font=("sans-serif", 20, "bold"), bg="#FFFDD0").place(x=700,
                                                                                                              y=400)
    ent_meal11 = Entry(ind_root, font=("sans-serif", 20, "bold")).place(x=1000, y=400)

    btn_pricelist = Button(ind_root, text="Price List", font=("sans-serif", 20, "bold"),bg = "red",fg = "white", command=chineese_pricelist).place(
        x=500, y=550)

    btn_ordernow = Button(ind_root, text="Order Now", font=("sans-serif", 20, "bold"),bg = "blue",fg = "white",command = ord.ordernow_indfood).place(x=700, y=550)
    ind_root.mainloop()








#----------------------------------------------------------------------------------------------------------#
#order Window

def order():
    root.destroy()

    order_root = Tk()
    order_root.geometry("1200x600+80+50")
    order_root.title("Order Window")
    order_root.config(bg="#FFFDD0")
    lbl_info = Label(order_root, text="WELCOME TO FOOD HUB", font=("algerian", 50, "bold"), bg="#FFFDD0",
                     fg="red").pack()

    image1 = Image.open('indianfood.jpg')
    rimg1 = image1.resize((350, 300))
    photo1 = ImageTk.PhotoImage(rimg1)

    image2 = Image.open('westernfood.jpg')
    rimg2 = image2.resize((350, 300))
    photo2 = ImageTk.PhotoImage(rimg2)

    image3 = Image.open('chineesfood.jpg')
    rimg3 = image3.resize((350, 300))
    photo3 = ImageTk.PhotoImage(rimg3)

    btn1 = Button(order_root, image=photo1,command = indian_food_list).place(x=50, y=130)
    btn2 = Button(order_root, image=photo2,command = western_food_list).place(x=420, y=130)
    btn3 = Button(order_root, image=photo3,command = chineese_food_list).place(x=790, y=130)

    lbl_indianfood = Label(order_root, text="Indian Food", font=("sans-serif", 25, "bold"), bg="#FFFDD0", fg="red")
    lbl_indianfood.place(x=100, y=440)

    lbl_westernfood = Label(order_root, text="Western Food", font=("sans-serif", 25, "bold"), bg="#FFFDD0", fg="red")
    lbl_westernfood.place(x=470, y=440)

    lbl_chineesfood = Label(order_root, text="Chinese Food", font=("sans-serif", 25, "bold"), bg="#FFFDD0", fg="red")
    lbl_chineesfood.place(x=840, y=440)

    order_root.mainloop()



#----------------------------------------------------------------------------------------------------------#


#main window root for login

root = Tk("Log In Window")
root.title("FOOD ORDER")
root.geometry("1000x600+180+50")
root.config(bg = "yellow")

lbl_info = Label(root,text = "LOGIN HERE",font = ("algerian",40,"bold"),fg = "blue",bg = "yellow")
lbl_info.place(x = 400,y = 60)
lbl_username = Label(root,text = "Email Id : ",font = ("TIMES NEW ROMAN",20,"bold"),bg = "yellow")
lbl_username.place(x = 300,y = 150)
cus_name = StringVar()
entr_username = Entry(root,font = ("TIMES NEW ROMAN",20),textvariable = cus_name)
entr_username.place(x = 500,y = 150)
lbl_password = Label(root,text = "Password : ",font = ("TIMES NEW ROMAN",20,"bold"),bg = "yellow")
lbl_password.place(x = 300,y = 230)
cus_password = StringVar()
entr_password = Entry(root,font = ("TIMES NEW ROMAN",20),show = "*",textvariable = cus_password)
entr_password.place(x = 500,y = 230)
btn_login = Button(text = "Sign In",font = ("TIMES NEW ROMAN",20,"bold"),width = 10,bg = "red",fg = "white",command = login_click).place(x = 450,y = 300)
btn_forgot = Button(text = "Forgot Password",font = ("TIMES NEW ROMAN",15,"bold"),width = 15,bg = "blue",fg = "white",command = forgot_click).place(x = 500,y = 380)
btn_signup = Button(text = "Sign Up",font = ("TIMES NEW ROMAN",15,"bold"),width = 10,bg = "blue",fg = "white",command = signup_click).place(x = 350,y = 380)




root.mainloop()