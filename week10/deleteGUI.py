# pip install tk
import sys
# Import Library
from tkinter import Tk # Window
from tkinter import Label # Label
from tkinter import Entry # Text Box
from tkinter import Button # Button
from cusInfo import Libs
from notebookmanager import *

def close():
    sys.exit()


def search720():
    # reading value from entry and send to library/middleware
    cid = txtNID.get()  #Read value from textbox

    #send value to search (Middleware)
    record = search(cid)

    #Display message
    if record==None:
        print("Record not found")

    else:
        print(record)
        txtPages.delete(0, len(txtPages.get()))
        txtPages.insert(0, record[1])

def editcopy():
    # reading value from entry and send to library/middleware
    cid = int(txtNID.get())  #Read value from textbox
    pages=txtPages.get()
    price=txtPrice.get()
    email=txtemail.get()
    password=txtPass.get()

    cust=Libs(cid, pages, price, email, password)
    result=edit(cust)
    if result==True:
        lblmessage['text']="Edit Record"

    else:
        lblmessage['text']="Error"


# Decalre and initialize
window = Tk() # Declare window
window.geometry("450x450")
window.resizable(False, False)
window.title("Insert New Record")

lblNID = Label(window, text="ID: ")
lblPages = Label(window, text="Name: ")
lblPrice = Label(window, text="Dob: ")
lblemail=Label(window, text="Email")
Password = Label(window, text="Password: ")

txtNID = Entry(window, width=20)
txtPages = Entry(window, width=20)
txtPrice = Entry(window, width=20)
txtemail = Entry(window, width=20)
txtPass = Entry(window, width=20)

btnSave = Button(window, text="Edit", command=editcopy) # calling save function
btnsearch = Button(window, text="Search", command=search720)
btnClose=Button(window, text="CLOSE", command=close)

lblNID.place(x=20, y=10)
txtNID.place(x=100, y=10)

lblPages.place(x=20, y=40)
txtPages.place(x=100, y=40)

lblPrice.place(x=20, y=70)
txtPrice.place(x=100, y=70)

lblemail.place(x=20, y=100)
txtemail.place(x=100, y=100)

Password.place(x=20, y=130)
txtPass.place(x=100, y=130)

lblmessage=Label(window, text="")
lblmessage.place(x=100, y=150)

btnSave.place(x=100, y=200)
btnsearch.place(x=150, y=250)
btnClose.place(x=150, y=200)

window.mainloop() # Display window


