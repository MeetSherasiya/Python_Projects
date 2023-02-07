from tkinter import *

root = Tk()
root.geometry("1050x500+100+100")
root.title("Bill Managment")
root.resizable(False,False)

def Reset():
    entry_dosa.delete(0,END)
    entry_cookies.delete(0,END)
    entry_tea.delete(0,END)
    entry_coffee.delete(0,END)
    entry_juice.delete(0,END)
    entry_pancakes.delete(0,END)
    entry_egg.delete(0,END)

def Total():
    try: a1 = int(dosa.get())
    except: a1 = 0

    try: a2 = int(cookies.get())
    except: a2 = 0

    try: a3 = int(tea.get())
    except: a3 =0

    try: a4 = int(coffee.get())
    except: a4 = 0

    try: a5 = int(juice.get())
    except: a5 = 0

    try: a6 = int(pancakes.get())
    except: a6 = 0

    try: a7 = int(egg.get())
    except: a7 = 0

    #********** Define cost of each item per quantity ***************

    c1 = 60 * a1
    c2 = 30 * a2
    c3 = 7 * a3
    c4 = 10 * a4
    c5 = 20 * a5
    c6 = 15 * a6
    c7 = 7 * a7

    entry_total = Entry(frame_bill, font=("aria", 20, "bold"), textvariable=Total_bill, bd=6, width=15, bg="lightgreen")
    entry_total.place(x=20, y=70)

    total_cost = c1+c2+c3+c4+c5+c6+c7
    string_bill = "Rs.", str('%.2f'%total_cost)
    Total_bill.set(string_bill)

    entry_write = Label(frame_bill, font=("Gabriola", 16, "bold"), text="Thank you for Purchasing!", bg="lightyellow")
    entry_write1 = Label(frame_bill, font=("Gabriola", 16, "bold"), text="Visit Again to our store", bg="lightyellow")
    entry_write.place(x=20, y=130)
    entry_write1.place(x=20, y=180)


Label(text="Bill Managment", bg="#dae6f6", fg="#364971", font=("poppins",33), width=300, height=2).pack()

#********* MENU CARD **************

frame_menu = Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=330, height=370)
frame_menu.place(x=10, y=118)

Label(frame_menu, text="Menu", font=("Gabriola",40,"bold"), fg="black", bg="lightgreen").place(x=80, y=0)

Label(frame_menu, font=("Lucida Calligraphy",15,"bold"), text="Dosa.........Rs.60/plate",fg="black",bg="lightgreen").place(x=10, y=80)
Label(frame_menu, font=("Lucida Calligraphy",15,"bold"), text="Cookis.........Rs.30/plate",fg="black",bg="lightgreen").place(x=10, y=110)
Label(frame_menu, font=("Lucida Calligraphy",15,"bold"), text="Tea.........Rs.7/cup",fg="black",bg="lightgreen").place(x=10, y=140)
Label(frame_menu, font=("Lucida Calligraphy",15,"bold"), text="Coffee.........Rs.10/cup",fg="black",bg="lightgreen").place(x=10, y=170)
Label(frame_menu, font=("Lucida Calligraphy",15,"bold"), text="Juice.........Rs.20/glass",fg="black",bg="lightgreen").place(x=10, y=200)
Label(frame_menu, font=("Lucida Calligraphy",15,"bold"), text="Pancakes.........Rs.15/pack",fg="black",bg="lightgreen").place(x=10, y=230)
Label(frame_menu, font=("Lucida Calligraphy",15,"bold"), text="Eggs.........Rs.7/egg",fg="black",bg="lightgreen").place(x=10, y=260)


#**********Bill *********

frame_bill = Frame(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=300, height=370)
frame_bill.place(x=730, y=118)

lbl_total = Label(frame_bill, font=("aria", 20, "bold"), text="Total Bill", width=18, fg="lightyellow", bg="black")
lbl_total.place(x=0, y=20)


#**********Entry Work ******************

frame_entry = Frame(root, bd=5, height=370, width=320, relief=RAISED)
frame_entry.pack()
frame_entry.place(x=350, y=115)

dosa = StringVar()
cookies = StringVar()
tea = StringVar()
coffee = StringVar()
juice = StringVar()
pancakes = StringVar()
egg = StringVar()
Total_bill = StringVar()


#********Label **********
lbl_dosa = Label(frame_entry, font=("aria", 20, "bold"), text="Dosa", width=12, fg="blue4")
lbl_cookies = Label(frame_entry, font=("aria", 20, "bold"), text="Cookies", width=12, fg="blue4")
lbl_tea = Label(frame_entry, font=("aria", 20, "bold"), text="Tea", width=12, fg="blue4")
lbl_coffee = Label(frame_entry, font=("aria", 20, "bold"), text="Coffee", width=12, fg="blue4")
lbl_juice = Label(frame_entry, font=("aria", 20, "bold"), text="Juice", width=12, fg="blue4")
lbl_pancakes = Label(frame_entry, font=("aria", 20, "bold"), text="Pancakes", width=12, fg="blue4")
lbl_egg = Label(frame_entry, font=("aria", 20, "bold"), text="Egg", width=12, fg="blue4")


lbl_dosa.grid(row=1,column=0)
lbl_cookies.grid(row=2,column=0)
lbl_tea.grid(row=3,column=0)
lbl_coffee.grid(row=4,column=0)
lbl_juice.grid(row=5,column=0)
lbl_pancakes.grid(row=6,column=0)
lbl_egg.grid(row=7,column=0)

#*********Entry ***********
entry_dosa = Entry(frame_entry, font=("aria", 20, "bold"), textvariable=dosa, bd=6, width=8, bg="lightpink")
entry_cookies = Entry(frame_entry, font=("aria", 20, "bold"), textvariable=cookies, bd=6, width=8, bg="lightpink")
entry_tea = Entry(frame_entry, font=("aria", 20, "bold"), textvariable=tea, bd=6, width=8, bg="lightpink")
entry_coffee = Entry(frame_entry, font=("aria", 20, "bold"), textvariable=coffee, bd=6, width=8, bg="lightpink")
entry_juice = Entry(frame_entry, font=("aria", 20, "bold"), textvariable=juice, bd=6, width=8, bg="lightpink")
entry_pancakes = Entry(frame_entry, font=("aria", 20, "bold"), textvariable=pancakes, bd=6, width=8, bg="lightpink")
entry_egg = Entry(frame_entry, font=("aria", 20, "bold"), textvariable=egg, bd=6, width=8, bg="lightpink")


entry_dosa.grid(row=1, column=1)
entry_cookies.grid(row=2, column=1)
entry_tea.grid(row=3, column=1)
entry_coffee.grid(row=4, column=1)
entry_juice.grid(row=5, column=1)
entry_pancakes.grid(row=6, column=1)
entry_egg.grid(row=7, column=1)


#*********Buttons ***************

btn_reset = Button(frame_entry, bd=5, fg="black", bg="lightblue", font=("arial", 16, "bold"), width=10, text="Reset", command=Reset)
btn_reset.grid(row=8, column=0)

btn_total = Button(frame_entry, bd=5, fg="black", bg="lightblue", font=("arial", 16, "bold"), width=10, text="Total", command=Total)
btn_total.grid(row=8, column=1)

root.mainloop()