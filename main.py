from tkinter import *
import pymysql

root = Tk()
root.geometry('500x500')
root.title("Sample Form")

Lastname = StringVar()
Firstname = StringVar()
Middlename = StringVar()
Positions = StringVar()

def database():
    lastname = Lastname.get()
    firstname = Firstname.get()
    middlename = Middlename.get()
    positions = Positions.get()
    conn = pymysql.connect(host="localhost", user="root", password="", db="testgodb")
    with conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO players(lname, fname, mname, position) VALUES(%s, %s, %s, %s)', (lastname, firstname, middlename, positions))
        conn.commit()


label_0 = Label(root, text="Sample form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="LastName", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=Lastname)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="FirstName", width=20, font=("bold", 10))
label_2.place(x=68, y=170)

entry_2 = Entry(root, textvar=Firstname)
entry_2.place(x=240, y=170)

label_3 = Label(root, text="MiddleName", width=20, font=("bold", 10))
label_3.place(x=68, y=210)

entry_3 = Entry(root, textvar=Middlename)
entry_3.place(x=240, y=210)

#label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
#label_3.place(x=70, y=230)

#var = IntVar()
#Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
#Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)

label_4 = Label(root, text="Positions", width=20, font=("bold", 10))
label_4.place(x=70, y=250)

list1 = ['Accounting', 'HR', 'Service'];

droplist = OptionMenu(root, Positions, *list1)
droplist.config(width=14)
Positions.set('Select position')
droplist.place(x=235, y=250)

# label_4 = Label(root, text="Programming", width=20, font=("bold", 10))
# label_4.place(x=85, y=330)
# var1 = IntVar()
# Checkbutton(root, text="java", variable=var1).place(x=235, y=330)
# var2 = IntVar()
# Checkbutton(root, text="python", variable=var2).place(x=290, y=330)

Button(root, text="Submit", width=20, bg="brown", fg="white", command=database).place(x=180, y=310)

mainloop()
