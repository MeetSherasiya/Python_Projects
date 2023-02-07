from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("Login form")
window.geometry('1000x500+100+100')
window.configure(bg='#333333')

def login():
    username = "Meet"
    password = "123456"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    elif username_entry.get()=="" or password_entry.get()=="":
        messagebox.showerror(title="Error", message="All Fileds are requiered!")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = Frame(bg='#333333')

# Creating widgets
login_label = Label(frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = Entry(frame, font=("Arial", 16))
password_entry = Entry(frame, show="*", font=("Arial", 16))
password_label = Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = Button(frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()