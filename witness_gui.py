from tkinter import *
from tkinter import ttk, messagebox
from database_operations import db_ops
import mysql.connector
from persons import Witness
from tkinter import font

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)

class WitnessManagementSystem:
    def __init__(self, window, back_callback=None):
     self.window = window
     self.back_callback = back_callback
     self.frame = Frame(self.window)
     self.frame.pack(fill=BOTH, expand=True)
     self.db_operations = db_ops(db)

     self.db_operations = db_ops(db)

     self.frame = Frame(self.window)
     self.frame.pack()

     self.witnessSelectionPage()

    def witnessSelectionPage(self):
     self.clearFrame()

     optionsFrame = LabelFrame(self.window, text="Options",bg="#79AC78")  
     optionsFrame.pack(padx=350, pady=5)
     custom_font = font.Font(family="Times New Roman", size=15)


     addVictimButton = Button(optionsFrame, text='Add Witness',bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=20, pady=20, command=self.addWitnessScreen)
     addVictimButton.grid(row=0,column=0,padx=10, pady=10)

     updateVictimButton = Button(optionsFrame, text='Update Witness',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.updateWitnessScreen)
     updateVictimButton.grid(row=1,column=0,padx=10, pady=10)

     deleteVictimButton = Button(optionsFrame, text='Delete Witness',bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=20, pady=20, command=self.deleteWitnessScreen)
     deleteVictimButton.grid(row=0,column=1,padx=10, pady=10)

     viewVictimsButton = Button(optionsFrame, text='View Witness',bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=20, pady=20, command=self.viewWitnessesScreen)
     viewVictimsButton.grid(row=1,column=1,padx=10, pady=10)
     
     backButton = Button(optionsFrame, text="Back", command=self.back_callback)
     backButton.grid(row=4, column=1, padx=20, pady=10)


    def addWitnessScreen(self):
        self.clearFrame()
        
        witnessDetailsFrame = LabelFrame(self.window, text="Add New Witness",bg="#79AC78")
        witnessDetailsFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(witnessDetailsFrame, text="Witness ID",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.idEntry = Entry(witnessDetailsFrame)
        self.idEntry.grid(row=0, column=1, padx=5, pady=5)

        caseIdLabel = Label(witnessDetailsFrame, text="Case ID",bg="#79AC78")
        caseIdLabel.grid(row=1, column=0, padx=5, pady=5)
        self.caseIdEntry = Entry(witnessDetailsFrame)
        self.caseIdEntry.grid(row=1, column=1, padx=5, pady=5)

        nameLabel = Label(witnessDetailsFrame, text="Name",bg="#79AC78")
        nameLabel.grid(row=2, column=0, padx=5, pady=5)
        self.nameEntry = Entry(witnessDetailsFrame)
        self.nameEntry.grid(row=2, column=1, padx=5, pady=5)

        ageLabel = Label(witnessDetailsFrame, text="Age",bg="#79AC78")
        ageLabel.grid(row=3, column=0, padx=5, pady=5)
        self.ageEntry = Entry(witnessDetailsFrame)
        self.ageEntry.grid(row=3, column=1, padx=5, pady=5)

        genderLabel = Label(witnessDetailsFrame, text="Gender",bg="#79AC78")
        genderLabel.grid(row=4, column=0, padx=5, pady=5)
        self.genderEntry = Entry(witnessDetailsFrame)
        self.genderEntry.grid(row=4, column=1, padx=5, pady=5)

        contactLabel = Label(witnessDetailsFrame, text="Contact",bg="#79AC78")
        contactLabel.grid(row=5, column=0, padx=5, pady=5)
        self.contactEntry = Entry(witnessDetailsFrame)
        self.contactEntry.grid(row=5, column=1, padx=5, pady=5)

        addressLabel = Label(witnessDetailsFrame, text="Address",bg="#79AC78")
        addressLabel.grid(row=6, column=0, padx=5, pady=5)
        self.addressEntry = Entry(witnessDetailsFrame)
        self.addressEntry.grid(row=6, column=1, padx=5, pady=5)

        statementLabel = Label(witnessDetailsFrame, text="Statement",bg="#79AC78")
        statementLabel.grid(row=7, column=0, padx=5, pady=5)
        self.statementEntry = Text(witnessDetailsFrame, height=5, width=30)
        self.statementEntry.grid(row=7, column=1, padx=5, pady=5)

        addButton = Button(witnessDetailsFrame, text="Save Witness Details", command=self.addWitness)
        addButton.grid(row=8, columnspan=2, padx=20, pady=10)

        backButton = Button(witnessDetailsFrame, text="Back", command=self.witnessSelectionPage)
        backButton.grid(row=9, columnspan=2, padx=20, pady=10)

    def updateWitnessScreen(self):
        self.clearFrame()

        updateWitnessFrame = LabelFrame(self.window, text="Update Witness",bg="#79AC78")
        updateWitnessFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(updateWitnessFrame, text="Witness ID to Update",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.updateIdEntry = Entry(updateWitnessFrame)
        self.updateIdEntry.grid(row=0, column=1, padx=5, pady=5)

        updateButton = Button(updateWitnessFrame, text="Update", command=self.updateWitness)
        updateButton.grid(row=1, columnspan=2, padx=10, pady=10)

        backButton = Button(updateWitnessFrame, text="Back", command=self.witnessSelectionPage)
        backButton.grid(row=2, columnspan=2, padx=10, pady=10)
    
    def updateWitness(self):
     witness_id = self.updateIdEntry.get()
     if witness_id:
        success, witness = self.db_operations.read("witness", witness_id)
        if success:
            self.clearFrame()

            updateWitnessFrame = LabelFrame(self.window, text="Update Witness",bg="#79AC78")
            updateWitnessFrame.grid(row=0, column=0, padx=350, pady=10)

            nameLabel = Label(updateWitnessFrame, text="Name",bg="#79AC78")
            nameLabel.grid(row=0, column=0, padx=5, pady=5)
            self.nameUpdateEntry = Entry(updateWitnessFrame)
            self.nameUpdateEntry.insert(0, witness[1])
            self.nameUpdateEntry.grid(row=0, column=1, padx=5, pady=5)

            ageLabel = Label(updateWitnessFrame, text="Age",bg="#79AC78")
            ageLabel.grid(row=1, column=0, padx=5, pady=5)
            self.ageUpdateEntry = Entry(updateWitnessFrame)
            self.ageUpdateEntry.insert(0, witness[2])
            self.ageUpdateEntry.grid(row=1, column=1, padx=5, pady=5)

            caseLabel = Label(updateWitnessFrame, text="Case",bg="#79AC78")
            caseLabel.grid(row=2, column=0, padx=5, pady=5)
            self.caseUpdateEntry = Entry(updateWitnessFrame)
            self.caseUpdateEntry.insert(0, witness[3])
            self.caseUpdateEntry.grid(row=2, column=1, padx=5, pady=5)

            genderLabel = Label(updateWitnessFrame, text="Gender",bg="#79AC78")
            genderLabel.grid(row=3, column=0, padx=5, pady=5)
            self.genderUpdateEntry = Entry(updateWitnessFrame)
            self.genderUpdateEntry.insert(0, witness[4])
            self.genderUpdateEntry.grid(row=3, column=1, padx=5, pady=5)

            contactLabel = Label(updateWitnessFrame, text="Contact",bg="#79AC78")
            contactLabel.grid(row=4, column=0, padx=5, pady=5)
            self.contactUpdateEntry = Entry(updateWitnessFrame)
            self.contactUpdateEntry.insert(0, witness[5])
            self.contactUpdateEntry.grid(row=4, column=1, padx=5, pady=5)

            addressLabel = Label(updateWitnessFrame, text="Address",bg="#79AC78")
            addressLabel.grid(row=5, column=0, padx=5, pady=5)
            self.addressUpdateEntry = Entry(updateWitnessFrame)
            self.addressUpdateEntry.insert(0, witness[6])
            self.addressUpdateEntry.grid(row=5, column=1, padx=5, pady=5)

            statementLabel = Label(updateWitnessFrame, text="Statement",bg="#79AC78")
            statementLabel.grid(row=6, column=0, padx=5, pady=5)
            self.statementUpdateEntry = Text(updateWitnessFrame, height=5, width=30)
            self.statementUpdateEntry.insert(END, witness[7])
            self.statementUpdateEntry.grid(row=6, column=1, padx=5, pady=5)

            updateButton = Button(updateWitnessFrame, text="Update Witness", command=lambda: self.performUpdate(witness_id))
            updateButton.grid(row=7, columnspan=2, padx=20, pady=10)

            backButton = Button(updateWitnessFrame, text="Back", command=self.witnessSelectionPage)
            backButton.grid(row=8, columnspan=2, padx=20, pady=10)
        else:
            messagebox.showerror("Error", "Witness not found.")
     else:
        messagebox.showerror("Error", "Witness ID is required.")


    def deleteWitnessScreen(self):
        self.clearFrame()

        deleteWitnessFrame = LabelFrame(self.window, text="Delete Witness",bg="#79AC78")
        deleteWitnessFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(deleteWitnessFrame, text="Witness ID to Delete",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.deleteIdEntry = Entry(deleteWitnessFrame)
        self.deleteIdEntry.grid(row=0, column=1, padx=5, pady=5)

        deleteButton = Button(deleteWitnessFrame, text="Delete", command=self.deleteWitness)
        deleteButton.grid(row=1, columnspan=2, padx=10, pady=10)

        backButton = Button(deleteWitnessFrame, text="Back", command=self.witnessSelectionPage)
        backButton.grid(row=2, columnspan=2, padx=10, pady=10)

    def viewWitnessesScreen(self):
        self.clearFrame()

        allWitnessesFrame = LabelFrame(self.window, text="All Witnesses",bg="#79AC78")
        allWitnessesFrame.grid(row=0, column=0, padx=350, pady=10)

        success, witnesses = self.db_operations.read_all("witness")
        if success:
            tree = ttk.Treeview(allWitnessesFrame, columns=("Witness ID", "Case ID", "Name", "Age", "Gender", "Contact", "Address", "Statement"), show="headings")
            tree.heading("Witness ID", text="Witness ID")
            tree.heading("Case ID", text="Case ID")
            tree.heading("Name", text="Name")
            tree.heading("Age", text="Age")
            tree.heading("Gender", text="Gender")
            tree.heading("Contact", text="Contact")
            tree.heading("Address", text="Address")
            tree.heading("Statement", text="Statement")
            
            for witness in witnesses:
                tree.insert("", "end", values=(witness[0], witness[1], witness[2], witness[3], witness[4], witness[5], witness[6], witness[7]))
            
            tree.pack()

        backButton = Button(allWitnessesFrame, text="Back", command=self.witnessSelectionPage)
        backButton.pack(pady=10)

    def clearFrame(self):
        try:
            for widget in self.window.winfo_children():
                widget.destroy()
        except Exception as e:
            print(f"Error in clearFrame: {str(e)}")


    def addWitness(self):
     witness_id = self.idEntry.get()
     case_id = self.caseIdEntry.get()
     name = self.nameEntry.get()
     age = self.ageEntry.get()
     gender = self.genderEntry.get()
     contact = self.contactEntry.get()
     address = self.addressEntry.get()
     statement = self.statementEntry.get("1.0", "end-1c")

     if witness_id and case_id and name and age and gender and contact and address and statement:
        new_witness = Witness(None, case_id, name, age, gender, contact, address, statement)
        success, message = self.db_operations.create("witness", Witness_id=witness_id, Case_info_id=case_id, Witness_name=name, Witness_age=age, Witness_gender=gender, Witness_contact=contact, Witness_address=address, Witness_statement=statement)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
     else:
        messagebox.showerror("Error", "All fields are required.")
    
    def performUpdate(self, witness_id):
     name = self.nameUpdateEntry.get()
     age = self.ageUpdateEntry.get()
     gender = self.genderUpdateEntry.get()
     contact = self.contactUpdateEntry.get()
     address = self.addressUpdateEntry.get()
     statement = self.statementUpdateEntry.get("1.0", "end-1c")

     if name and age and gender and contact and address and statement:
        updated_witness = Witness(witness_id, None, name, age, gender, contact, address, statement)
        success, message = self.db_operations.update("witness", witness_id, Witness_name=name, Witness_age=age, Witness_gender=gender, Witness_contact=contact, Witness_address=address, Witness_statement=statement)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
     else:
        messagebox.showerror("Error", "All fields are required.")

    def deleteWitness(self):
        witness_id = self.deleteIdEntry.get()
        success, message = self.db_operations.delete("witness",witness_id)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)


if __name__ == "__main__":
    root = Tk()
    app = WitnessManagementSystem(root)
    root.mainloop()

