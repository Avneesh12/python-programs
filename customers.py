
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



