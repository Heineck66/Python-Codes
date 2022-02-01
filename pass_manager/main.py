# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from os import read
from passgenerator import generate_password


def get_password():
    e_pass.delete(0, END)
    new_password = generate_password()
    e_pass.insert(0, string=new_password)
    window.clipboard_append(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
import json

def save_to_file():

    name = e_name.get()
    user = e_user.get()
    password = e_pass.get()
    new_data = { name: {
        'user': user,
        'password': password
    }}

    if (
        (name.isspace() or len(name) == 0)
        or (user.isspace() or len(user) == 0)
        or (password.isspace() or len(password) == 0)
    ):
        messagebox.showwarning("Oops", "Fields cannot be blank.")
    else:
        is_ok = messagebox.askyesnocancel(
            "Save",
            f"Do you want to save:\nname: {name}\nuser: {user}\npassword:{password}",
        )

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
                    print(data)
            except FileNotFoundError:
                with open("data.json", 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", 'w') as data_file:
                    json.dump(data, data_file, indent=4)


            e_name.delete(0, END)
            e_user.delete(0, END)
            e_pass.delete(0, END)


# ---------------------------- Find Password ------------------------------- #

def find_password(name):
    print(f'searching {name}... \n')
    try:
        with open('./data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning("Oops", "No Data file found.")
    else:
        if name in data:
            info_user = data[name]['user']
            info_pass = data[name]['password']
            messagebox.showwarning(f"{name}", f"\nApp: {name}\nUser: {info_user} \nPassword: {info_pass} \n(copied to clipboard)")
            window.clipboard_append(info_pass)
        else:
            messagebox.showwarning("Oops", "No details for name searched.")

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("PassManager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
logo = canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
l_name = Label(text="Name: ")
l_name.grid(column=0, row=1)

l_user = Label(text="Email/Username: ")
l_user.grid(column=0, row=2)

l_pass = Label(text="Password: ")
l_pass.grid(column=0, row=3)


# Entries
e_name = Entry(width=36)
e_name.grid(column=1, row=1)
e_name.focus()

e_user = Entry(width=55)
e_user.grid(column=1, row=2, columnspan=2)

e_pass = Entry(width=36)
e_pass.grid(column=1, row=3)


# Buttons
bnt_searchpass = Button(text="Search", width=15, command= lambda: find_password(e_name.get()))
bnt_searchpass.grid(column=2, row=1)

bnt_passgen = Button(text="Generate Password", command=get_password)
bnt_passgen.grid(column=2, row=3)

bnt_add = Button(text="Add", width=46, command=save_to_file)
bnt_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
