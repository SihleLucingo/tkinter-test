from tkinter import *
from tkinter import ttk
from unittest import result

root = Tk()


def add():
    global count
    for i in tree_table.get_children():
        tree_table.delete(i)

    get_name = txt_name.get()
    get_ref = txt_ref.get()
    get_age = txt_age.get()
    get_email = txt_email.get()
    data_list.append((get_name, get_ref, get_age, get_email))

    for result in data_list:
        tree_table.insert(parent='', index='end', iid=count, text="", values=(result),tag="row")
    txt_name.delete(0, END)
    txt_ref.delete(0, END)
    txt_age.delete(0, END)
    txt_email.delete(0, END)
    print(data_list)


tree_table = ttk.Treeview(root)
global count
count = 0

data_list = []
tree_table['columns'] = ("Serial_Number", "Condition", "Users", "Email Address")

tree_table.column("#0", width=30)
tree_table.column("Serial_Number", width=120, anchor=W)
tree_table.column("Condition", width=120, anchor=W)
tree_table.column("Users", width=120, anchor=W)
tree_table.column("Email Address", width=120, anchor=W)

headings = ["#0", "Serial_Number", "Condition", "Users", "Email Address"]
txt_headings = ["No.", "Serial_Number", "Condition", "Users", "Problem"]
for i in range(len(headings)):
    tree_table.heading(headings[i], text=txt_headings[i], anchor=W)


txt_name = Entry(root, width=20)
txt_name.pack()
txt_ref = Entry(root, width=20)
txt_ref.pack()
txt_age = Entry(root, width=20)
txt_age.pack()
txt_email = Entry(root, width=20)
txt_email.pack()
btn_enter = Button(root, text="Add", width=20, command=add)
btn_enter.pack()

tree_table.pack()
root.mainloop() 