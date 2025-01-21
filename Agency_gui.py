from tkinter import *
from tkinter import ttk, messagebox
from database_operations import db_ops
import mysql.connector
from agency import Agency
from tkinter import font
import os

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)

class AgencyManagementSystem:
   
    def __init__(self, window, back_callback=None):
        self.window = window

        self.back_callback = back_callback
        self.window = Frame(self.window,bg="#1a4d2e")
        self.window.pack(fill=BOTH, expand=True)
        self.db_operations = db_ops(db)
        
      
        
        self.AgencySelectionPage()




        
    def addAgencyScreen(self):
        self.clearFrame()
        
        agencyDetailsFrame = LabelFrame(self.window, text="Add New Agency",bg="#79AC78")
        agencyDetailsFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(agencyDetailsFrame, text="ID",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.idEntry = Entry(agencyDetailsFrame)
        self.idEntry.grid(row=0, column=1, padx=5, pady=5)

        nameLabel = Label(agencyDetailsFrame, text="Name",bg="#79AC78")
        nameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.nameEntry = Entry(agencyDetailsFrame)
        self.nameEntry.grid(row=1, column=1, padx=5, pady=5)

        addressLabel = Label(agencyDetailsFrame, text="Address",bg="#79AC78")
        addressLabel.grid(row=2, column=0, padx=5, pady=5)
        self.addressEntry = Entry(agencyDetailsFrame)
        self.addressEntry.grid(row=2, column=1, padx=5, pady=5)

        contactLabel = Label(agencyDetailsFrame, text="Contact",bg="#79AC78")
        contactLabel.grid(row=3, column=0, padx=5, pady=5)
        self.contactEntry = Entry(agencyDetailsFrame)
        self.contactEntry.grid(row=3, column=1, padx=5, pady=5)

        expertiseLabel = Label(agencyDetailsFrame, text="Expertise",bg="#79AC78")
        expertiseLabel.grid(row=4, column=0, padx=5, pady=5)
        self.expertiseEntry = Entry(agencyDetailsFrame)
        self.expertiseEntry.grid(row=4, column=1, padx=5, pady=5)

        addButton = Button(agencyDetailsFrame, text="Save Agency Details", command=self.addAgency)
        addButton.grid(row=5, columnspan=2, padx=20, pady=10)

        backButton = Button(agencyDetailsFrame, text="Back", command=self.AgencySelectionPage)
        backButton.grid(row=6, columnspan=2, padx=20, pady=10)

    def updateAgencyScreen(self):
        self.clearFrame()
        

        idLabel = Label(self.window, text="Enter Agency ID to Update:",bg="#79AC78")
        idLabel.pack(padx=10, pady=10)
        self.updateIdEntry = Entry(self.window)
        self.updateIdEntry.pack(padx=350, pady=10)

        updateButton = Button(self.window, text="Update", command=lambda: self.updateAgency(self.updateIdEntry.get()))
        updateButton.pack(padx=10, pady=10)

        backButton = Button(self.window, text="Back", command=self.AgencySelectionPage)
        backButton.pack(padx=10, pady=10)

    def deleteAgencyScreen(self):
        self.clearFrame()

        idLabel = Label(self.window, text="Enter Agency ID to Delete:",bg="#79AC78")
        idLabel.pack(padx=350, pady=10)
        self.deleteIdEntry = Entry(self.window)
        self.deleteIdEntry.pack(padx=10, pady=10)

        deleteButton = Button(self.window, text="Delete", command=self.deleteAgency)
        deleteButton.pack(padx=10, pady=10)

        backButton = Button(self.window, text="Back", command=self.AgencySelectionPage)
        backButton.pack(padx=10, pady=10)

    def viewAgenciesScreen(self):
        self.clearFrame()

        allAgenciesFrame = LabelFrame(self.window, text="All Agencies",bg="#79AC78")
        allAgenciesFrame.pack(padx=20, pady=20)

        success, agencies = self.db_operations.read_all("Agency")
        if success:
            tree = ttk.Treeview(allAgenciesFrame, columns=("ID", "Name", "Address", "Contact", "Expertise"))
            tree.heading("#0", text="", anchor="center") 
            tree.heading("ID", text="ID", anchor="center")
            tree.heading("Name", text="Name", anchor="center")
            tree.heading("Address", text="Address", anchor="center")
            tree.heading("Contact", text="Contact", anchor="center")
            tree.heading("Expertise", text="Expertise", anchor="center")
            
            tree.column("#0", width=0, stretch=NO)
            tree.column("ID", anchor="center", width=80)
            tree.column("Name", anchor="center", width=120)
            tree.column("Address", anchor="center", width=150)
            tree.column("Contact", anchor="center", width=100)
            tree.column("Expertise", anchor="center", width=100)

            for agency in agencies:
                tree.insert("", "end", values=agency)
            
            tree.pack()

        backButton = Button(allAgenciesFrame, text="Back", command=self.AgencySelectionPage)
        backButton.pack(padx=10, pady=10)

    def addAgency(self):
        agency_id = self.idEntry.get()
        agency_name = self.nameEntry.get()
        agency_address = self.addressEntry.get()
        agency_contact = self.contactEntry.get()
        agency_expertise = self.expertiseEntry.get()

        if agency_id and agency_name and agency_address and agency_contact and agency_expertise:
            new_agency = Agency(agency_id, agency_name, agency_address, agency_contact, agency_expertise)

            success, message = self.db_operations.create("Agency", agency_id=agency_id, agency_name=agency_name, agency_address=agency_address, agency_contact=agency_contact, agency_expertise=agency_expertise)
            
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def updateAgency(self, agency_id=None):
     
     if agency_id is None:
        agency_id = self.updateIdEntry.get()
     if agency_id:
        success, agency = self.db_operations.read("Agency", agency_id)
        if success and agency is not None:  # Check if agency data is retrieved successfully and is not None
            self.clearFrame()

            updateAgencyFrame = LabelFrame(self.window, text="Update Agency",bg="#79AC78")
            updateAgencyFrame.pack(padx=350, pady=10)

            idLabel = Label(updateAgencyFrame, text="ID",bg="#79AC78")
            idLabel.grid(row=0, column=0, padx=5, pady=5)
            self.idUpdateEntry = Entry(updateAgencyFrame)
            self.idUpdateEntry.insert(0, agency[0])  # Make sure agency[0] exists and contains the ID
            self.idUpdateEntry.grid(row=0, column=1, padx=5, pady=5)
            self.idUpdateEntry.config(state='disabled')

            nameLabel = Label(updateAgencyFrame, text="Name",bg="#79AC78")
            nameLabel.grid(row=1, column=0, padx=5, pady=5)
            self.nameUpdateEntry = Entry(updateAgencyFrame)
            self.nameUpdateEntry.insert(0, agency[1])
            self.nameUpdateEntry.grid(row=1, column=1, padx=5, pady=5)

            addressLabel = Label(updateAgencyFrame, text="Address",bg="#79AC78")
            addressLabel.grid(row=2, column=0, padx=5, pady=5)
            self.addressUpdateEntry = Entry(updateAgencyFrame)
            self.addressUpdateEntry.insert(0, agency[2])
            self.addressUpdateEntry.grid(row=2, column=1, padx=5, pady=5)

            contactLabel = Label(updateAgencyFrame, text="Contact",bg="#79AC78")
            contactLabel.grid(row=3, column=0, padx=5, pady=5)
            self.contactUpdateEntry = Entry(updateAgencyFrame)
            self.contactUpdateEntry.insert(0, agency[3])
            self.contactUpdateEntry.grid(row=3, column=1, padx=5, pady=5)

            expertiseLabel = Label(updateAgencyFrame, text="Expertise",bg="#79AC78")
            expertiseLabel.grid(row=4, column=0, padx=5, pady=5)
            self.expertiseUpdateEntry = Entry(updateAgencyFrame)
            self.expertiseUpdateEntry.insert(0, agency[4])
            self.expertiseUpdateEntry.grid(row=4, column=1, padx=5, pady=5)

            updateButton = Button(updateAgencyFrame, text="Update Agency", command=lambda: self.performUpdate(agency_id))
            updateButton.grid(row=5, columnspan=2, padx=20, pady=10)

            backButton = Button(updateAgencyFrame, text="Back", command=self.AgencySelectionPage)
            backButton.grid(row=6, columnspan=2, padx=20, pady=10)
        elif not success:
            messagebox.showerror("Error", "Failed to retrieve agency data.")
        else:
            messagebox.showerror("Error", "Agency not found.")
     else:
        messagebox.showerror("Error", "Agency ID is required.")

    def performUpdate(self, agency_id):
        agency_name = self.nameUpdateEntry.get()
        agency_address = self.addressUpdateEntry.get()
        agency_contact = self.contactUpdateEntry.get()
        agency_expertise = self.expertiseUpdateEntry.get()

        if agency_name and agency_address and agency_contact and agency_expertise:
            success, message = self.db_operations.update("Agency", agency_id, agency_name=agency_name, agency_address=agency_address, agency_contact=agency_contact, agency_expertise=agency_expertise)
            if success:
                updated_agency = Agency(agency_id, agency_name, agency_address, agency_contact, agency_expertise)

                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def deleteAgency(self):
        agency_id = self.deleteIdEntry.get()
        if agency_id:
            success, message = self.db_operations.delete("Agency", agency_id)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "Agency ID is required.")

   


    def clearFrame(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def AgencySelectionPage(self):
     self.clearFrame()

  
     optionsFrame = LabelFrame(self.window, text="Options",bg="#79AC78")
     optionsFrame.grid(row=0, column=0, padx=350, pady=10)
     custom_font = font.Font(family="Times New Roman", size=15)



     addAgencyButton = Button(optionsFrame, text='Add Agency',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.addAgencyScreen)
     addAgencyButton.grid(row=0, column=0, padx=100, pady=10)

     updateAgencyButton = Button(optionsFrame, text='Update Agency',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.updateAgencyScreen)
     updateAgencyButton.grid(row=1, column=0, padx=100, pady=10)

     deleteAgencyButton = Button(optionsFrame, text='Delete Agency',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.deleteAgencyScreen)
     deleteAgencyButton.grid(row=0, column=1, padx=100, pady=10)

     viewAgenciesButton = Button(optionsFrame, text='View Agencies',bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=20, pady=20, command=self.viewAgenciesScreen)
     viewAgenciesButton.grid(row=1, column=1, padx=100, pady=10)

     if self.back_callback:
        backButton = Button(optionsFrame, text="Back", command=self.back_callback)
        backButton.grid(row=2, column=0, columnspan=2, pady=10)


     

    

    

if __name__ == "__main__":
    root = Tk()
    app = AgencyManagementSystem(root)
    root.mainloop()
