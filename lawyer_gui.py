from tkinter import *
from tkinter import ttk, messagebox
from database_operations import db_ops
import mysql.connector
from persons import Lawyer
from tkinter import font

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)

class LawyerManagementSystem:
    def __init__(self, window, back_callback=None):
        self.window = window
        self.back_callback = back_callback
        self.frame = Frame(self.window,bg="#1a4d2e")
        self.frame.pack(fill=BOTH, expand=True)
        self.db_operations = db_ops(db)

        self.selectionPage()

    def selectionPage(self):
        self.clearFrame()

        optionsFrame = LabelFrame(self.frame, text="Options",bg="#79AC78")
        optionsFrame.grid(row=0, column=0, padx=350, pady=10)
        custom_font = font.Font(family="Times New Roman", size=15)


        addLawyerButton = Button(optionsFrame, text='Add Lawyer',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.addLawyerScreen)
        addLawyerButton.grid(row=0,column=0,padx=100, pady=10)

        updateLawyerButton = Button(optionsFrame, text='Update Lawyer', bg="#7AB2B2",fg="black",font=custom_font,height=2, width=15, padx=20, pady=20, command=self.updateLawyerScreen)
        updateLawyerButton.grid(row=1,column=0,padx=100, pady=10)

        deleteLawyerButton = Button(optionsFrame, text='Delete Lawyer',bg="#7AB2B2",fg="black",font=custom_font,height=2, width=15, padx=20, pady=20, command=self.deleteLawyerScreen)
        deleteLawyerButton.grid(row=0,column=1,padx=100, pady=10)

        viewLawyersButton = Button(optionsFrame, text='View Lawyers',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.viewLawyersScreen)
        viewLawyersButton.grid(row=1,column=1,padx=100, pady=10)
        if self.back_callback:
            backButton = Button(optionsFrame, text="Back", command=self.back_callback)
            backButton.grid(row=3, column=1, padx=20, pady=10)

    def addLawyerScreen(self):
        self.clearFrame()
        
        lawyerDetailsFrame = LabelFrame(self.frame, text="Add New Lawyer",bg="#79AC78")
        lawyerDetailsFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(lawyerDetailsFrame, text="ID",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.idEntry = Entry(lawyerDetailsFrame)
        self.idEntry.grid(row=0, column=1, padx=5, pady=5)

        caseIdLabel = Label(lawyerDetailsFrame, text="Case ID",bg="#79AC78")
        caseIdLabel.grid(row=1, column=0, padx=5, pady=5)
        self.caseIdEntry = Entry(lawyerDetailsFrame)
        self.caseIdEntry.grid(row=1, column=1, padx=5, pady=5)

        licenseLabel = Label(lawyerDetailsFrame, text="License No.",bg="#79AC78")
        licenseLabel.grid(row=2, column=0, padx=5, pady=5)
        self.licenseEntry = Entry(lawyerDetailsFrame)
        self.licenseEntry.grid(row=2, column=1, padx=5, pady=5)

        nameLabel = Label(lawyerDetailsFrame, text="Name",bg="#79AC78")
        nameLabel.grid(row=3, column=0, padx=5, pady=5)
        self.nameEntry = Entry(lawyerDetailsFrame)
        self.nameEntry.grid(row=3, column=1, padx=5, pady=5)

        genderLabel = Label(lawyerDetailsFrame, text="Gender",bg="#79AC78")
        genderLabel.grid(row=4, column=0, padx=5, pady=5)
        self.genderEntry = Entry(lawyerDetailsFrame)
        self.genderEntry.grid(row=4, column=1, padx=5, pady=5)

        addressLabel = Label(lawyerDetailsFrame, text="Address",bg="#79AC78")
        addressLabel.grid(row=5, column=0, padx=5, pady=5)
        self.addressEntry = Entry(lawyerDetailsFrame)
        self.addressEntry.grid(row=5, column=1, padx=5, pady=5)

        contactLabel = Label(lawyerDetailsFrame, text="Contact",bg="#79AC78")
        contactLabel.grid(row=6, column=0, padx=5, pady=5)
        self.contactEntry = Entry(lawyerDetailsFrame)
        self.contactEntry.grid(row=6, column=1, padx=5, pady=5)

        feeLabel = Label(lawyerDetailsFrame, text="Fee",bg="#79AC78")
        feeLabel.grid(row=7, column=0, padx=5, pady=5)
        self.feeEntry = Entry(lawyerDetailsFrame)
        self.feeEntry.grid(row=7, column=1, padx=5, pady=5)

        courtLabel = Label(lawyerDetailsFrame, text="Court",bg="#79AC78")
        courtLabel.grid(row=8, column=0, padx=5, pady=5)
        self.courtEntry = Entry(lawyerDetailsFrame)
        self.courtEntry.grid(row=8, column=1, padx=5, pady=5)

        totalCasesLabel = Label(lawyerDetailsFrame, text="Total Cases",bg="#79AC78")
        totalCasesLabel.grid(row=9, column=0, padx=5, pady=5)
        self.totalCasesEntry = Entry(lawyerDetailsFrame)
        self.totalCasesEntry.grid(row=9, column=1, padx=5, pady=5)

        winLossRatioLabel = Label(lawyerDetailsFrame, text="Win/Loss Ratio",bg="#79AC78")
        winLossRatioLabel.grid(row=10, column=0, padx=5, pady=5)
        self.winLossRatioEntry = Entry(lawyerDetailsFrame)
        self.winLossRatioEntry.grid(row=10, column=1, padx=5, pady=5)

        ageLabel = Label(lawyerDetailsFrame, text="Age",bg="#79AC78")
        ageLabel.grid(row=11, column=0, padx=5, pady=5)
        self.lawyerAge = Entry(lawyerDetailsFrame)
        self.lawyerAge.grid(row=11, column=1, padx=5, pady=5)

        addButton = Button(lawyerDetailsFrame, text="Save Lawyer Details", command=self.addLawyer)
        addButton.grid(row=12, columnspan=2, padx=20, pady=10)

        backButton = Button(lawyerDetailsFrame, text="Back", command=self.selectionPage)
        backButton.grid(row=13, columnspan=2, padx=20, pady=10)

    def updateLawyerScreen(self):
        self.clearFrame()

        idLabel = Label(self.frame, text="Enter Lawyer ID to Update:",bg="#79AC78")
        idLabel.pack(padx=10, pady=10)
        self.updateIdEntry = Entry(self.frame)
        self.updateIdEntry.pack(padx=10, pady=10)

        updateButton = Button(self.frame, text="Update", command=self.updateLawyer)
        updateButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def deleteLawyerScreen(self):
        self.clearFrame()

        idLabel = Label(self.frame, text="Enter Lawyer ID to Delete:",bg="#79AC78")
        idLabel.pack(padx=10, pady=10)
        self.deleteIdEntry = Entry(self.frame)
        self.deleteIdEntry.pack(padx=10, pady=10)

        deleteButton = Button(self.frame, text="Delete", command=self.deleteLawyer)
        deleteButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def viewLawyersScreen(self):
        self.clearFrame()

        allLawyersFrame = LabelFrame(self.frame, text="All Lawyers",bg="#79AC78")
        allLawyersFrame.pack(padx=20, pady=10)

        success, lawyers = self.db_operations.read_all("Lawyer")
        if success:
            tree = ttk.Treeview(allLawyersFrame, columns=("ID", "Case ID", "License No.", "Name", "Gender", "Address", "Contact", "Fee", "Court", "Total Cases", "Win/Loss Ratio","Lawyer_age"))
            tree.heading("#0", text="", anchor="center") 
            tree.heading("ID", text="ID", anchor="center")
            tree.heading("Case ID", text="Case ID", anchor="center")
            tree.heading("License No.", text="License No.", anchor="center")
            tree.heading("Name", text="Name", anchor="center")
            tree.heading("Gender", text="Gender", anchor="center")
            tree.heading("Address", text="Address", anchor="center")
            tree.heading("Contact", text="Contact", anchor="center")
            tree.heading("Fee", text="Fee", anchor="center")
            tree.heading("Court", text="Court", anchor="center")
            tree.heading("Total Cases", text="Total Cases", anchor="center")
            tree.heading("Win/Loss Ratio", text="Win/Loss Ratio", anchor="center")
            tree.heading("Lawyer_age", text="Lawyer_age", anchor="center")


            for lawyer in lawyers:
                tree.insert("", "end", values=lawyer)
            
            tree.pack()

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def addLawyer(self):
        lawyer_id = self.idEntry.get()
        case_info_id = self.caseIdEntry.get()
        license_no = self.licenseEntry.get()  
        lawyer_name = self.nameEntry.get()
        gender = self.genderEntry.get()
        address = self.addressEntry.get()
        contact = self.contactEntry.get()
        fee = self.feeEntry.get()
        court = self.courtEntry.get()
        total_cases = self.totalCasesEntry.get()
        win_loss_ratio = self.winLossRatioEntry.get()
        lawyer_age=self.lawyerAge.get()

        if lawyer_id and case_info_id and license_no and lawyer_name and gender and address and contact and fee and court and total_cases and win_loss_ratio and lawyer_age:
            new_lawyer = Lawyer(None, license_no, lawyer_name, gender, address, contact, fee, court, total_cases, win_loss_ratio, case_info_id,lawyer_age)

            success, message = self.db_operations.create("Lawyer", Lawyer_id=lawyer_id, case_info_id=case_info_id, Lawyer_License_no=license_no, Lawyer_name=lawyer_name, Lawyer_gender=gender, Lawyer_address=address, Lawyer_contact=contact, Lawyer_fee=fee, Authorized_court=court, Lawyer_total_cases=total_cases, Lawyer_win_loss_ratio=win_loss_ratio,lawyer_age=lawyer_age)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def updateLawyer(self):
        lawyer_id = self.updateIdEntry.get()
        if lawyer_id:
            success, lawyer = self.db_operations.read("Lawyer", lawyer_id)
            if success:
                self.clearFrame()

                updateLawyerFrame = LabelFrame(self.frame, text="Update Lawyer",bg="#79AC78")
                updateLawyerFrame.pack(padx=20, pady=10)

                caseIdLabel = Label(updateLawyerFrame, text="Case ID",bg="#79AC78")
                caseIdLabel.grid(row=0, column=0, padx=5, pady=5)
                self.caseIdUpdateEntry = Entry(updateLawyerFrame)
                self.caseIdUpdateEntry.insert(0, lawyer[1])
                self.caseIdUpdateEntry.grid(row=0, column=1, padx=5, pady=5)

                licenseLabel = Label(updateLawyerFrame, text="License No.",bg="#79AC78")
                licenseLabel.grid(row=1, column=0, padx=5, pady=5)
                self.licenseUpdateEntry = Entry(updateLawyerFrame)
                self.licenseUpdateEntry.insert(0, lawyer[2])
                self.licenseUpdateEntry.grid(row=1, column=1, padx=5, pady=5)

                nameLabel = Label(updateLawyerFrame, text="Name",bg="#79AC78")
                nameLabel.grid(row=2, column=0, padx=5, pady=5)
                self.nameUpdateEntry = Entry(updateLawyerFrame)
                self.nameUpdateEntry.insert(0, lawyer[3])
                self.nameUpdateEntry.grid(row=2, column=1, padx=5, pady=5)

                genderLabel = Label(updateLawyerFrame, text="Gender",bg="#79AC78")
                genderLabel.grid(row=3, column=0, padx=5, pady=5)
                self.genderUpdateEntry = Entry(updateLawyerFrame)
                self.genderUpdateEntry.insert(0, lawyer[4])
                self.genderUpdateEntry.grid(row=3, column=1, padx=5, pady=5)

                addressLabel = Label(updateLawyerFrame, text="Address",bg="#79AC78")
                addressLabel.grid(row=4, column=0, padx=5, pady=5)
                self.addressUpdateEntry = Entry(updateLawyerFrame)
                self.addressUpdateEntry.insert(0, lawyer[5])
                self.addressUpdateEntry.grid(row=4, column=1, padx=5, pady=5)

                contactLabel = Label(updateLawyerFrame, text="Contact",bg="#79AC78")
                contactLabel.grid(row=5, column=0, padx=5, pady=5)
                self.contactUpdateEntry = Entry(updateLawyerFrame)
                self.contactUpdateEntry.insert(0, lawyer[6])
                self.contactUpdateEntry.grid(row=5, column=1, padx=5, pady=5)

                feeLabel = Label(updateLawyerFrame, text="Fee",bg="#79AC78")
                feeLabel.grid(row=6, column=0, padx=5, pady=5)
                self.feeUpdateEntry = Entry(updateLawyerFrame)
                self.feeUpdateEntry.insert(0, lawyer[7])
                self.feeUpdateEntry.grid(row=6, column=1, padx=5, pady=5)

                courtLabel = Label(updateLawyerFrame, text="Court",bg="#79AC78")
                courtLabel.grid(row=7, column=0, padx=5, pady=5)
                self.courtUpdateEntry = Entry(updateLawyerFrame)
                self.courtUpdateEntry.insert(0, lawyer[8])
                self.courtUpdateEntry.grid(row=7, column=1, padx=5, pady=5)

                totalCasesLabel = Label(updateLawyerFrame, text="Total Cases",bg="#79AC78")
                totalCasesLabel.grid(row=8, column=0, padx=5, pady=5)
                self.totalCasesUpdateEntry = Entry(updateLawyerFrame)
                self.totalCasesUpdateEntry.insert(0, lawyer[9])
                self.totalCasesUpdateEntry.grid(row=8, column=1, padx=5, pady=5)

                winLossRatioLabel = Label(updateLawyerFrame, text="Win/Loss Ratio",bg="#79AC78")
                winLossRatioLabel.grid(row=9, column=0, padx=5, pady=5)
                self.winLossRatioUpdateEntry = Entry(updateLawyerFrame)
                self.winLossRatioUpdateEntry.insert(0, lawyer[10])
                self.winLossRatioUpdateEntry.grid(row=9, column=1, padx=5, pady=5)


                lawyerAge = Label(updateLawyerFrame, text="Age",bg="#79AC78")
                lawyerAge.grid(row=10, column=0, padx=5, pady=5)
                self.Updatedage = Entry(updateLawyerFrame)
                self.Updatedage.insert(0, lawyer[11])
                self.Updatedage.grid(row=10, column=1, padx=5, pady=5)


                updateButton = Button(updateLawyerFrame, text="Update Lawyer", command=lambda: self.performUpdate(lawyer_id))
                updateButton.grid(row=11, columnspan=2, padx=20, pady=10)

                backButton = Button(self.frame, text="Back", command=self.selectionPage)
                backButton.pack(padx=12, pady=10)

            else:
                messagebox.showerror("Error", "Lawyer not found.")
        else:
            messagebox.showerror("Error", "Lawyer ID is required.")

    def performUpdate(self, lawyer_id):
        case_info_id = self.caseIdUpdateEntry.get()
        license_no = self.licenseUpdateEntry.get()
        lawyer_name = self.nameUpdateEntry.get()
        gender = self.genderUpdateEntry.get()
        address = self.addressUpdateEntry.get()
        contact = self.contactUpdateEntry.get()
        fee = self.feeUpdateEntry.get()
        court = self.courtUpdateEntry.get()
        total_cases = self.totalCasesUpdateEntry.get()
        win_loss_ratio = self.winLossRatioUpdateEntry.get()
        lawyer_age=self.Updatedage.get()

        if case_info_id and license_no and lawyer_name and gender and address and contact and fee and court and total_cases and win_loss_ratio:
            updated_lawyer = Lawyer(lawyer_id, license_no, lawyer_name, gender, address, contact, fee, court, total_cases, win_loss_ratio, case_info_id,lawyer_age)

            success, message = self.db_operations.update("Lawyer", lawyer_id, case_info_id=case_info_id, Lawyer_License_no=license_no, Lawyer_name=lawyer_name, Lawyer_gender=gender, Lawyer_address=address, Lawyer_contact=contact, Lawyer_fee=fee, Authorized_court=court, Lawyer_total_cases=total_cases, Lawyer_win_loss_ratio=win_loss_ratio,lawyer_age=lawyer_age)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def deleteLawyer(self):
        lawyer_id = self.deleteIdEntry.get()
        if lawyer_id:
            success, message = self.db_operations.delete("Lawyer", lawyer_id)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "Lawyer ID is required.")

    def clearFrame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = Tk()
    app = LawyerManagementSystem(root)
    root.mainloop()
