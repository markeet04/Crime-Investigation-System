from tkinter import *
from tkinter import ttk, messagebox
from persons import Suspect
from database_operations import db_ops
import mysql.connector
from tkinter import font

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)

class SuspectManagementSystem:
    def __init__(self, window, back_callback=None):
        self.window = window
        self.back_callback = back_callback
        self.frame = Frame(self.window)
        self.frame.pack(fill=BOTH, expand=True)
        self.db_operations = db_ops(db)


        self.selectionPage()

    def selectionPage(self):
        self.clearFrame()

        optionsFrame = LabelFrame(self.window, text="Options")
        optionsFrame.pack(padx=350, pady=10)
        custom_font = font.Font(family="Times New Roman", size=15)


        addSuspectButton = Button(optionsFrame, text='Add Suspect',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.addSuspectScreen)
        addSuspectButton.pack(padx=20, pady=10)

        updateSuspectButton = Button(optionsFrame, text='Update Suspect',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.updateSuspectScreen)
        updateSuspectButton.pack(padx=20, pady=10)

        deleteSuspectButton = Button(optionsFrame, text='Delete Suspect',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.deleteSuspectScreen)
        deleteSuspectButton.pack(padx=20, pady=10)

        viewSuspectsButton = Button(optionsFrame, text='View Suspects', bg="#7AB2B2",fg="black",font=custom_font,height=2, width=15, padx=20, pady=20, command=self.viewSuspectsScreen)
        viewSuspectsButton.pack(padx=20, pady=10)
        
        backButton = Button(optionsFrame, text="Back", command=self.back_callback)
        backButton.pack(padx=20, pady=10)

    def addSuspectScreen(self):
        self.clearFrame()
        
        suspectDetailsFrame = LabelFrame(self.window, text="Add New Suspect",bg="#79AC78")
        suspectDetailsFrame.pack(padx=20, pady=10)

        suspectIDlabel = Label(suspectDetailsFrame, text="ID",bg="#79AC78")
        suspectIDlabel.pack(padx=5, pady=5)
        self.SuspectIDentry = Entry(suspectDetailsFrame)
        self.SuspectIDentry.pack(padx=5, pady=5)


        caseIdLabel = Label(suspectDetailsFrame, text="Case ID",bg="#79AC78")
        caseIdLabel.pack(padx=5, pady=5)
        self.caseIdEntry = Entry(suspectDetailsFrame)
        self.caseIdEntry.pack(padx=5, pady=5)

        evidenceIdLabel = Label(suspectDetailsFrame, text="Evidence ID",bg="#79AC78")
        evidenceIdLabel.pack(padx=5, pady=5)
        self.evidenceIdEntry = Entry(suspectDetailsFrame)
        self.evidenceIdEntry.pack(padx=5, pady=5)

        nameLabel = Label(suspectDetailsFrame, text="Name",bg="#79AC78")
        nameLabel.pack(padx=5, pady=5)
        self.nameEntry = Entry(suspectDetailsFrame)
        self.nameEntry.pack(padx=5, pady=5)

        ageLabel = Label(suspectDetailsFrame, text="Age",bg="#79AC78")
        ageLabel.pack(padx=5, pady=5)
        self.ageEntry = Entry(suspectDetailsFrame)
        self.ageEntry.pack(padx=5, pady=5)

        genderLabel = Label(suspectDetailsFrame, text="Gender",bg="#79AC78")
        genderLabel.pack(padx=5, pady=5)
        self.genderEntry = Entry(suspectDetailsFrame)
        self.genderEntry.pack(padx=5, pady=5)

        contactLabel = Label(suspectDetailsFrame, text="Contact",bg="#79AC78")
        contactLabel.pack(padx=5, pady=5)
        self.contactEntry = Entry(suspectDetailsFrame)
        self.contactEntry.pack(padx=5, pady=5)

        addressLabel = Label(suspectDetailsFrame, text="Address",bg="#79AC78")
        addressLabel.pack(padx=5, pady=5)
        self.addressEntry = Entry(suspectDetailsFrame)
        self.addressEntry.pack(padx=5, pady=5)

        statementLabel = Label(suspectDetailsFrame, text="Statement",bg="#79AC78")
        statementLabel.pack(padx=5, pady=5)
        self.statementEntry = Text(suspectDetailsFrame, height=5, width=30)
        self.statementEntry.pack(padx=5, pady=5)

        pastRecordLabel = Label(suspectDetailsFrame, text="Past Criminal Record",bg="#79AC78")
        pastRecordLabel.pack(padx=5, pady=5)
        self.pastRecordEntry = Text(suspectDetailsFrame, height=5, width=30)
        self.pastRecordEntry.pack(padx=5, pady=5)

        addButton = Button(suspectDetailsFrame, text="Save Suspect Details", command=self.addSuspect)
        addButton.pack(padx=20, pady=10)

        backButton = Button(suspectDetailsFrame, text="Back", command=self.selectionPage)
        backButton.pack(padx=20, pady=10)

    def addSuspect(self):
     suspects_id = self.SuspectIDentry.get()
     case_info_id = self.caseIdEntry.get()
     evidence_id = self.evidenceIdEntry.get()
     suspect_name = self.nameEntry.get()
     suspect_age = self.ageEntry.get()
     suspect_gender = self.genderEntry.get()
     suspect_contact = self.contactEntry.get()
     suspect_address = self.addressEntry.get()
     suspect_statement = self.statementEntry.get("1.0", "end-1c")
     suspect_past_criminal_record = self.pastRecordEntry.get("1.0", "end-1c")

     if ( suspects_id and case_info_id and evidence_id and suspect_name and 
        suspect_age and suspect_gender and suspect_contact and 
        suspect_address and suspect_statement and suspect_past_criminal_record):

        new_suspect = Suspect(suspects_id, case_info_id, evidence_id, suspect_name, suspect_age, suspect_gender, suspect_contact, suspect_address, suspect_statement, suspect_past_criminal_record)
        
        success, message = self.db_operations.create("suspects", suspects_id=suspects_id,
            Case_info_id=case_info_id, 
            Evidence_id=evidence_id, 
            Suspect_name=suspect_name, 
            Suspect_age=suspect_age, 
            Suspect_gender=suspect_gender, 
            Suspect_contact=suspect_contact, 
            Suspect_address=suspect_address, 
            Suspect_statement=suspect_statement, 
            Suspect_past_criminal_record=suspect_past_criminal_record)

        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
     else:
        messagebox.showerror("Error", "All fields are required.")

    def updateSuspectScreen(self):
        self.clearFrame()

        updateSuspectFrame = LabelFrame(self.window, text="Update Suspect",bg="#79AC78")
        updateSuspectFrame.pack(padx=20, pady=10)

        idLabel = Label(updateSuspectFrame, text="Suspect ID to Update",bg="#79AC78")
        idLabel.pack(padx=5, pady=5)
        self.updateIdEntry = Entry(updateSuspectFrame)
        self.updateIdEntry.pack(padx=5, pady=5)

        updateButton = Button(updateSuspectFrame, text="Update", command=self.updateSuspect)
        updateButton.pack(padx=10, pady=10)

        backButton = Button(updateSuspectFrame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def updateSuspect(self):
        suspects_id = self.updateIdEntry.get()
        if suspects_id:
            success, suspect = self.db_operations.read("suspects", suspects_id)
            if success:
                self.clearFrame()

                updateSuspectFrame = LabelFrame(self.frame, text="Update Suspect",bg="#79AC78")
                updateSuspectFrame.pack(padx=20, pady=10)

                nameLabel = Label(updateSuspectFrame, text="Name",bg="#79AC78")
                nameLabel.pack(padx=5, pady=5)
                self.nameUpdateEntry = Entry(updateSuspectFrame)
                self.nameUpdateEntry.insert(0, suspect[3])
                self.nameUpdateEntry.pack(padx=5, pady=5)

                ageLabel = Label(updateSuspectFrame, text="Age",bg="#79AC78")
                ageLabel.pack(padx=5, pady=5)
                self.ageUpdateEntry = Entry(updateSuspectFrame)
                self.ageUpdateEntry.insert(0, suspect[4])
                self.ageUpdateEntry.pack(padx=5, pady=5)

                caseLabel = Label(updateSuspectFrame, text="Case ID",bg="#79AC78")
                caseLabel.pack(padx=5, pady=5)
                self.caseUpdateEntry = Entry(updateSuspectFrame)
                self.caseUpdateEntry.insert(0, suspect[1])
                self.caseUpdateEntry.pack(padx=5, pady=5)

                evidenceLabel = Label(updateSuspectFrame, text="Evidence ID",bg="#79AC78")
                evidenceLabel.pack(padx=5, pady=5)
                self.evidenceUpdateEntry = Entry(updateSuspectFrame)
                self.evidenceUpdateEntry.insert(0, suspect[2])
                self.evidenceUpdateEntry.pack(padx=5, pady=5)

                genderLabel = Label(updateSuspectFrame, text="Gender",bg="#79AC78")
                genderLabel.pack(padx=5, pady=5)
                self.genderUpdateEntry = Entry(updateSuspectFrame)
                self.genderUpdateEntry.insert(0, suspect[5])
                self.genderUpdateEntry.pack(padx=5, pady=5)

                contactLabel = Label(updateSuspectFrame, text="Contact",bg="#79AC78")
                contactLabel.pack(padx=5, pady=5)
                self.contactUpdateEntry = Entry(updateSuspectFrame)
                self.contactUpdateEntry.insert(0, suspect[6])
                self.contactUpdateEntry.pack(padx=5, pady=5)

                addressLabel = Label(updateSuspectFrame, text="Address",bg="#79AC78")
                addressLabel.pack(padx=5, pady=5)
                self.addressUpdateEntry = Entry(updateSuspectFrame)
                self.addressUpdateEntry.insert(0, suspect[7])
                self.addressUpdateEntry.pack(padx=5, pady=5)

                statementLabel = Label(updateSuspectFrame, text="Statement",bg="#79AC78")
                statementLabel.pack(padx=5, pady=5)
                self.statementUpdateEntry = Text(updateSuspectFrame, height=5, width=30)
                self.statementUpdateEntry.insert('1.0', suspect[8])
                self.statementUpdateEntry.pack(padx=5, pady=5)

                pastRecordLabel = Label(updateSuspectFrame, text="Past Criminal Record",bg="#79AC78")
                pastRecordLabel.pack(padx=5, pady=5)
                self.pastRecordUpdateEntry = Text(updateSuspectFrame, height=5, width=30)
                self.pastRecordUpdateEntry.insert('1.0', suspect[9])
                self.pastRecordUpdateEntry.pack(padx=5, pady=5)

                updateButton = Button(updateSuspectFrame, text="Update Suspect Details", command=lambda: self.saveUpdatedSuspect(suspects_id))
                updateButton.pack(padx=20, pady=10)

                backButton = Button(updateSuspectFrame, text="Back", command=self.selectionPage)
                backButton.pack(padx=20, pady=10)
            else:
                messagebox.showerror("Error", "Suspect not found.")
        else:
            messagebox.showerror("Error", "Please enter a Suspect ID.")

    def saveUpdatedSuspect(self, suspects_id):
        suspect_details = {
            'suspects_id': suspects_id,
            'case_id': self.caseUpdateEntry.get(),
            'evidence_id': self.evidenceUpdateEntry.get(),
            'name': self.nameUpdateEntry.get(),
            'age': self.ageUpdateEntry.get(),
            'gender': self.genderUpdateEntry.get(),
            'contact': self.contactUpdateEntry.get(),
            'address': self.addressUpdateEntry.get(),
            'statement': self.statementUpdateEntry.get('1.0', END).strip(),
            'past_criminal_record': self.pastRecordUpdateEntry.get('1.0', END).strip()
        }
        
        if self.db_operations.update("suspects", suspect_details):
            messagebox.showinfo("Success", "Suspect details updated successfully.")
            self.selectionPage()
        else:
            messagebox.showerror("Error", "Failed to update suspect details.")

    def deleteSuspectScreen(self):
        self.clearFrame()

        deleteSuspectFrame = LabelFrame(self.window, text="Delete Suspect",bg="#79AC78")
        deleteSuspectFrame.pack(padx=20, pady=10)

        idLabel = Label(deleteSuspectFrame, text="Suspect ID to Delete",bg="#79AC78")
        idLabel.pack(padx=5, pady=5)
        self.deleteIdEntry = Entry(deleteSuspectFrame)
        self.deleteIdEntry.pack(padx=5, pady=5)

        deleteButton = Button(deleteSuspectFrame, text="Delete", command=self.deleteSuspect)
        deleteButton.pack(padx=10, pady=10)

        backButton = Button(deleteSuspectFrame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def deleteSuspect(self):
        suspects_id = self.deleteIdEntry.get()
        if suspects_id:
            if self.db_operations.delete("suspects", suspects_id):
                messagebox.showinfo("Success", "Suspect deleted successfully.")
                self.selectionPage()
            else:
                messagebox.showerror("Error", "Failed to delete suspect.")
        else:
            messagebox.showerror("Error", "Please enter a Suspect ID.")

    def viewSuspectsScreen(self):
     self.clearFrame()

     allSuspectsFrame = LabelFrame(self.window, text="All Suspects",bg="#79AC78")
     allSuspectsFrame.grid(padx=20, pady=10)

     success, suspects = self.db_operations.read_all("suspects")
     if success:
        tree = ttk.Treeview(allSuspectsFrame, columns=("Suspect ID", "Case ID", "Evidence ID", "Name", "Age", "Gender", "Contact", "Address", "Statement", "Past Criminal Record"), show="headings")
        tree.heading("Suspect ID", text="Suspect ID")
        tree.heading("Case ID", text="Case ID")
        tree.heading("Evidence ID", text="Evidence ID")
        tree.heading("Name", text="Name")
        tree.heading("Age", text="Age")
        tree.heading("Gender", text="Gender")
        tree.heading("Contact", text="Contact")
        tree.heading("Address", text="Address")
        tree.heading("Statement", text="Statement")
        tree.heading("Past Criminal Record", text="Past Criminal Record")

        for suspect in suspects:
            tree.insert("", "end", values=suspect)

        tree.grid()

     backButton = Button(allSuspectsFrame, text="Back", command=self.selectionPage)
     backButton.grid(pady=10)

    def clearFrame(self):
        try:
            for widget in self.window.winfo_children():
                widget.destroy()
        except Exception as e:
            print(f"Error in clearFrame: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    SuspectManagementSystem(root)
    root.mainloop()
