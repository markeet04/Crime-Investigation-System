from tkinter import *
from tkinter import ttk, messagebox
from database_operations import db_ops
import mysql.connector
from persons import Judges
from tkinter import font

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)

class JudgeManagementSystem:
    def __init__(self, window, back_callback=None):
        self.window = window
        self.back_callback = back_callback
        self.frame = Frame(self.window,bg="#1a4d2e")
        self.frame.pack(fill=BOTH, expand=True)
        self.db_operations = db_ops(db)

        self.selectionPage()  # Display selection page initially

    def selectionPage(self):
        self.clearFrame()

        optionsFrame = LabelFrame(self.frame, text="Options",bg="#79AC78")
        optionsFrame.grid(row=0, column=0, padx=350, pady=10)
        custom_font = font.Font(family="Times New Roman", size=15)


        addJudgeButton = Button(optionsFrame, text='Add Judge',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.addJudgeScreen)
        addJudgeButton.grid(row=0,column=0,padx=100, pady=10)

        updateJudgeButton = Button(optionsFrame, text='Update Judge',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.updateJudgeScreen)
        updateJudgeButton.grid(row=1,column=0,padx=100, pady=10)

        deleteJudgeButton = Button(optionsFrame, text='Delete Judge',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.deleteJudgeScreen)
        deleteJudgeButton.grid(row=0,column=1,padx=100, pady=10)

        viewJudgesButton = Button(optionsFrame, text='View Judges',bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=20, pady=20, command=self.viewJudgesScreen)
        viewJudgesButton.grid(row=1,column=1,padx=100, pady=10)
        if self.back_callback:
            backButton = Button(optionsFrame, text="Back", command=self.back_callback)
            backButton.grid(row=3, column=1, padx=20, pady=10)

    def addJudgeScreen(self):
        self.clearFrame()
        
        judgeDetailsFrame = LabelFrame(self.frame, text="Add New Judge")
        judgeDetailsFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(judgeDetailsFrame, text="ID")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.idEntry = Entry(judgeDetailsFrame)
        self.idEntry.grid(row=0, column=1, padx=5, pady=5)

        courtIdLabel = Label(judgeDetailsFrame, text="Court ID")
        courtIdLabel.grid(row=1, column=0, padx=5, pady=5)
        self.courtIdEntry = Entry(judgeDetailsFrame)
        self.courtIdEntry.grid(row=1, column=1, padx=5, pady=5)

        nameLabel = Label(judgeDetailsFrame, text="Name")
        nameLabel.grid(row=2, column=0, padx=5, pady=5)
        self.nameEntry = Entry(judgeDetailsFrame)
        self.nameEntry.grid(row=2, column=1, padx=5, pady=5)

        appointmentLabel = Label(judgeDetailsFrame, text="Appointment")
        appointmentLabel.grid(row=3, column=0, padx=5, pady=5)
        self.appointmentEntry = Entry(judgeDetailsFrame)
        self.appointmentEntry.grid(row=3, column=1, padx=5, pady=5)

        genderLabel = Label(judgeDetailsFrame, text="Gender")
        genderLabel.grid(row=4, column=0, padx=5, pady=5)
        self.genderEntry = Entry(judgeDetailsFrame)
        self.genderEntry.grid(row=4, column=1, padx=5, pady=5)

        caseIdLabel = Label(judgeDetailsFrame, text="Case ID")
        caseIdLabel.grid(row=5, column=0, padx=5, pady=5)
        self.caseIdEntry = Entry(judgeDetailsFrame)
        self.caseIdEntry.grid(row=5, column=1, padx=5, pady=5)

        contactLabel = Label(judgeDetailsFrame, text="contact")
        contactLabel.grid(row=6, column=0, padx=5, pady=5)
        self.contactEntry = Entry(judgeDetailsFrame)
        self.contactEntry.grid(row=6, column=1, padx=5, pady=5)

        addButton = Button(judgeDetailsFrame, text="Save Judge Details", command=self.addJudge)
        addButton.grid(row=7, columnspan=2, padx=20, pady=10)

        backButton = Button(judgeDetailsFrame, text="Back", command=self.selectionPage)
        backButton.grid(row=8, columnspan=2, padx=20, pady=10)

    def updateJudgeScreen(self):
        self.clearFrame()

        idLabel = Label(self.frame, text="Enter Judge ID to Update:")
        idLabel.pack(padx=350, pady=10)
        self.updateIdEntry = Entry(self.frame)
        self.updateIdEntry.pack(padx=10, pady=10)

        updateButton = Button(self.frame, text="Update", command=self.updateJudge)
        updateButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def deleteJudgeScreen(self):
        self.clearFrame()

        idLabel = Label(self.frame, text="Enter Judge ID to Delete:")
        idLabel.pack(padx=350, pady=10)
        self.deleteIdEntry = Entry(self.frame)
        self.deleteIdEntry.pack(padx=10, pady=10)

        deleteButton = Button(self.frame, text="Delete", command=self.deleteJudge)
        deleteButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def viewJudgesScreen(self):
        self.clearFrame()

        allJudgesFrame = LabelFrame(self.frame, text="All Judges")
        allJudgesFrame.pack(padx=20, pady=10)

        success, judges = self.db_operations.read_all("Judge")
        if success:
            tree = ttk.Treeview(allJudgesFrame, columns=("ID", "Court ID", "Name", "Appointment", "Gender","Case ID",'Contact'))
            tree.heading("#0", text="", anchor="center") 
            tree.heading("ID", text="ID", anchor="center")
            tree.heading("Court ID", text="Court ID", anchor="center")
            tree.heading("Name", text="Name", anchor="center")
            tree.heading("Appointment", text="Appointment", anchor="center")
            tree.heading("Gender", text="Gender", anchor="center")
            tree.heading("Case ID", text="Case ID", anchor="center")
            tree.heading("Contact", text="Contact", anchor="center")


            
            for judge in judges:
                tree.insert("", "end", values=judge)
            
            tree.pack()

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def addJudge(self):
        judge_id = self.idEntry.get()
        court_id = self.courtIdEntry.get()
        judge_name = self.nameEntry.get()  
        judge_appointment = self.appointmentEntry.get()
        judge_gender = self.genderEntry.get()
        case_info_id=self.caseIdEntry.get()
        judge_contact=self.contactEntry.get()

        if judge_id and court_id and judge_name and judge_appointment and judge_gender and case_info_id and judge_contact:
            new_judge = Judges(judge_id, judge_name, None, judge_gender, court_id, None, case_info_id,judge_contact)
            success, message = self.db_operations.create("Judge", Judge_id=judge_id, Court_id=court_id, Judge_name=judge_name, Judge_appointment=judge_appointment, Judge_gender=judge_gender,case_info_id=case_info_id , judge_contact=judge_contact)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def updateJudge(self):
        judge_id = self.updateIdEntry.get()
        if judge_id:
            success, judge = self.db_operations.read("Judge", judge_id)
            if success:
                self.clearFrame()

                updateJudgeFrame = LabelFrame(self.frame, text="Update Judge")
                updateJudgeFrame.pack(padx=350, pady=10)

                courtIdLabel = Label(updateJudgeFrame, text="Court ID")
                courtIdLabel.grid(row=0, column=0, padx=5, pady=5)
                self.courtIdUpdateEntry = Entry(updateJudgeFrame)
                self.courtIdUpdateEntry.insert(0, judge[1])
                self.courtIdUpdateEntry.grid(row=0, column=1, padx=5, pady=5)

                nameLabel = Label(updateJudgeFrame, text="Name")
                nameLabel.grid(row=1, column=0, padx=5, pady=5)
                self.nameUpdateEntry = Entry(updateJudgeFrame)
                self.nameUpdateEntry.insert(0, judge[2])
                self.nameUpdateEntry.grid(row=1, column=1, padx=5, pady=5)

                appointmentLabel = Label(updateJudgeFrame, text="Appointment")
                appointmentLabel.grid(row=2, column=0, padx=5, pady=5)
                self.appointmentUpdateEntry = Entry(updateJudgeFrame)
                self.appointmentUpdateEntry.insert(0, judge[3])
                self.appointmentUpdateEntry.grid(row=2, column=1, padx=5, pady=5)

                genderLabel = Label(updateJudgeFrame, text="Gender")
                genderLabel.grid(row=3, column=0, padx=5, pady=5)
                self.genderUpdateEntry = Entry(updateJudgeFrame)
                self.genderUpdateEntry.insert(0, judge[4])
                self.genderUpdateEntry.grid(row=3, column=1, padx=5, pady=5)

                caseLabel = Label(updateJudgeFrame, text="CASE ID")
                caseLabel.grid(row=4, column=0, padx=5, pady=5)
                self.caseIDUpdateEntry = Entry(updateJudgeFrame)
                self.caseIDUpdateEntry.insert(0, judge[5])
                self.caseIDUpdateEntry.grid(row=4, column=1, padx=5, pady=5)

                contactLabel = Label(updateJudgeFrame, text="contact")
                contactLabel.grid(row=5, column=0, padx=5, pady=5)
                self.contactUpdate = Entry(updateJudgeFrame)
                self.contactUpdate.insert(0, judge[6])
                self.contactUpdate.grid(row=5, column=1, padx=5, pady=5)






                updateButton = Button(updateJudgeFrame, text="Update Judge", command=lambda: self.performUpdate(judge_id))
                updateButton.grid(row=7, columnspan=2, padx=20, pady=10)

                backButton = Button(self.frame, text="Back", command=self.selectionPage)
                backButton.pack(padx=10, pady=10)

            else:
                messagebox.showerror("Error", "Judge not found.")
        else:
            messagebox.showerror("Error", "Judge ID is required.")

    def performUpdate(self, judge_id):
        court_id = self.courtIdUpdateEntry.get()
        judge_name = self.nameUpdateEntry.get()
        judge_appointment = self.appointmentUpdateEntry.get()
        judge_gender = self.genderUpdateEntry.get()
        case_info_id=self.caseIDUpdateEntry.get()
        judge_contact=self.contactUpdate.get()


        if court_id and judge_name and judge_appointment and judge_gender and case_info_id and judge_contact:
            success, message = self.db_operations.update("Judge", judge_id, Court_id=court_id, Judge_name=judge_name, Judge_appointment=judge_appointment, Judge_gender=judge_gender,case_info_id=case_info_id,judge_contact=judge_contact)
            if success:
                updated_judge = Judges(judge_id, judge_name, None, judge_gender, court_id, None, case_info_id,judge_contact)

                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def deleteJudge(self):
        judge_id = self.deleteIdEntry.get()
        if judge_id:
            success, message = self.db_operations.delete("Judge", judge_id)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "Judge ID is required.")

    def clearFrame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = Tk()
    app = JudgeManagementSystem(root)
    root.mainloop()
