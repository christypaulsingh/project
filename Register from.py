from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Register form")
window.geometry("500x500")

def submit():
    name=txtName.get()
    #messagebox.showinfo("Name",name)
    password=txtPass.get()
    email=txtEmail.get()
    phone=txtPhone.get()

    if name and name.isalpha():
        lbN=Label(window,font=("times",10,"bold"),fg="green",text="Validation Name")
        lbN.grid(row=2,column=2)
    else:
        lbN=Label(window,font=("times",10,"bold"),fg="red",text="Invalid name!")
        lbN.grid(row=2,column=2)

    if password and password.isalnum() and len(password)==8:
        lbP=Label(window,font=("times",10,"bold"),fg="green",text="Validation Password")
        lbP.grid(row=4,column=2)

    else:
        lbP = Label(window, font=("times", 10, "bold"), fg="red", text="Invalid Password!")
        lbP.grid(row=4,column=2)

    if email and email.endswith("@gmail.com"):
        lbE = Label(window, font=("times", 10, "bold"), fg="green", text="Validation Email address")
        lbE.grid(row=6,column=2)

    else:
        lbE = Label(window, font=("times", 10, "bold"), fg="red", text="Invalid Email address!")
        lbE.grid(row=6,column=2)

    if phone and len(phone)==10:
        lbPH = Label(window, font=("times", 10, "bold"), fg="green", text="Validation Phone number")
        lbPH.grid(row=8,column=2)

    else:
        lbN = Label(window, font=("times", 10, "bold"), fg="red", text="Invalid Phone number!")
        lbN.grid(row=8,column=2)










lbTitle=Label(window,text="Registration form",font=("Times",14,"bold"),fg="Red",pady=10)
lbTitle.grid(row=0,column=2)

lblName=Label(window,text="Name",font=("times",13,"bold"),pady=10)
lblName.grid(row=1,column=1)

name=StringVar

txtName=Entry(window,font=("times",14,"bold"),textvariable=name)
txtName.grid(row=1,column=2)

lblPass=Label(window,text="Password",font=("times",13,"bold"),pady=10)
lblPass.grid(row=3,column=1)

passw=StringVar

txtPass=Entry(window,font=("times",14,"bold"),textvariable=passw)
txtPass.grid(row=3,column=2)

lblEmail=Label(window,text="Email",font=("times",13,"bold"),pady=10)
lblEmail.grid(row=5,column=1)

email=StringVar

txtEmail=Entry(window,font=("times",14,"bold"),textvariable=email)
txtEmail.grid(row=5,column=2)

lblPhone=Label(window,text="Mobile",font=("times",13,"bold"),pady=10)
lblPhone.grid(row=7,column=1)
phone=IntVar

txtPhone=Entry(window,font=("times",14,"bold"),textvariable=phone)
txtPhone.grid(row=7,column=2)

btnSub=Button(window,text="Submit",font=("times",13,"bold"),bg="red",fg="white",command=submit)
btnSub.grid(row=9,column=2)


window.mainloop()