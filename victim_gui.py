from tkinter import *
from tkinter import ttk, messagebox
from database_operations import db_ops
import mysql.connector
from persons import Victim
from tkinter import font



db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)

class VictimManagementSystem:
    def __init__(self, window, back_callback=None):
        self.window = window
        self.back_callback = back_callback
        self.frame = Frame(self.window,bg="#1a4d2e")
        self.frame.pack(fill=BOTH, expand=True)
        self.db_operations = db_ops(db)

        self.victimSelectionPage()

    def victimSelectionPage(self):
     self.clearFrame()

     optionsFrame = LabelFrame(self.window, text="Options",bg="#79AC78")  
     optionsFrame.pack(padx=350, pady=5)
     custom_font = font.Font(family="Times New Roman", size=15)


     addVictimButton = Button(optionsFrame, text='Add Victim',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.addVictimScreen)
     addVictimButton.grid(row=0,column=0,padx=10, pady=10)

     updateVictimButton = Button(optionsFrame, text='Update Victim',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.updateVictimScreen)
     updateVictimButton.grid(row=1,column=0,padx=10, pady=10)

     deleteVictimButton = Button(optionsFrame, text='Delete Victim',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.deleteVictimScreen)
     deleteVictimButton.grid(row=0,column=1,padx=10, pady=10)

     viewVictimsButton = Button(optionsFrame, text='View Victims',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.viewVictimsScreen)
     viewVictimsButton.grid(row=1,column=1,padx=10, pady=10)
     
     backButton = Button(optionsFrame, text="Back", command=self.back_callback)
     backButton.grid(row=4, column=1, padx=20, pady=10)

    
     

    def addVictimScreen(self):
        self.clearFrame()
        
        victimDetailsFrame = LabelFrame(self.window, text="Add New Victim",bg="#79AC78")
        victimDetailsFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(victimDetailsFrame, text="Victim ID",bg="#79AC78")
        idLabel.grid(row=1, column=0, padx=5, pady=5)
        self.idEntry = Entry(victimDetailsFrame)
        self.idEntry.grid(row=1, column=1, padx=5, pady=5)

        caseIdLabel = Label(victimDetailsFrame, text="Case ID",bg="#79AC78")
        caseIdLabel.grid(row=2, column=0, padx=5, pady=5)
        self.caseIdEntry = Entry(victimDetailsFrame)
        self.caseIdEntry.grid(row=2, column=1, padx=5, pady=5)

        nameLabel = Label(victimDetailsFrame, text="Name",bg="#79AC78")
        nameLabel.grid(row=3, column=0, padx=5, pady=5)
        self.nameEntry = Entry(victimDetailsFrame)
        self.nameEntry.grid(row=3, column=1, padx=5, pady=5)

        ageLabel = Label(victimDetailsFrame, text="Age",bg="#79AC78")
        ageLabel.grid(row=4, column=0, padx=5, pady=5)
        self.ageEntry = Entry(victimDetailsFrame)
        self.ageEntry.grid(row=4, column=1, padx=5, pady=5)

        genderLabel = Label(victimDetailsFrame, text="Gender",bg="#79AC78")
        genderLabel.grid(row=5, column=0, padx=5, pady=5)
        self.genderEntry = Entry(victimDetailsFrame)
        self.genderEntry.grid(row=5, column=1, padx=5, pady=5)

        contactLabel = Label(victimDetailsFrame, text="Contact",bg="#79AC78")
        contactLabel.grid(row=6, column=0, padx=5, pady=5)
        self.contactEntry = Entry(victimDetailsFrame)
        self.contactEntry.grid(row=6, column=1, padx=5, pady=5)

        statusLabel = Label(victimDetailsFrame, text="Status",bg="#79AC78")
        statusLabel.grid(row=7, column=0, padx=5, pady=5)
        self.statusEntry = Entry(victimDetailsFrame)
        self.statusEntry.grid(row=7, column=1, padx=5, pady=5)

        addressLabel = Label(victimDetailsFrame, text="Address",bg="#79AC78")
        addressLabel.grid(row=8, column=0, padx=5, pady=5)
        self.addressEntry = Entry(victimDetailsFrame)
        self.addressEntry.grid(row=8, column=1, padx=5, pady=5)

        bloodGroupLabel = Label(victimDetailsFrame, text="Blood Group",bg="#79AC78")
        bloodGroupLabel.grid(row=9, column=0, padx=5, pady=5)
        self.bloodGroupEntry = Entry(victimDetailsFrame)
        self.bloodGroupEntry.grid(row=9, column=1, padx=5, pady=5)

        addButton = Button(victimDetailsFrame, text="Save Victim Details", command=self.addVictim)
        addButton.grid(row=10, columnspan=2, padx=20, pady=10)

        backButton = Button(victimDetailsFrame, text="Back", command=self.victimSelectionPage)
        backButton.grid(row=11, columnspan=2, padx=20, pady=10)

    def updateVictimScreen(self):
        self.clearFrame()

        updateVictimFrame = LabelFrame(self.window, text="Update Victim",bg="#79AC78")
        updateVictimFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(updateVictimFrame, text="Victim ID to Update",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.updateIdEntry = Entry(updateVictimFrame)
        self.updateIdEntry.grid(row=0, column=1, padx=5, pady=5)

        updateButton = Button(updateVictimFrame, text="Update", command=self.updateVictim)
        updateButton.grid(row=1, columnspan=2, padx=10, pady=10)

        backButton = Button(updateVictimFrame, text="Back", command=self.victimSelectionPage)
        backButton.grid(row=2, columnspan=2, padx=10, pady=10)

    def deleteVictimScreen(self):
        self.clearFrame()

        deleteVictimFrame = LabelFrame(self.window, text="Delete Victim",bg="#79AC78")
        deleteVictimFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(deleteVictimFrame, text="Victim ID to Delete",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.deleteIdEntry = Entry(deleteVictimFrame)
        self.deleteIdEntry.grid(row=0, column=1, padx=5, pady=5)

        deleteButton = Button(deleteVictimFrame, text="Delete", command=self.deleteVictim)
        deleteButton.grid(row=1, columnspan=2, padx=10, pady=10)

        backButton = Button(deleteVictimFrame, text="Back", command=self.victimSelectionPage)
        backButton.grid(row=2, columnspan=2, padx=10, pady=10)

    def viewVictimsScreen(self):
        self.clearFrame()

        allVictimsFrame = LabelFrame(self.window, text="All Victims",bg="#79AC78")
        allVictimsFrame.grid(row=0, column=0, padx=20, pady=10)

        success, victims = self.db_operations.read_all("victim")
        if success:
            tree = ttk.Treeview(allVictimsFrame, columns=("Victim ID", "Case ID", "Name", "Age", "Gender", "Contact", "Status", "Address", "Blood Group"))
            tree.heading("#0", text="", anchor="center") 
            tree.heading("Victim ID", text="Victim ID", anchor="center")
            tree.heading("Case ID", text="Case ID", anchor="center")
            tree.heading("Name", text="Name", anchor="center")
            tree.heading("Age", text="Age", anchor="center")
            tree.heading("Gender", text="Gender", anchor="center")
            tree.heading("Contact", text="Contact", anchor="center")
            tree.heading("Status", text="Status", anchor="center")
            tree.heading("Address", text="Address", anchor="center")
            tree.heading("Blood Group", text="Blood Group", anchor="center")

            for victim in victims:
                tree.insert("", "end", values=victim)
            
            tree.pack()
        backButton = Button(self.window, text="Back", command=self.victimSelectionPage)
        backButton.grid(row=1, column=0, padx=10, pady=10)

    def addVictim(self):
        victim_id = self.idEntry.get()
        case_info_id = self.caseIdEntry.get()
        name = self.nameEntry.get()
        age = self.ageEntry.get()
        gender = self.genderEntry.get()
        contact = self.contactEntry.get()
        status = self.statusEntry.get()
        address = self.addressEntry.get()
        blood_group = self.bloodGroupEntry.get()

        if victim_id and case_info_id and name and age and gender and contact and status and address and blood_group:
            new_victim = Victim(None, name, age, gender, contact, status, address, blood_group, case_info_id)

            success, message = self.db_operations.create("victim", Victim_id=victim_id, case_info_id=case_info_id, Victim_name=name, Victim_age=age, Victim_gender=gender, Victim_contact=contact, Victim_status=status, Victim_address=address, Victim_bloodgroup=blood_group)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def updateVictim(self):
        victim_id = self.updateIdEntry.get()
        if victim_id:
            success, victim = self.db_operations.read("victim", victim_id)
            if success:
                self.clearFrame()

                updateVictimFrame = LabelFrame(self.window, text="Update Victim",bg="#79AC78")
                updateVictimFrame.grid(row=0, column=0, padx=350, pady=10)

                nameLabel = Label(updateVictimFrame, text="Name",bg="#79AC78")
                nameLabel.grid(row=0, column=0, padx=5, pady=5)
                self.nameUpdateEntry = Entry(updateVictimFrame)
                self.nameUpdateEntry.insert(0, victim[2])
                self.nameUpdateEntry.grid(row=0, column=1, padx=5, pady=5)

                ageLabel = Label(updateVictimFrame, text="Age",bg="#79AC78")
                ageLabel.grid(row=1, column=0, padx=5, pady=5)
                self.ageUpdateEntry = Entry(updateVictimFrame)
                self.ageUpdateEntry.insert(0, victim[3])
                self.ageUpdateEntry.grid(row=1, column=1, padx=5, pady=5)

                genderLabel = Label(updateVictimFrame, text="Gender",bg="#79AC78")
                genderLabel.grid(row=2, column=0, padx=5, pady=5)
                self.genderUpdateEntry = Entry(updateVictimFrame)
                self.genderUpdateEntry.insert(0, victim[4])
                self.genderUpdateEntry.grid(row=2, column=1, padx=5, pady=5)

                contactLabel = Label(updateVictimFrame, text="Contact",bg="#79AC78")
                contactLabel.grid(row=3, column=0, padx=5, pady=5)
                self.contactUpdateEntry = Entry(updateVictimFrame)
                self.contactUpdateEntry.insert(0, victim[5])
                self.contactUpdateEntry.grid(row=3, column=1, padx=5, pady=5)

                statusLabel = Label(updateVictimFrame, text="Status",bg="#79AC78")
                statusLabel.grid(row=4, column=0, padx=5, pady=5)
                self.statusUpdateEntry = Entry(updateVictimFrame)
                self.statusUpdateEntry.insert(0, victim[6])
                self.statusUpdateEntry.grid(row=4, column=1, padx=5, pady=5)

                addressLabel = Label(updateVictimFrame, text="Address",bg="#79AC78")
                addressLabel.grid(row=5, column=0, padx=5, pady=5)
                self.addressUpdateEntry = Entry(updateVictimFrame)
                self.addressUpdateEntry.insert(0, victim[7])
                self.addressUpdateEntry.grid(row=5, column=1, padx=5, pady=5)

                bloodGroupLabel = Label(updateVictimFrame, text="Blood Group",bg="#79AC78")
                bloodGroupLabel.grid(row=6, column=0, padx=5, pady=5)
                self.bloodGroupUpdateEntry = Entry(updateVictimFrame)
                self.bloodGroupUpdateEntry.insert(0, victim[8])
                self.bloodGroupUpdateEntry.grid(row=6, column=1, padx=5, pady=5)

                updateButton = Button(updateVictimFrame, text="Update Victim", command=lambda: self.performUpdate(victim_id))
                updateButton.grid(row=7, columnspan=2, padx=20, pady=10)

                backButton = Button(updateVictimFrame, text="Back", command=self.victimSelectionPage)
                backButton.grid(row=8, columnspan=2, padx=20, pady=10)
            else:
                messagebox.showerror("Error", "Victim not found.")
        else:
            messagebox.showerror("Error", "Victim ID is required.")

    def performUpdate(self, victim_id):
        name = self.nameUpdateEntry.get()
        age = self.ageUpdateEntry.get()
        gender = self.genderUpdateEntry.get()
        contact = self.contactUpdateEntry.get()
        status = self.statusUpdateEntry.get()
        address = self.addressUpdateEntry.get()
        blood_group = self.bloodGroupUpdateEntry.get()

        if name and age and gender and contact and status and address and blood_group:
            updated_victim = Victim(victim_id, name, age, gender, contact, status, address, blood_group, None)

            success, message = self.db_operations.update("victim", victim_id, Victim_name=name, Victim_age=age, Victim_gender=gender, Victim_contact=contact, Victim_status=status, Victim_address=address, Victim_bloodgroup=blood_group)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def deleteVictim(self):
        victim_id = self.deleteIdEntry.get()
        if victim_id:
            success, message = self.db_operations.delete("victim", victim_id)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "Victim ID is required.")

    def clearFrame(self):
        try:
            for widget in self.window.winfo_children():
                widget.destroy()
        except Exception as e:
            print(f"Error in clearFrame: {str(e)}")

if __name__ == "__main__":
    root = Tk() 
    app = VictimManagementSystem(root)
    root.mainloop()

