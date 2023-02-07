from tkinter import *
from twilio.rest import Client
import random
from tkinter import messagebox

class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        global number
        number_file = open("Beginners_projects/Otp_Verification/Number.txt","r")
        number = str(number_file.readlines())

        self.geometry("1000x580+200+80")
        self.title("MONO")
        self.configure(bg="#A5D9FF")
        self.resizable(False, False)
        self.n = str(self.OTP())
        image_icon = PhotoImage(file="Beginners_projects/Otp_Verification/Images/logo.png")
        self.iconphoto(False, image_icon)
        self.client = Client("AC8457fdfde37e8192ce57f84117f5792f", "0d452c97512722f760a054627320c7ce")
        self.client.messages.create(to=("+91" + number),
                                    from_ = "+14066121548",
                                    body = self.n
                                        )

        number_file.close()


    def submit(self):
        try:
            self.userInput = int(self.User_Name.get(1.0, "end -1c"))
            if self.userInput == int(self.n):
                messagebox.showinfo("Showinfo", "Verification Successful")
                self.n = "done"
            else:
                messagebox.showinfo("Showinfo", "Please Enter Correct OTP or Resend OTP on your Phone")
        except:
            messagebox.showerror("Showerror", "Invalid OTP")

    def resend(self):
        self.n = str(self.OTP())
        self.client = Client("AC8457fdfde37e8192ce57f84117f5792f", "0d452c97512722f760a054627320c7ce")
        self.client.messages.create(to=("+91"+ number),
                                    from_ = "+14066121548",
                                    body = self.n
                                        )

    def OTP(self):
        return random. randrange(100000, 1000000)
    
    def Labels(self):
        self.c = Frame(self, bg="#A5D9FF", width=440, height=200)
        self.c.place(x=290, y=120)

        self.upper_frame = Frame(self, bg="#2550b8", width=1500, height=130)
        self.upper_frame.place(x=0, y=0)

        self.picture = PhotoImage(file="Beginners_projects/Otp_Verification/Images/Logo 2.png")
        self.k = Label(self.upper_frame, image=self.picture, bg="#2550b8")
        self.k.place(x=200, y=30)

        self.j = Label(self.upper_frame, text="Verify Your OTP", bg="#2550b8", font="TimesNewRoman 34 bold", fg="white")
        self.j.place(x = 350, y = 35)


    def Entry(self):

        self.label = Label(self, text="Enter the OTP in Below Field", font="TimesNewRoman 16 bold", fg="black", bg="#A5D9FF")
        self.label.place(x = 315, y=150)

        self.User_Name = Text(self, font ="calibri 20", borderwidth=2, wrap=WORD, width=27, height=1)
        self.User_Name.place(x=320, y=190)

    def Buttons(self):
        self.submitButtonImage = PhotoImage(file="Beginners_projects/Otp_Verification/Images/Submit_btn.png")
        self.submitButton = Button(self, image=self.submitButtonImage,bg="#A5D9FF", command= self.submit, border= 0)
        self.submitButton.place(x=310, y=240)

        self.resendOTPImage = PhotoImage(file="Beginners_projects/Otp_Verification/Images/resend_btn.png")
        self.resendOTP = Button(self, image=self.resendOTPImage, border = 0,bg="#A5D9FF", command = self.resend)
        self.resendOTP.place(x=510, y=240)



if __name__ == "__main__":
    window = otp_verifier()
    window.Labels()
    window.Buttons()
    window.Entry()
    window.mainloop()