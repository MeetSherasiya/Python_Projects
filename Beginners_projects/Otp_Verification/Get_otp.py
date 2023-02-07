from tkinter import *
from Receive_otp import *
from subprocess import call

class Generate_otp(Tk):
    def __init__(self):
        super().__init__()
        self.title("MONO")
        image_icon = PhotoImage(file="Beginners_projects/Otp_Verification/Images/logo.png")
        self.iconphoto(False, image_icon)
        self.geometry("1000x580+200+80")
        self.configure(bg = "#FFFFFF")
        self.resizable(False, False)
        self.f = ("Times bold", 14)

    def Labels(self):
        
        
        self.upper_frame = Frame(self , bg = "#4682B4" , width = 1500 , height = 130 )
        self.upper_frame.place ( x = 0 , y = 0 )
        self.lower_frame = Frame(self , bg = "#4682B4" , width = 1500 , height = 200 )
        self.lower_frame.place ( x = 0 , y = 270 )
        self.picture = PhotoImage (file="Beginners_projects/Otp_Verification/Images/Logo 21.png")
        self.k = Label ( self.upper_frame , image = self.picture , bg = "#4682B4").place(x=180,y=30)
        self.picture1 = PhotoImage (file="Beginners_projects/Otp_Verification/Images/OTP 1.png")
        self.l = Label ( self.upper_frame , image = self.picture1 , bg = "#4682B4").place(x=750,y=37)

        self.middle_frame = Frame(self, width = 1500 , height = 130)
        self.middle_frame.place(x=0, y=130)
        self.m = Entry(self.middle_frame, font ="calibri 20", borderwidth=2, bg="#4682B4", fg="white")
        self.m.place(x=350, y=20)

        self.j = Label(self.upper_frame, text="OTP Verification", font = "TimesNewRoman 38 bold",bg= "#4682B4", fg="white").place(x= 330, y= 35)
        self.a = Label(self, text="OTP is valid for 10 minutes.", font = "TimesNewRoman 14",bg= "#4682B4", fg="white").place(x= 370, y= 290)
        self.b = Label(self, text="Click on the Generate OTP button to generate OTP.", font = "TimesNewRoman 14", bg= '#4682B4', fg="white").place(x= 270, y= 338)
        

    def Buttons(self):
        self.GenerateOTP=PhotoImage(file="Beginners_projects/Otp_Verification/Images/Get_otp_btn.png")
        self.generatebutton = Button(self , image=self.GenerateOTP,bg="#4682B4", command = self.Open, border = 0 )
        self.generatebutton.place(x = 400 ,y = 390)

    
    def Open(self):
        number = self.m.get()
        number_file = open("Beginners_projects/Otp_Verification/Number.txt","w")
        number_file.write(number)
        number_file.close()
        program1 = self.destroy()
        call(["python", "Beginners_projects/Otp_Verification/Receive_otp.py"])




if __name__ == "__main__":
    window = Generate_otp()
    
    window.Labels()
    window.Buttons()
    window.mainloop()
    