from tkinter import *
from tkinter import ttk, messagebox
from database_operations import db_ops
from fir import FIR
import mysql.connector
from tkinter import font
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)

class FIRManagementSystem:
    def __init__(self, window, back_callback=None):
        self.window = window
        self.back_callback = back_callback
        self.frame = Frame(self.window,bg="#1a4d2e")
        self.frame.pack(fill=BOTH, expand=True)
        self.db_operations = db_ops(db)

        self.selectionPage()

    def addFIRScreen(self):
        self.clearFrame()
        
        firDetailsFrame = LabelFrame(self.frame, text="Add New FIR",bg="#79AC78")
        firDetailsFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(firDetailsFrame, text="ID",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.idEntry = Entry(firDetailsFrame)
        self.idEntry.grid(row=0, column=1, padx=5, pady=5)

        nameLabel = Label(firDetailsFrame, text="Name",bg="#79AC78")
        nameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.nameEntry = Entry(firDetailsFrame)
        self.nameEntry.grid(row=1, column=1, padx=5, pady=5)

        ageLabel = Label(firDetailsFrame, text="Age",bg="#79AC78")
        ageLabel.grid(row=2, column=0, padx=5, pady=5)
        self.ageEntry = Entry(firDetailsFrame)
        self.ageEntry.grid(row=2, column=1, padx=5, pady=5)

        genderLabel = Label(firDetailsFrame, text="Gender",bg="#79AC78")
        genderLabel.grid(row=3, column=0, padx=5, pady=5)
        self.genderEntry = Entry(firDetailsFrame)
        self.genderEntry.grid(row=3, column=1, padx=5, pady=5)

        addressLabel = Label(firDetailsFrame, text="Address",bg="#79AC78")
        addressLabel.grid(row=4, column=0, padx=5, pady=5)
        self.addressEntry = Entry(firDetailsFrame)
        self.addressEntry.grid(row=4, column=1, padx=5, pady=5)

        contactLabel = Label(firDetailsFrame, text="Contact",bg="#79AC78")
        contactLabel.grid(row=5, column=0, padx=5, pady=5)
        self.contactEntry = Entry(firDetailsFrame)
        self.contactEntry.grid(row=5, column=1, padx=5, pady=5)

        

        relationLabel = Label(firDetailsFrame, text="Relation with Victim",bg="#79AC78")
        relationLabel.grid(row=7, column=0, padx=5, pady=5)
        self.relationEntry = Entry(firDetailsFrame)
        self.relationEntry.grid(row=7, column=1, padx=5, pady=5)

        crimeLabel = Label(firDetailsFrame, text="Crime ID",bg="#79AC78")
        crimeLabel.grid(row=8, column=0, padx=5, pady=5)
        self.crimeEntry = Entry(firDetailsFrame)
        self.crimeEntry.grid(row=8, column=1, padx=5, pady=5)

        addButton = Button(firDetailsFrame, text="Save FIR Details", command=self.addFIR)
        addButton.grid(row=9, columnspan=2, padx=20, pady=10)

        backButton = Button(firDetailsFrame, text="Back", command=self.selectionPage)
        backButton.grid(row=10, columnspan=2, padx=20, pady=10)

    def updateFIRScreen(self):
        self.clearFrame()

        updateIdLabel = Label(self.frame, text="Enter FIR ID to Update:",bg="#79AC78")
        updateIdLabel.pack(padx=350, pady=10)
        self.updateIdEntry = Entry(self.frame)
        self.updateIdEntry.pack(padx=10, pady=10)

        updateButton = Button(self.frame, text="Update", command=lambda: self.updateFIR(self.updateIdEntry.get()))
        updateButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def updateFIR(self, fir_id=None):
     if fir_id is None:
        fir_id = self.updateIdEntry.get()
     if fir_id:
        success, fir = self.db_operations.read("FIR", fir_id)
        if success and fir is not None:
            self.clearFrame()

            updateFIRFrame = LabelFrame(self.frame, text="Update FIR",bg="#79AC78")
            updateFIRFrame.pack(padx=20, pady=10)

            idLabel = Label(updateFIRFrame, text="ID",bg="#79AC78")
            idLabel.grid(row=0, column=0, padx=5, pady=5)
            self.idUpdateEntry = Entry(updateFIRFrame)
            self.idUpdateEntry.insert(0, fir[0])
            self.idUpdateEntry.grid(row=0, column=1, padx=5, pady=5)
            self.idUpdateEntry.config(state='disabled')

            nameLabel = Label(updateFIRFrame, text="Name",bg="#79AC78")
            nameLabel.grid(row=1, column=0, padx=5, pady=5)
            self.nameUpdateEntry = Entry(updateFIRFrame)
            self.nameUpdateEntry.insert(0, fir[1])
            self.nameUpdateEntry.grid(row=1, column=1, padx=5, pady=5)

            ageLabel = Label(updateFIRFrame, text="Age",bg="#79AC78")
            ageLabel.grid(row=2, column=0, padx=5, pady=5)
            self.ageUpdateEntry = Entry(updateFIRFrame)
            self.ageUpdateEntry.insert(0, fir[2])
            self.ageUpdateEntry.grid(row=2, column=1, padx=5, pady=5)

            genderLabel = Label(updateFIRFrame, text="Gender",bg="#79AC78")
            genderLabel.grid(row=3, column=0, padx=5, pady=5)
            self.genderUpdateEntry = Entry(updateFIRFrame)
            self.genderUpdateEntry.insert(0, fir[3])
            self.genderUpdateEntry.grid(row=3, column=1, padx=5, pady=5)

            addressLabel = Label(updateFIRFrame, text="Address",bg="#79AC78")
            addressLabel.grid(row=4, column=0, padx=5, pady=5)
            self.addressUpdateEntry = Entry(updateFIRFrame)
            self.addressUpdateEntry.insert(0, fir[4])
            self.addressUpdateEntry.grid(row=4, column=1, padx=5, pady=5)

            contactLabel = Label(updateFIRFrame, text="Contact",bg="#79AC78")
            contactLabel.grid(row=5, column=0, padx=5, pady=5)
            self.contactUpdateEntry = Entry(updateFIRFrame)
            self.contactUpdateEntry.insert(0, fir[5])
            self.contactUpdateEntry.grid(row=5, column=1, padx=5, pady=5)

            relationLabel = Label(updateFIRFrame, text="Relation with Victim",bg="#79AC78")
            relationLabel.grid(row=6, column=0, padx=5, pady=5)
            self.relationUpdateEntry = Entry(updateFIRFrame)
            self.relationUpdateEntry.insert(0, fir[6])
            self.relationUpdateEntry.grid(row=6, column=1, padx=5, pady=5)

            crimeLabel = Label(updateFIRFrame, text="Crime ID",bg="#79AC78")
            crimeLabel.grid(row=7, column=0, padx=5, pady=5)
            self.crimeUpdateEntry = Entry(updateFIRFrame)
            self.crimeUpdateEntry.insert(0, fir[7])
            self.crimeUpdateEntry.grid(row=7, column=1, padx=5, pady=5)

            updateButton = Button(updateFIRFrame, text="Update FIR", command=lambda: self.performUpdate(fir_id))
            updateButton.grid(row=8, columnspan=2, padx=20, pady=10)

            backButton = Button(updateFIRFrame, text="Back", command=self.selectionPage)
            backButton.grid(row=9, columnspan=2, padx=20, pady=10)
        elif not success:
            messagebox.showerror("Error", "Failed to retrieve FIR data.")
        else:
            messagebox.showerror("Error", "FIR not found.")
     else:
        messagebox.showerror("Error", "FIR ID is required.")
       
    def performUpdate(self, fir_id):
        f_name = self.nameUpdateEntry.get()
        f_age = self.ageUpdateEntry.get()
        f_gender = self.genderUpdateEntry.get()
        f_address = self.addressUpdateEntry.get()
        f_contact = self.contactUpdateEntry.get()
        f_relation_with_victim = self.relationUpdateEntry.get()
        crime_id = self.crimeUpdateEntry.get()

        if f_name and f_age and f_gender and f_address and f_contact and f_relation_with_victim and crime_id:
            updated_fir = FIR(fir_id, f_name, f_age, f_gender, f_address, f_contact, f_relation_with_victim, crime_id)

            success, message = self.db_operations.update("FIR", fir_id, F_name=f_name, F_age=f_age, F_gender=f_gender, F_address=f_address, F_contact=f_contact, F_relation_with_victim=f_relation_with_victim, Crime_id=crime_id)
            if success:
                messagebox.showinfo("Success", "FIR updated successfully.")
                self.selectionPage()
            else:
                messagebox.showerror("Error", f"Failed to update FIR: {message}")
        else:
            messagebox.showerror("Error", "All fields are required.")



    def deleteFIRScreen(self):
        self.clearFrame()

        deleteIdLabel = Label(self.frame, text="Enter FIR ID to Delete:",bg="#79AC78")
        deleteIdLabel.pack(padx=350, pady=10)
        self.deleteIdEntry = Entry(self.frame)
        self.deleteIdEntry.pack(padx=10, pady=10)

        deleteButton = Button(self.frame, text="Delete", command=self.deleteFIR)
        deleteButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def deleteFIR(self):
     fir_id = self.deleteIdEntry.get()
     if fir_id:
        success, message = self.db_operations.delete("FIR", fir_id)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
     else:
        messagebox.showerror("Error", "FIR ID is required.")

    def viewFIRsScreen(self):
     self.clearFrame()

     allFIRsFrame = LabelFrame(self.frame, text="All FIRs",bg="#79AC78")
     allFIRsFrame.pack(padx=20, pady=20)

     success, FIRs = self.db_operations.read_all("FIR")
     if success:
        tree = ttk.Treeview(allFIRsFrame, columns=("ID", "Name", "Age", "Gender", "Address", "Contact", "Relation with Victim", "Crime ID"))
        tree.heading("#0", text="", anchor="center")
        tree.heading("ID", text="ID", anchor="center")
        tree.heading("Name", text="Name", anchor="center")
        tree.heading("Age", text="Age", anchor="center")
        tree.heading("Gender", text="Gender", anchor="center")
        tree.heading("Address", text="Address", anchor="center")
        tree.heading("Contact", text="Contact", anchor="center")
        tree.heading("Relation with Victim", text="Relation with Victim", anchor="center")
        tree.heading("Crime ID", text="Crime ID", anchor="center")

        for fir in FIRs:
            tree.insert("", "end", values=fir)

        tree.pack()

     backButton = Button(allFIRsFrame, text="Back", command=self.selectionPage)
     backButton.pack(padx=10, pady=10)


    

    def addFIR(self):
        fir_id = self.idEntry.get()
        f_name = self.nameEntry.get()
        f_age = self.ageEntry.get()
        f_gender = self.genderEntry.get()
        f_address = self.addressEntry.get()
        f_contact = self.contactEntry.get()
        f_relation_with_victim = self.relationEntry.get()
        crime_id = self.crimeEntry.get()

        if fir_id and f_name and f_age and f_gender and f_address and f_contact and f_relation_with_victim and crime_id:
            new_fir = FIR(fir_id, f_name, f_age, f_gender, f_address, f_contact, f_relation_with_victim, crime_id)

            success, message = self.db_operations.create("FIR", fir_id=fir_id, F_name=f_name, F_age=f_age, F_gender=f_gender, F_address=f_address, F_contact=f_contact, F_relation_with_victim=f_relation_with_victim, Crime_id=crime_id)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def clearFrame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def selectionPage(self):
        self.clearFrame()
        optionsFrame = LabelFrame(self.frame, text="Options",bg="#79AC78")
        optionsFrame.grid(row=0, column=0, padx=350, pady=10)
        custom_font = font.Font(family="Times New Roman", size=15)


        addFIRButton = Button(optionsFrame, text='Add FIR',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.addFIRScreen)
        addFIRButton.grid(row=0,column=0,padx=100, pady=10)

        updateFIRButton = Button(optionsFrame, text='Update FIR',bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=20, pady=20, command=self.updateFIRScreen)
        updateFIRButton.grid(row=1,column=0,padx=100, pady=10)

        deleteFIRButton = Button(optionsFrame, text='Delete FIR', bg="#7AB2B2",fg="black",font=custom_font,height=2, width=15, padx=20, pady=20, command=self.deleteFIRScreen)
        deleteFIRButton.grid(row=0,column=1,padx=100, pady=10)

        viewFIRsButton = Button(optionsFrame, text='View FIRs',bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=20, pady=20, command=self.viewFIRsScreen)
        viewFIRsButton.grid(row=1,column=1,padx=100, pady=10)
        if self.back_callback:
            backButton = Button(optionsFrame, text="Back", command=self.back_callback)
            backButton.grid(row=3, column=1, padx=20, pady=10)

if __name__ == "__main__":
    root = Tk()
    app = FIRManagementSystem(root)
    root.mainloop()
