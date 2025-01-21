from tkinter import *
from tkinter import font
from tkinter import messagebox
import mysql.connector
from Case_gui import * 
from database_operations import *
from article import *
from Agency_gui import *
from article_gui import *
from lawyer_gui import *
from investigating_officer_gui import *
from judge_gui import *
from Fir_gui import *
from criminal_record_gui import *
from Crime_gui import *
from user_gui import*
from court_gui import *
from forensic_gui import *
from report_gui import*

import os

# Database connection using mysql
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sqm22104",
    database="cid"
)

class LoginPage:
    def __init__(self, root):
        self.window = root
        self.window.title("Police Officer Login")

        self.window.geometry("800x600")  
        self.window.state("zoomed")
        root.configure(bg="#1a4d2e")
        custom_font = font.Font(family="Calibri", size=20, weight="bold")

    
        current_directory = os.path.dirname(__file__)
        image_path = os.path.join(current_directory, "qasim.png")

        self.background_image = PhotoImage(file=image_path)

        background_label = Label(self.window, image=self.background_image)
        background_label.place(relwidth=1, relheight=1)

        background_label.pack_propagate(False)

        self.login_frame = Frame(self.window, bg="#686D76",highlightbackground="#948979", highlightthickness=3)
        self.login_frame.pack(expand=True)

        self.db_operations = db_ops(db)

        self.id_label = Label(self.login_frame, text="Username", font=("helvetica", 17), bg="#686D76", fg="white")
        self.id_label.pack(pady=10,padx=20)

        self.id_entry = Entry(self.login_frame, font=("times new roman", 15), bg="white", fg="gray",highlightbackground="#948979", highlightthickness=3)
        self.id_entry.pack(pady=10,padx=20)

        # Password label and entry
        self.password_label = Label(self.login_frame, text="Password", font=("helvetica", 17), bg="#686D76", fg="white")
        self.password_label.pack(pady=10,padx=20)

        self.password_entry = Entry(self.login_frame, font=("times new roman", 15), bg="white", fg="gray", show="*",highlightbackground="#948979", highlightthickness=3 )
        self.password_entry.pack(pady=10,padx=20)

        # Login button
        self.login_button = Button(self.login_frame, text="Log In", command=self.login_func, font=("times new roman", 15), bg="#0E46A3", fg="white")
        self.login_button.pack(pady=10)
        self.report_button= Button(self.login_frame,text="File a complaint",command=self.open_public_report_submission,font=("times new roman", 15), bg="#0E46A3", fg="white")
        self.report_button.pack(pady=10)

    
    def open_public_report_submission(self):
        self.clearFrame()
        self.report_submission = PublicReportSubmission(self.window)
    def page1(self):
        self.clearFrame()
        print("Navigating to Case Selection Page...")  
        self.case_management = CaseManagementSystem(self.window, self.showOptionsPage)
        print("Case Selection Page should now be visible.")
        
    def page2(self):
        self.clearFrame()
        print("Navigating to Agency Selection Page...")  
        self.agency_management = AgencyManagementSystem(self.window,self.showOptionsPage)
        print("Agency Selection Page should now be visible.")
        
    def page3(self):
        self.clearFrame()
        print("Navigating to Article Selection Page...")  
        self.article_management = ArticleManagementSystem(self.window, self.showOptionsPage)
        print("Article Selection Page should now be visible.")
        
    def page4(self):
        self.clearFrame()
        print("Navigating to Court Selection Page...")  
        self.court_management = CourtManagementSystem(self.window,self.showOptionsPage)
        print("Court Selection Page should now be visible.")
        
    def page5(self):
        self.clearFrame()
        print("Navigating to Officer Selection Page...")  
        self.investigatingOfficer = OfficerManagementSystem(self.window,self.showOptionsPage)
        print("Officer Selection Page should now be visible.")
        
    def page6(self):
        self.clearFrame()
        print("Navigating to Lawyer Selection Page...")  
        self.lawyer_management = LawyerManagementSystem(self.window,self.showOptionsPage)
        print("Lawyer Selection Page should now be visible.")
        
    def page7(self):
        self.clearFrame()
        print("Navigating to Judge Selection Page...")  
        self.judge_management = JudgeManagementSystem(self.window,self.showOptionsPage)
        print("Judge Selection Page should now be visible.")
        
    def page8(self):
        self.clearFrame()
        print("Navigating to FIR Selection Page...")  
        self.FIR_management = FIRManagementSystem(self.window,self.showOptionsPage)
        print("FIR Selection Page should now be visible.")
        
    def page9(self):
        self.clearFrame()
        print("Navigating to Criminal Record Selection Page...")  
        self.criminalRecord = CriminalRecordManagementSystem(self.window,self.showOptionsPage)
        print("Criminal Record Selection Page should now be visible.")
        
    def page10(self):
        self.clearFrame()
        print("Navigating to Crime Selection Page...")  
        self.crimeManagement = CrimeManagementSystem(self.window,self.showOptionsPage)
        print("Crime Selection Page should now be visible.")
        
    def page11(self):
        self.clearFrame()
        print("Navigating to User Selection Page...")  
        self.Usermanagement = UserManagementSystem(self.window,self.showOptionsPage)
        print("User Selection Page should now be visible.")
    def page12(self):
        self.clearFrame()
        print("Navigating to Forensic Selection Page...")  
        self.crimeManagement = ForensicManagementSystem(self.window,self.showOptionsPage)
        print("Forensic Selection Page should now be visible.")  

    def login_func(self):
        if self.id_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error!", "All fields are required", parent=self.window)
            return

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Sqm22104",
                database="cid"
            )
            with connection.cursor() as cur:
                cur.execute("SELECT User_name, User_password FROM Users WHERE User_name = %s", (self.id_entry.get(),))
                row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error!", "Invalid Username or Password", parent=self.window)
            else:
                stored_username, stored_password = row
                entered_username = self.id_entry.get()
                entered_password = self.password_entry.get()

                if entered_username == stored_username and entered_password == stored_password:
                    messagebox.showinfo("Success", "Welcome to the Police Management System", parent=self.window)
                    self.reset_fields()
                    self.clearFrame()
        
                    for widget in self.window.winfo_children():
                        if widget.winfo_manager() == 'pack':
                            widget.destroy()

                    self.showOptionsPage()
                else:
                    messagebox.showerror("Error!", "Invalid Username or Password", parent=self.window)
        except mysql.Error as e:
            messagebox.showerror("Database Error", f"Error accessing database: {str(e)}", parent=self.window)
        except Exception as e:
            messagebox.showerror("Error!", f"An unexpected error occurred: {str(e)}", parent=self.window)
        finally:
            connection.close()

    def showOptionsPage(self):
        self.clearFrame()
        optionsFrame = LabelFrame(self.window, text="Options",bg="#79AC78")
        optionsFrame.grid(row=0, column=0, padx=450, pady=10)
        custom_font = font.Font(family="Times New Roman", size=15,weight="bold")


        manageWitnessButton = Button(optionsFrame, text="Manage Cases",bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=50, pady=10, command=self.page1)
        manageWitnessButton.grid(row=0, column=0, padx=10, pady=10) 
        manageAgencybutton = Button(optionsFrame, text="Manage Agency",bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=50, pady=10, command=self.page2)
        manageAgencybutton.grid(row=1, column=0, padx=10, pady=10)
        manageArticlebutton = Button(optionsFrame, text="Manage Article", bg="#7AB2B2",fg="black",font=custom_font,height=2, width=15, padx=50, pady=10, command=self.page3)
        manageArticlebutton.grid(row=2, column=0, padx=10, pady=10)
        manageCourtButton = Button(optionsFrame, text="Manage Court", bg="#7AB2B2",fg="black",font=custom_font,height=2, width=15, padx=50, pady=10, command=self.page4)
        manageCourtButton.grid(row=3, column=0, padx=10, pady=10)
        manageArticlebutton = Button(optionsFrame, text="Manage Officers",bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=50, pady=10, command=self.page5)
        manageArticlebutton.grid(row=4, column=0, padx=10, pady=10)
        manageArticlebutton = Button(optionsFrame, text="Manage Lawyers",bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=50, pady=10, command=self.page6)
        manageArticlebutton.grid(row=5, column=0, padx=10, pady=10)
        manageArticlebutton = Button(optionsFrame, text="Manage Judges",bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=50, pady=10, command=self.page7)
        manageArticlebutton.grid(row=0, column=1, padx=10, pady=10)
        manageArticlebutton = Button(optionsFrame, text="Manage FIR",bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=50, pady=10, command=self.page8)
        manageArticlebutton.grid(row=1, column=1, padx=10, pady=10)
        manageArticlebutton = Button(optionsFrame, text="Manage Criminal Record",bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=50, pady=10, command=self.page9)
        manageArticlebutton.grid(row=2, column=1, padx=10, pady=10)
        manageArticlebutton = Button(optionsFrame, text="Manage Crime",bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=50, pady=10, command=self.page10)
        manageArticlebutton.grid(row=3, column=1, padx=10, pady=10)
        manageArticlebutton = Button(optionsFrame, text="Manage Users",bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=50, pady=10, command=self.page11)
        manageArticlebutton.grid(row=4, column=1, padx=10, pady=10)
        manageArticlebutton = Button(optionsFrame, text="Manage Forensics",bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=50, pady=10, command=self.page12)
        manageArticlebutton.grid(row=5, column=1, padx=10, pady=10)
        logOut = Button(optionsFrame, text="Log Out", font=custom_font, bg="#0e46a3",fg="white",height=2, width=15, padx=50, pady=10, command=self.log_out)
        logOut.grid(row=13, columnspan=2, padx=20, pady=10)

         
    def log_out(self):
     self.clearFrame()
    
     LoginPage(self.window)

    
    def reset_fields(self):
        self.id_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def clearFrame(self):
        for widget in self.window.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = Tk()
    LoginPage(root)
    root.mainloop()
