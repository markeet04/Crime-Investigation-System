from tkinter import *
from tkinter import ttk, messagebox
from database_operations import db_ops
import mysql.connector
from persons import InvestigatingOfficer
from tkinter import font

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)

class OfficerManagementSystem:
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


        addOfficerButton = Button(optionsFrame, text='Add Officer',bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=20, pady=20, command=self.addOfficerScreen)
        addOfficerButton.grid(row=0,column=0,padx=100, pady=10)

        updateOfficerButton = Button(optionsFrame, text='Update Officer',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.updateOfficerScreen)
        updateOfficerButton.grid(row=1,column=0,padx=100, pady=10)

        deleteOfficerButton = Button(optionsFrame, text='Delete Officer',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.deleteOfficerScreen)
        deleteOfficerButton.grid(row=0,column=1,padx=100, pady=10)

        viewOfficersButton = Button(optionsFrame, text='View Officers',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.viewOfficersScreen)
        viewOfficersButton.grid(row=1,column=1,padx=100, pady=10)
        if self.back_callback:
            backButton = Button(optionsFrame, text="Back", command=self.back_callback)
            backButton.grid(row=3, column=1, padx=20, pady=10)

    def addOfficerScreen(self):
        self.clearFrame()
        
        officerDetailsFrame = LabelFrame(self.frame, text="Add New Officer",bg="#79AC78")
        officerDetailsFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(officerDetailsFrame, text="ID",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.idEntry = Entry(officerDetailsFrame)
        self.idEntry.grid(row=0, column=1, padx=5, pady=5)

        agencyIdLabel = Label(officerDetailsFrame, text="Agency ID",bg="#79AC78")
        agencyIdLabel.grid(row=1, column=0, padx=5, pady=5)
        self.agencyIdEntry = Entry(officerDetailsFrame)
        self.agencyIdEntry.grid(row=1, column=1, padx=5, pady=5)

        caseIdLabel = Label(officerDetailsFrame, text="Case ID",bg="#79AC78")
        caseIdLabel.grid(row=2, column=0, padx=5, pady=5)
        self.caseIdEntry = Entry(officerDetailsFrame)
        self.caseIdEntry.grid(row=2, column=1, padx=5, pady=5)

        batchLabel = Label(officerDetailsFrame, text="Batch No.",bg="#79AC78")
        batchLabel.grid(row=3, column=0, padx=5, pady=5)
        self.batchEntry = Entry(officerDetailsFrame)
        self.batchEntry.grid(row=3, column=1, padx=5, pady=5)

        nameLabel = Label(officerDetailsFrame, text="Name",bg="#79AC78")
        nameLabel.grid(row=4, column=0, padx=5, pady=5)
        self.nameEntry = Entry(officerDetailsFrame)
        self.nameEntry.grid(row=4, column=1, padx=5, pady=5)

        ageLabel = Label(officerDetailsFrame, text="Age",bg="#79AC78")
        ageLabel.grid(row=5, column=0, padx=5, pady=5)
        self.ageEntry = Entry(officerDetailsFrame)
        self.ageEntry.grid(row=5, column=1, padx=5, pady=5)

        genderLabel = Label(officerDetailsFrame, text="Gender",bg="#79AC78")
        genderLabel.grid(row=6, column=0, padx=5, pady=5)
        self.genderEntry = Entry(officerDetailsFrame)
        self.genderEntry.grid(row=6, column=1, padx=5, pady=5)

        contactLabel = Label(officerDetailsFrame, text="Contact",bg="#79AC78")
        contactLabel.grid(row=7, column=0, padx=5, pady=5)
        self.contactEntry = Entry(officerDetailsFrame)
        self.contactEntry.grid(row=7, column=1, padx=5, pady=5)

        addressLabel = Label(officerDetailsFrame, text="Address",bg="#79AC78")
        addressLabel.grid(row=8, column=0, padx=5, pady=5)
        self.addressEntry = Entry(officerDetailsFrame)
        self.addressEntry.grid(row=8, column=1, padx=5, pady=5)

        rankLabel = Label(officerDetailsFrame, text="Rank",bg="#79AC78")
        rankLabel.grid(row=9, column=0, padx=5, pady=5)
        self.rankEntry = Entry(officerDetailsFrame)
        self.rankEntry.grid(row=9, column=1, padx=5, pady=5)

        positionLabel = Label(officerDetailsFrame, text="Position",bg="#79AC78")
        positionLabel.grid(row=10, column=0, padx=5, pady=5)
        self.positionEntry = Entry(officerDetailsFrame)
        self.positionEntry.grid(row=10, column=1, padx=5, pady=5)

        departmentLabel = Label(officerDetailsFrame, text="Department",bg="#79AC78")
        departmentLabel.grid(row=11, column=0, padx=5, pady=5)
        self.departmentEntry = Entry(officerDetailsFrame)
        self.departmentEntry.grid(row=11, column=1, padx=5, pady=5)

        addButton = Button(officerDetailsFrame, text="Save Officer Details", command=self.addOfficer)
        addButton.grid(row=12, columnspan=2, padx=20, pady=10)

        backButton = Button(officerDetailsFrame, text="Back", command=self.selectionPage)
        backButton.grid(row=13, columnspan=2, padx=20, pady=10)

    def updateOfficerScreen(self):
        self.clearFrame()

        idLabel = Label(self.frame, text="Enter Officer ID to Update:",bg="#79AC78")
        idLabel.pack(padx=10, pady=10)
        self.updateIdEntry = Entry(self.frame)
        self.updateIdEntry.pack(padx=10, pady=10)

        updateButton = Button(self.frame, text="Update", command=self.updateOfficer)
        updateButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def deleteOfficerScreen(self):
        self.clearFrame()

        idLabel = Label(self.frame, text="Enter Officer ID to Delete:",bg="#79AC78")
        idLabel.pack(padx=10, pady=10)
        self.deleteIdEntry = Entry(self.frame)
        self.deleteIdEntry.pack(padx=10, pady=10)

        deleteButton = Button(self.frame, text="Delete", command=self.deleteOfficer)
        deleteButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def viewOfficersScreen(self):
        self.clearFrame()

        allOfficersFrame = LabelFrame(self.frame, text="All Officers",bg="#79AC78")
        allOfficersFrame.pack(padx=350, pady=10)

        success, officers = self.db_operations.read_all("Investigating_officers")
        if success:
            tree = ttk.Treeview(allOfficersFrame, columns=("ID", "Agency ID", "Case ID", "Batch No.", "Name", "Age", "Gender", "Contact", "Address", "Rank", "Position", "Department"))
            tree.heading("#0", text="", anchor="center") 
            tree.heading("ID", text="ID", anchor="center")
            tree.heading("Agency ID", text="Agency ID", anchor="center")
            tree.heading("Case ID", text="Case ID", anchor="center")
            tree.heading("Batch No.", text="Batch No.", anchor="center")
            tree.heading("Name", text="Name", anchor="center")
            tree.heading("Age", text="Age", anchor="center")
            tree.heading("Gender", text="Gender", anchor="center")
            tree.heading("Contact", text="Contact", anchor="center")
            tree.heading("Address", text="Address", anchor="center")
            tree.heading("Rank", text="Rank", anchor="center")
            tree.heading("Position", text="Position", anchor="center")
            tree.heading("Department", text="Department", anchor="center")

            
            for officer in officers:
                tree.insert("", "end", values=officer)
            
            tree.pack()

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def addOfficer(self):
        investigating_officers_id = self.idEntry.get()
        agency_id = self.agencyIdEntry.get()
        case_info_id = self.caseIdEntry.get()  
        batch_no = self.batchEntry.get()
        name = self.nameEntry.get()
        age = self.ageEntry.get()
        gender = self.genderEntry.get()
        contact = self.contactEntry.get()
        address = self.addressEntry.get()
        rank = self.rankEntry.get()
        position = self.positionEntry.get()
        department = self.departmentEntry.get()

        if investigating_officers_id and agency_id and case_info_id and batch_no and name and age and gender and contact and address and rank and position and department:
            new_officer = InvestigatingOfficer(None, batch_no, name, age, gender, contact, address, rank,position, department, agency_id, case_info_id)

            success, message = self.db_operations.create("Investigating_officers", investigating_officers_id=investigating_officers_id, Agency_id=agency_id, case_info_id=case_info_id, Batch_no=batch_no, Officer_name=name, Officer_age=age, Officer_gender=gender, Officer_contact=contact, Officer_address=address, Officer_officer_rank=rank, Officer_position=position, Officer_department=department)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def updateOfficer(self):
        investigating_officers_id = self.updateIdEntry.get()
        if investigating_officers_id:
            success, officer = self.db_operations.read("Investigating_officers", investigating_officers_id)
            if success:
                self.clearFrame()

                updateOfficerFrame = LabelFrame(self.frame, text="Update Officer",bg="#79AC78")
                updateOfficerFrame.pack(padx=350, pady=10)

                agencyIdLabel = Label(updateOfficerFrame, text="Agency ID",bg="#79AC78")
                agencyIdLabel.grid(row=0, column=0, padx=5, pady=5)
                self.agencyIdUpdateEntry = Entry(updateOfficerFrame)
                self.agencyIdUpdateEntry.insert(0, officer[1])
                self.agencyIdUpdateEntry.grid(row=0, column=1, padx=5, pady=5)

                caseIdLabel = Label(updateOfficerFrame, text="Case ID",bg="#79AC78")
                caseIdLabel.grid(row=1, column=0, padx=5, pady=5)
                self.caseIdUpdateEntry = Entry(updateOfficerFrame)
                self.caseIdUpdateEntry.insert(0, officer[2])
                self.caseIdUpdateEntry.grid(row=1, column=1, padx=5, pady=5)

                batchLabel = Label(updateOfficerFrame, text="Batch No.",bg="#79AC78")
                batchLabel.grid(row=2, column=0, padx=5, pady=5)
                self.batchUpdateEntry = Entry(updateOfficerFrame)
                self.batchUpdateEntry.insert(0, officer[3])
                self.batchUpdateEntry.grid(row=2, column=1, padx=5, pady=5)

                nameLabel = Label(updateOfficerFrame, text="Name",bg="#79AC78")
                nameLabel.grid(row=3, column=0, padx=5, pady=5)
                self.nameUpdateEntry = Entry(updateOfficerFrame)
                self.nameUpdateEntry.insert(0, officer[4])
                self.nameUpdateEntry.grid(row=3, column=1, padx=5, pady=5)

                ageLabel = Label(updateOfficerFrame, text="Age",bg="#79AC78")
                ageLabel.grid(row=4, column=0, padx=5, pady=5)
                self.ageUpdateEntry = Entry(updateOfficerFrame)
                self.ageUpdateEntry.insert(0, officer[5])
                self.ageUpdateEntry.grid(row=4, column=1, padx=5, pady=5)

                genderLabel = Label(updateOfficerFrame, text="Gender",bg="#79AC78")
                genderLabel.grid(row=5, column=0, padx=5, pady=5)
                self.genderUpdateEntry = Entry(updateOfficerFrame)
                self.genderUpdateEntry.insert(0, officer[6])
                self.genderUpdateEntry.grid(row=5, column=1, padx=5, pady=5)

                contactLabel = Label(updateOfficerFrame, text="Contact",bg="#79AC78")
                contactLabel.grid(row=6, column=0, padx=5, pady=5)
                self.contactUpdateEntry = Entry(updateOfficerFrame)
                self.contactUpdateEntry.insert(0, officer[7])
                self.contactUpdateEntry.grid(row=6, column=1, padx=5, pady=5)

                addressLabel = Label(updateOfficerFrame, text="Address",bg="#79AC78")
                addressLabel.grid(row=7, column=0, padx=5, pady=5)
                self.addressUpdateEntry = Entry(updateOfficerFrame)
                self.addressUpdateEntry.insert(0, officer[8])
                self.addressUpdateEntry.grid(row=7, column=1, padx=5, pady=5)

                rankLabel = Label(updateOfficerFrame, text="Rank",bg="#79AC78")
                rankLabel.grid(row=8, column=0, padx=5, pady=5)
                self.rankUpdateEntry = Entry(updateOfficerFrame)
                self.rankUpdateEntry.insert(0, officer[9])
                self.rankUpdateEntry.grid(row=8, column=1, padx=5, pady=5)

                positionLabel = Label(updateOfficerFrame, text="Position",bg="#79AC78")
                positionLabel.grid(row=9, column=0, padx=5, pady=5)
                self.positionUpdateEntry = Entry(updateOfficerFrame)
                self.positionUpdateEntry.insert(0, officer[10])
                self.positionUpdateEntry.grid(row=9, column=1, padx=5, pady=5)

                departmentLabel = Label(updateOfficerFrame, text="Department",bg="#79AC78")
                departmentLabel.grid(row=10, column=0, padx=5, pady=5)
                self.departmentUpdateEntry = Entry(updateOfficerFrame)
                self.departmentUpdateEntry.insert(0, officer[11])
                self.departmentUpdateEntry.grid(row=10, column=1, padx=5, pady=5)

                updateButton = Button(updateOfficerFrame, text="Update Officer", command=lambda: self.performUpdate(investigating_officers_id))
                updateButton.grid(row=12, columnspan=2, padx=20, pady=10)

                backButton = Button(self.frame, text="Back", command=self.selectionPage)
                backButton.pack(padx=10, pady=10)

            else:
                messagebox.showerror("Error", "Officer not found.")
        else:
            messagebox.showerror("Error", "Officer ID is required.")

    def performUpdate(self, investigating_officers_id):
        agency_id = self.agencyIdUpdateEntry.get()
        case_info_id = self.caseIdUpdateEntry.get()
        batch_no = self.batchUpdateEntry.get()
        name = self.nameUpdateEntry.get()
        age = self.ageUpdateEntry.get()
        gender = self.genderUpdateEntry.get()
        contact = self.contactUpdateEntry.get()
        address = self.addressUpdateEntry.get()
        rank = self.rankUpdateEntry.get()
        position = self.positionUpdateEntry.get()
        department = self.departmentUpdateEntry.get()

        if agency_id and case_info_id and batch_no and name and age and gender and contact and address and rank and position and department:
            updated_officer = InvestigatingOfficer(investigating_officers_id, batch_no, name, age, gender, contact, address, rank,position, department, agency_id, case_info_id)

            success, message = self.db_operations.update("Investigating_officers", investigating_officers_id, Agency_id=agency_id, case_info_id=case_info_id, Batch_no=batch_no, Officer_name=name, Officer_age=age, Officer_gender=gender, Officer_contact=contact, Officer_address=address, Officer_officer_rank=rank, Officer_position=position, Officer_department=department)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def deleteOfficer(self):
        investigating_officers_id = self.deleteIdEntry.get()
        if investigating_officers_id:
            success, message = self.db_operations.delete("Investigating_officers", investigating_officers_id)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "Officer ID is required.")

    def clearFrame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = Tk()
    app = OfficerManagementSystem(root)
    root.mainloop()
