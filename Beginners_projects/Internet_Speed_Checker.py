from tkinter import *
import speedtest


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    download = str(round(sp.download()/(10**6),3))+"Mb/s"
    upload = str(round(sp.upload()/(10**6),3))+"Mb/s"
    text_download.config(text=download)
    text_upload.config(text=upload)

sp = Tk()
image_icon = PhotoImage(file="Beginners_projects/Images/browser.png")
sp.iconphoto(False, image_icon)
sp.title("Internet Speed Tester")
sp.geometry("500x550+100+100")
sp.config(bg="Blue")

lbl = Label(sp, text="Internet Speed Test", font=("Time New Roman", 30, "bold"), bg="blue", fg="white")
lbl.place(x=60,y=40, height=50, width=380)

lbl_download = Label(sp, text="Download Speed", font=("Time New Roman", 30, "bold"))
lbl_download.place(x=60,y=130, height=50, width=380)

text_download = Label(sp, font=("Time New Roman", 30, "bold"))
text_download.place(x=60,y=200, height=50, width=380)

lbl_upload = Label(sp, text="Upload Speed", font=("Time New Roman", 30, "bold"))
lbl_upload.place(x=60,y=290, height=50, width=380)

text_upload = Label(sp, font=("Time New Roman", 30, "bold"))
text_upload.place(x=60,y=360, height=50, width=380)

button = Button(sp, text="Check Speed", font=("Time New Roman", 30, "bold"), relief=RAISED, bg="red", fg="white", command=speedcheck)
button.place(x=60,y=460, height=50, width=380)

sp.mainloop()