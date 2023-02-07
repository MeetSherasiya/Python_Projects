from tkinter import *
from tkinter import messagebox
import base64

def decrypt():
    password = code.get()

    if password=="123456":
        screen1 = Toplevel(screen)
        screen1.title("Decryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#00bd56")

        image_icon = PhotoImage(file="Beginners_projects/Images/userman.png")
        screen1.iconphoto(False, image_icon)

        message = text1.get(1.0,END)
        decode_message = message.encode("ascii")
        base64_byte = base64.b64decode(decode_message)
        decrypt = base64_byte.decode("ascii")

        Label(screen1, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen1, font="Robote 14", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)

    elif password=="":
        messagebox.showerror("Decryption", "Input password!")

    elif password != "123456":
        messagebox.showerror("Decryption","Invalid Password")


def encrypt():
    password = code.get()

    if password=="123456":
        screen2 = Toplevel(screen)
        screen2.title("Encryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#ed3833")

        image_icon = PhotoImage(file="Beginners_projects/Images/userman.png")
        screen2.iconphoto(False, image_icon)

        message = text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_byte = base64.b64encode(encode_message)
        encrypt = base64_byte.decode("ascii")

        Label(screen2, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen2, font="Robote 14", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)

    elif password=="":
        messagebox.showerror("Encryption", "Input password!")

    elif password != "123456":
        messagebox.showerror("Encryption","Invalid Password")

def main_screen():

    global screen
    global code
    global text1
    
    screen = Tk()
    screen.geometry("375x398")
    screen.configure(bg='#333333')

    #icon
    image_icon = PhotoImage(file="Beginners_projects/Images/userman.png")
    screen.iconphoto(False, image_icon)
    screen.title("Encrypt & Decrypt App")

    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(text="Enter text for encryption and decryption", fg="black", font=("calbri",13)).place(x=10,y=10)
    text1 = Text(font="Robote 14", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=40, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri",13)).place(x=10, y=150)
    code= StringVar()
    Entry(textvariable=code, width=19,bd=0, font=("arial",25), show="*").place(x=10, y=183)

    Button(text="ENCRYPT", height="2", width="23", bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width="23", bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width="50", bg="#1089ff", fg="White", bd=0, command=reset).place(x=10, y=300)


    screen.mainloop()

main_screen()