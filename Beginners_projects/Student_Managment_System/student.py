from tkinter import *
from tkinter import ttk
import sqlite3

class Student:

    def reset_fields():
        global Roll_No_var, email_var, contact_var, gender_var, dob_var, textAddress
        for i in ['name_var', 'email_var', 'contact_var', 'gender_var', 'Roll_No_var','self.textAddress']:
            exec(f"{i}.set('')")

    def __init__(self,root):
        self.root = root
        self.root.title("Student Managment System")
        self.root.geometry(("1350x750+0+0"))

        title = Label(self.root,text="Student Managment System", relief=GROOVE, font=("times new roman",40,"bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        #*************All Variables*******************

        Roll_No_var=StringVar()
        name_var=StringVar()
        email_var=StringVar()
        gender_var=StringVar()
        contact_var=StringVar()
        dob_var=StringVar()

        self.Roll_No_var = Roll_No_var
        self.name_var = name_var
        self.email_var = email_var
        self.gender_var = gender_var
        self.contact_var = contact_var
        self.dob_var = dob_var


        #*********Manage Frame******************

        Manage_Frame = Frame(self.root,bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=10,y=70,width=450,height=650)

        m_title = Label(Manage_Frame, text="Manage Students", font=("times new roman",30,"bold"), bg="crimson", fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll No.", font=("times new roman",20,"bold"), bg="crimson", fg="white")
        lbl_roll.grid(row=1,column=0,pady=10,sticky="w")

        textRoll = Entry(Manage_Frame, textvariable=Roll_No_var, font=("times new roman",20,"bold"), bd=5, relief=GROOVE)
        textRoll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", font=("times new roman",20,"bold"), bg="crimson", fg="white")
        lbl_name.grid(row=2,column=0,pady=10,sticky="w")

        textName = Entry(Manage_Frame, textvariable=name_var, font=("times new roman",20,"bold"), bd=5, relief=GROOVE)
        textName.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", font=("times new roman",20,"bold"), bg="crimson", fg="white")
        lbl_Email.grid(row=3,column=0,pady=10,sticky="w")

        textEmail = Entry(Manage_Frame, textvariable=email_var, font=("times new roman",20,"bold"), bd=5, relief=GROOVE)
        textEmail.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender", font=("times new roman",20,"bold"), bg="crimson", fg="white")
        lbl_Gender.grid(row=4,column=0,pady=10,sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame, textvariable=gender_var, font=("times new roman",15,"bold"), state='readonly')
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_Contact = Label(Manage_Frame, text="Contact", font=("times new roman",20,"bold"), bg="crimson", fg="white")
        lbl_Contact.grid(row=5,column=0,pady=10,sticky="w")

        textContact = Entry(Manage_Frame, textvariable=contact_var, font=("times new roman",20,"bold"), bd=5, relief=GROOVE)
        textContact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_DOB = Label(Manage_Frame, text="D.O.B.", font=("times new roman",20,"bold"), bg="crimson", fg="white")
        lbl_DOB.grid(row=6,column=0,pady=10,sticky="w")

        textDOB = Entry(Manage_Frame, textvariable=dob_var, font=("times new roman",20,"bold"), bd=5, relief=GROOVE)
        textDOB.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_Add = Label(Manage_Frame, text="Address", font=("times new roman",20,"bold"), bg="crimson", fg="white")
        lbl_Add.grid(row=7,column=0,pady=10,sticky="w")

        self.textAddress = Text(Manage_Frame, width=35, height=4, font=("",10))
        self.textAddress.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        #**********Button Frame****************

        btn_Frame = Frame(Manage_Frame,bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=10,y=570,width=420,height=50)

        AddBtn = Button(btn_Frame, text="Add", width=10, command=self.add_student)
        AddBtn.grid(row=0, column=0, padx=10, pady=10)
        updateBtn = Button(btn_Frame, text="Update", width=10).grid(row=0, column=1, padx=10, pady=10)
        deleteBtn = Button(btn_Frame, text="Delete", width=10).grid(row=0, column=2, padx=10, pady=10)
        clearBtn = Button(btn_Frame, text="Clear", width=10).grid(row=0, column=3, padx=10, pady=10)


        #**********Detail Frame*****************

        Detail_Frame = Frame(self.root,bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500,y=70,width=800,height=650)

        lbl_Search = Label(Detail_Frame, text="Search By:", font=("times new roman",20,"bold"), bg="crimson", fg="white")
        lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,width=10, font=("times new roman",15,"bold"),state="readonly")
        combo_search['values']=("Roll No.","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        textSearch = Entry(Detail_Frame,width=25, font=("times new roman",10,"bold"), bd=5, relief=GROOVE)
        textSearch.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        SearchBtn = Button(Detail_Frame, text="Search", width=10).grid(row=0, column=3, padx=10, pady=10)
        ShowBtn = Button(Detail_Frame, text="Show All", width=10).grid(row=0, column=4, padx=10, pady=10)


        #*****************Table Frame***************

        Table_Frame = Frame(Detail_Frame,bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=550)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
        Student_table = ttk.Treeview(Table_Frame, columns=("Roll No.", "Name", "Email", "Gender", "Contact", "DOB", "Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("Roll No.",text="Roll No.")
        Student_table.heading("Name",text="Name")
        Student_table.heading("Email",text="Email")
        Student_table.heading("Gender",text="Gender")
        Student_table.heading("Contact",text="Contact")
        Student_table.heading("DOB",text="DOB")
        Student_table.heading("Address",text="Address")
        Student_table['show']="headings"
        Student_table.column("Roll No.",width=100)
        Student_table.column("Name",width=100)
        Student_table.column("Email",width=100)
        Student_table.column("Gender",width=100)
        Student_table.column("Contact",width=100)
        Student_table.column("DOB",width=100)
        Student_table.column("Address",width=150)
        Student_table.pack(fill=BOTH, expand=1)



    def add_student(self):

        connector = sqlite3.connect('Beginners_projects/Student_Managment_System/STUDENT_MANAGEMENT.db')
        cursor = connector.cursor()
        cursor.execute(
        """CREATE TABLE IF NOT EXISTS STUDENT_MANAGEMENT(
            Roll_No integer,
            name text,
            email text,
            gender text,
            contact integer,
            dob integer,
            adress text
            )"""
        )

        cursor.execute("insert into STUDENT_MANAGEMENT values(%s, %s, %s, %s, %s, %s, %s)",(self.Roll_No_var.get(),
                                                                                                self.name_var.get(),
                                                                                                self.email_var.get(),
                                                                                                self.gender_var.get(),
                                                                                                self.contact_var.get(),
                                                                                                self.dob_var.get(),
                                                                                                self.textAddress.get('1.0', END)
                                                                                                ))

        connector.commit()
        connector.close()


root=Tk()
obj=Student(root)
root.mainloop()