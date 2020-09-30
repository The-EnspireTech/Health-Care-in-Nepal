from tkinter import*
import sqlite3



conn = sqlite3.connect('Information.db')
c = conn.cursor()

class ExtractInformation:
    def __init__(self,master):
        self.master = master
        self.frame = Frame(master, bg='white')
        self.phone = IntVar()
        
        title = Label(master, text="Search Patient Information\n using Username", font=("times new roman", 18, "bold"), bg="white", fg="blue",
                       relief=GROOVE)
        title.place(x=2, y=0, relwidth=1)

        #self.user_icon = PhotoImage("https://raw.githubusercontent.com/nirajpoudel18/Python/master/SharedPower/images/logo.png")
        
        Information_Frame = Frame(master, bg="white")
        Information_Frame.place(x=20, y=100)
        
        #logolbl = Label(Information_Frame, image=self.user_icon, bd=0).grid(row=0,column=1, columnspan=2, pady=20)
        search_user = Entry(Information_Frame, bd=1, width=24, textvariable=self.phone, relief=GROOVE, font=("", 15))
        search_user.grid(row=2, column=3, padx=20, pady=40)
        
        search_button = Button(Information_Frame, text="go", command=self.Search_Information)
        search_button.grid(row=2, column=4,padx=0, pady=40)
        
        
    def Search_Information(self):
        find_user = ('SELECT * FROM PatientInfo WHERE PatientPhone = ?')
        c.execute(find_user,[self.phone.get()])
        result = c.fetchall()
        if result:
            print("These are the user information!!")
            for value in result:
                print(result)
        else:
            print("User not found!")
        
        

root=Tk()
root.title('Hospital Information Management')
root.geometry('450x450')
ExtractInformation(root)
root.configure(bg="white")
root.mainloop()