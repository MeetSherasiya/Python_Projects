from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")

    lbl_hr.config(text=hr)
    lbl_min.config(text=min)
    lbl_sec.config(text=sec)
    lbl_am.config(text=am)
    lbl_date.config(text=date)
    lbl_month.config(text=month)
    lbl_year.config(text=year)
    lbl_day.config(text=day)

    #*********** change time when open app ************
    lbl_hr.after(200,date_time)

root = Tk()
root.title("Digital Clock")
root.geometry("1000x500+100+100")
root.config(bg="black")
image_icon = PhotoImage(file="Beginners_projects/Digital_clock/logo.png")
root.iconphoto(False, image_icon)

clock = Frame(root, height=400, width=900, bg="black")
clock.place(x=50, y=50)

lbl_hr = Label(clock, font="arial 50 bold", bg="#00F1FF", fg="black")
lbl_hr.place(x=70, y=0, height=110, width=100)
lbl_hr_name = Label(clock,text="Hour", font="arial 30 bold", bg="#00F1FF", fg="black")
lbl_hr_name.place(x=70, y=120, height=45, width=100)

lbl_min = Label(clock, font="arial 50 bold", bg="#00F1FF", fg="black")
lbl_min.place(x=290, y=0, height=110, width=100)
lbl_min_name = Label(clock,text="Min", font="arial 32 bold", bg="#00F1FF", fg="black")
lbl_min_name.place(x=290, y=120, height=45, width=100)

lbl_sec = Label(clock, font="arial 50 bold", bg="#00F1FF", fg="black")
lbl_sec.place(x=510, y=0, height=110, width=100)
lbl_sec_name = Label(clock,text="Sec", font="arial 32 bold", bg="#00F1FF", fg="black")
lbl_sec_name.place(x=510, y=120, height=45, width=100)

lbl_am = Label(clock, font="arial 50 bold", bg="#00F1FF", fg="black")
lbl_am.place(x=730, y=0, height=110, width=100)
lbl_am_name = Label(clock,text="AM/PM", font="arial 22 bold", bg="#00F1FF", fg="black")
lbl_am_name.place(x=730, y=120, height=45, width=100)

lbl_date = Label(clock, font="arial 50 bold", bg="#00F1FF", fg="black")
lbl_date.place(x=70, y=220, height=110, width=100)
lbl_date_name = Label(clock,text="Date", font="arial 32 bold", bg="#00F1FF", fg="black")
lbl_date_name.place(x=70, y=340, height=45, width=100)

lbl_month = Label(clock, font="arial 50 bold", bg="#00F1FF", fg="black")
lbl_month.place(x=290, y=220, height=110, width=100)
lbl_month_name = Label(clock,text="Month", font="arial 24    bold", bg="#00F1FF", fg="black")
lbl_month_name.place(x=290, y=340, height=45, width=100)

lbl_year = Label(clock, font="arial 50 bold", bg="#00F1FF", fg="black")
lbl_year.place(x=510, y=220, height=110, width=100)
lbl_year_name = Label(clock,text="Year", font="arial 30 bold", bg="#00F1FF", fg="black")
lbl_year_name.place(x=510, y=340, height=45, width=100)

lbl_day = Label(clock, font="arial 40 bold", bg="#00F1FF", fg="black")
lbl_day.place(x=730, y=220, height=110, width=100)
lbl_day_name = Label(clock,text="Day", font="arial 29 bold", bg="#00F1FF", fg="black")
lbl_day_name.place(x=730, y=340, height=45, width=100)


date_time()
root.mainloop()