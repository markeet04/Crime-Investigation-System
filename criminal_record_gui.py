from tkinter import *
from tkinter import ttk, messagebox
from database_operations import db_ops
from criminal_record import CriminalRecord
import mysql.connector
from tkinter import font

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)

class CriminalRecordManagementSystem:
    def __init__(self, window, back_callback=None):
        self.window = window
        self.back_callback = back_callback
        self.frame = Frame(self.window,bg="#1a4d2e")
        self.frame.pack(fill=BOTH, expand=True)
        self.db_operations = db_ops(db)
        
        self.selectionPage()

    def addCriminalRecordScreen(self):
        self.clearFrame()
        
        criminalRecordDetailsFrame = LabelFrame(self.frame, text="Add New Criminal Record",bg="#79AC78")
        criminalRecordDetailsFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(criminalRecordDetailsFrame, text="ID",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.crimnalRecordidEntry = Entry(criminalRecordDetailsFrame)
        self.crimnalRecordidEntry.grid(row=0, column=1, padx=5, pady=5)

        nameLabel = Label(criminalRecordDetailsFrame, text="Name",bg="#79AC78")
        nameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.nameEntry = Entry(criminalRecordDetailsFrame)
        self.nameEntry.grid(row=1, column=1, padx=5, pady=5)

        contactLabel = Label(criminalRecordDetailsFrame, text="Contact",bg="#79AC78")
        contactLabel.grid(row=2, column=0, padx=5, pady=5)
        self.contactEntry = Entry(criminalRecordDetailsFrame)
        self.contactEntry.grid(row=2, column=1, padx=5, pady=5)

        addressLabel = Label(criminalRecordDetailsFrame, text="Address",bg="#79AC78")
        addressLabel.grid(row=3, column=0, padx=5, pady=5)
        self.addressEntry = Entry(criminalRecordDetailsFrame)
        self.addressEntry.grid(row=3, column=1, padx=5, pady=5)

        caseIdLabel = Label(criminalRecordDetailsFrame, text="Case ID",bg="#79AC78")
        caseIdLabel.grid(row=4, column=0, padx=5, pady=5)
        self.caseIdEntry = Entry(criminalRecordDetailsFrame)
        self.caseIdEntry.grid(row=4, column=1, padx=5, pady=5)

        articleIdLabel = Label(criminalRecordDetailsFrame, text="Article ID",bg="#79AC78")
        articleIdLabel.grid(row=5, column=0, padx=5, pady=5)
        self.articleIdEntry = Entry(criminalRecordDetailsFrame)
        self.articleIdEntry.grid(row=5, column=1, padx=5, pady=5)

        ageLabel = Label(criminalRecordDetailsFrame, text="Age",bg="#79AC78")
        ageLabel.grid(row=6, column=0, padx=5, pady=5)
        self.ageEntry = Entry(criminalRecordDetailsFrame)
        self.ageEntry.grid(row=6, column=1, padx=5, pady=5)

        genderLabel = Label(criminalRecordDetailsFrame, text="Gender",bg="#79AC78")
        genderLabel.grid(row=7, column=0, padx=5, pady=5)
        self.genderEntry = Entry(criminalRecordDetailsFrame)
        self.genderEntry.grid(row=7, column=1, padx=5, pady=5)

        statusLabel = Label(criminalRecordDetailsFrame, text="Status",bg="#79AC78")
        statusLabel.grid(row=8, column=0, padx=5, pady=5)
        self.statusEntry = Entry(criminalRecordDetailsFrame)
        self.statusEntry.grid(row=8, column=1, padx=5, pady=5)

        addButton = Button(criminalRecordDetailsFrame, text="Save Criminal Record", command=self.addCriminalRecord)
        addButton.grid(row=9, columnspan=2, padx=20, pady=10)

        backButton = Button(criminalRecordDetailsFrame, text="Back", command=self.selectionPage)
        backButton.grid(row=10, columnspan=2, padx=20, pady=10)
    
    def updateCriminalRecordScreen(self):
        self.clearFrame()

        idLabel = Label(self.frame, text="Enter Criminal ID to Update:",bg="#79AC78")
        idLabel.pack(padx=350, pady=10)
        self.updateIdEntry = Entry(self.frame)
        self.updateIdEntry.pack(padx=10, pady=10)

        updateButton = Button(self.frame, text="Update", command=lambda: self.updateCriminalRecord(self.updateIdEntry.get()))
        updateButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)
    

    def deleteCriminalRecordScreen(self):
        self.clearFrame()

        idLabel = Label(self.frame, text="Enter Criminal ID to Delete:",bg="#79AC78")
        idLabel.pack(padx=350, pady=10)
        self.deleteIdEntry = Entry(self.frame)
        self.deleteIdEntry.pack(padx=10, pady=10)

        deleteButton = Button(self.frame, text="Delete", command=self.deleteCriminalRecord)
        deleteButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)
    


    def viewCriminalRecordsScreen(self):
     self.clearFrame()

     allCriminalRecordsFrame = LabelFrame(self.frame, text="All Criminal Records",bg="#79AC78")
     allCriminalRecordsFrame.pack(padx=350, pady=20)

     success, criminalRecord = self.db_operations.read_all("criminalRecord")
     if success:
        tree = ttk.Treeview(allCriminalRecordsFrame, columns=("ID", "Name", "Contact", "Address", "Case ID", "Article ID", "Age", "Gender", "Status"))
        tree.heading("#0", text="", anchor="center")
        tree.heading("ID", text="ID", anchor="center")
        tree.heading("Name", text="Name", anchor="center")
        tree.heading("Contact", text="Contact", anchor="center")
        tree.heading("Address", text="Address", anchor="center")
        tree.heading("Case ID", text="Case ID", anchor="center")
        tree.heading("Article ID", text="Article ID", anchor="center")
        tree.heading("Age", text="Age", anchor="center")
        tree.heading("Gender", text="Gender", anchor="center")
        tree.heading("Status", text="Status", anchor="center")

        tree.column("#0", width=0, stretch=NO)
        tree.column("ID", anchor="center", width=80)
        tree.column("Name", anchor="center", width=120)
        tree.column("Contact", anchor="center", width=100)
        tree.column("Address", anchor="center", width=150)
        tree.column("Case ID", anchor="center", width=100)
        tree.column("Article ID", anchor="center", width=100)
        tree.column("Age", anchor="center", width=60)
        tree.column("Gender", anchor="center", width=80)
        tree.column("Status", anchor="center", width=100)

        for criminalRecord in criminalRecord:
            tree.insert("", "end", values=criminalRecord)

        tree.pack()

     backButton = Button(allCriminalRecordsFrame, text="Back", command=self.selectionPage)
     backButton.pack(padx=10, pady=10)

    def addCriminalRecord(self):
      criminalRecord_id = self.crimnalRecordidEntry.get()
      criminal_name = self.nameEntry.get()
      criminal_contact = self.contactEntry.get()
      criminal_address = self.addressEntry.get()
      case_info_id = self.caseIdEntry.get()
      article_id = self.articleIdEntry.get()
      criminal_age = self.ageEntry.get()
      criminal_gender = self.genderEntry.get()
      criminal_status = self.statusEntry.get()

      if criminalRecord_id and criminal_name and criminal_contact and criminal_address and case_info_id and article_id and criminal_age and criminal_gender and criminal_status:
        new_criminal_record = CriminalRecord(criminalRecord_id, criminal_name, criminal_contact, criminal_address, case_info_id, article_id, criminal_age, criminal_gender, criminal_status)

        success = self.db_operations.create("criminalRecord",criminalRecord_id=criminalRecord_id, criminal_name=criminal_name, criminal_contact=criminal_contact, criminal_address=criminal_address, case_info_id=case_info_id, article_id=article_id, criminal_age=criminal_age, criminal_gender=criminal_gender, criminal_status=criminal_status)

        if success:
            messagebox.showinfo("Success", "Criminal Record added successfully.")
        else:
            messagebox.showerror("Error", "Failed to add Criminal Record.")
      else:
        messagebox.showerror("Error", "All fields are required.")

    def updateCriminalRecord(self, criminalRecord_id=None):
     if criminalRecord_id is None:
        criminalRecord_id = self.updateIdEntry.get()
     if criminalRecord_id:
        success, criminal = self.db_operations.read("criminalRecord", criminalRecord_id)
        if success and criminal is not None:
            self.clearFrame()

            updateCriminalRecordFrame = LabelFrame(self.frame, text="Update Criminal Record",bg="#79AC78")
            updateCriminalRecordFrame.pack(padx=350, pady=10)

            idLabel = Label(updateCriminalRecordFrame, text="ID",bg="#79AC78")
            idLabel.grid(row=0, column=0, padx=5, pady=5)
            self.idUpdateEntry = Entry(updateCriminalRecordFrame)
            self.idUpdateEntry.insert(0, criminal[0])
            self.idUpdateEntry.grid(row=0, column=1, padx=5, pady=5)
            self.idUpdateEntry.config(state='disabled')

            nameLabel = Label(updateCriminalRecordFrame, text="Name",bg="#79AC78")
            nameLabel.grid(row=1, column=0, padx=5, pady=5)
            self.nameUpdateEntry = Entry(updateCriminalRecordFrame)
            self.nameUpdateEntry.insert(0, criminal[1])
            self.nameUpdateEntry.grid(row=1, column=1, padx=5, pady=5)

            contactLabel = Label(updateCriminalRecordFrame, text="Contact",bg="#79AC78")
            contactLabel.grid(row=2, column=0, padx=5, pady=5)
            self.contactUpdateEntry = Entry(updateCriminalRecordFrame)
            self.contactUpdateEntry.insert(0, criminal[2])
            self.contactUpdateEntry.grid(row=2, column=1, padx=5, pady=5)

            addressLabel = Label(updateCriminalRecordFrame, text="Address",bg="#79AC78")
            addressLabel.grid(row=3, column=0, padx=5, pady=5)
            self.addressUpdateEntry = Entry(updateCriminalRecordFrame)
            self.addressUpdateEntry.insert(0, criminal[3])
            self.addressUpdateEntry.grid(row=3, column=1, padx=5, pady=5)

            caseLabel = Label(updateCriminalRecordFrame, text="Case ID",bg="#79AC78")
            caseLabel.grid(row=4, column=0, padx=5, pady=5)
            self.caseIdUpdateEntry = Entry(updateCriminalRecordFrame)
            self.caseIdUpdateEntry.insert(0, criminal[4])
            self.caseIdUpdateEntry.grid(row=4, column=1, padx=5, pady=5)

            articleLabel = Label(updateCriminalRecordFrame, text="Article ID",bg="#79AC78")
            articleLabel.grid(row=5, column=0, padx=5, pady=5)
            self.articleIdUpdateEntry = Entry(updateCriminalRecordFrame)
            self.articleIdUpdateEntry.insert(0, criminal[5])
            self.articleIdUpdateEntry.grid(row=5, column=1, padx=5, pady=5)

            ageLabel = Label(updateCriminalRecordFrame, text="Age",bg="#79AC78")
            ageLabel.grid(row=6, column=0, padx=5, pady=5)
            self.ageUpdateEntry = Entry(updateCriminalRecordFrame)
            self.ageUpdateEntry.insert(0, criminal[6])
            self.ageUpdateEntry.grid(row=6, column=1, padx=5, pady=5)

            genderLabel = Label(updateCriminalRecordFrame, text="Gender",bg="#79AC78")
            genderLabel.grid(row=7, column=0, padx=5, pady=5)
            self.genderUpdateEntry = Entry(updateCriminalRecordFrame)
            self.genderUpdateEntry.insert(0, criminal[7])
            self.genderUpdateEntry.grid(row=7, column=1, padx=5, pady=5)

            statusLabel = Label(updateCriminalRecordFrame, text="Status",bg="#79AC78")
            statusLabel.grid(row=8, column=0, padx=5, pady=5)
            self.statusUpdateEntry = Entry(updateCriminalRecordFrame)
            self.statusUpdateEntry.insert(0, criminal[8])
            self.statusUpdateEntry.grid(row=8, column=1, padx=5, pady=5)

            updateButton = Button(updateCriminalRecordFrame, text="Update Criminal Record", command=lambda: self.performUpdateCriminalRecord(criminalRecord_id))
            updateButton.grid(row=9, columnspan=2, padx=20, pady=10)

            backButton = Button(updateCriminalRecordFrame, text="Back", command=self.selectionPage)
            backButton.grid(row=10, columnspan=2, padx=20, pady=10)
        elif not success:
            messagebox.showerror("Error", "Failed to retrieve criminal record data.")
        else:
            messagebox.showerror("Error", "Criminal record not found.")
     else:
        messagebox.showerror("Error",)
    
    def performUpdateCriminalRecord(self, criminalRecord_id):
     criminal_name = self.nameUpdateEntry.get()
     criminal_age = self.ageUpdateEntry.get()
     criminal_gender = self.genderUpdateEntry.get()
     criminal_contact = self.contactUpdateEntry.get()
     criminal_address = self.addressUpdateEntry.get()
     criminal_status = self.statusUpdateEntry.get()
     case_info_id = self.caseIdUpdateEntry.get()
     article_id = self.articleIdUpdateEntry.get()

     if criminal_name and criminal_age and criminal_gender and criminal_contact and criminal_address and criminal_status and case_info_id and article_id:
        updated_criminal_record = CriminalRecord(criminalRecord_id, criminal_name, criminal_contact, criminal_address, case_info_id, article_id, criminal_age, criminal_gender, criminal_status)

        success, message = self.db_operations.update("criminalRecord", criminalRecord_id, criminal_name=criminal_name, criminal_age=criminal_age, criminal_gender=criminal_gender, criminal_contact=criminal_contact, criminal_address=criminal_address, criminal_status=criminal_status, case_info_id=case_info_id, article_id=article_id)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
     else:
        messagebox.showerror("Error", "All fields are required.")


    def deleteCriminalRecord(self):
     criminalRecord_id = self.deleteIdEntry.get()
     if criminalRecord_id:
        success, message = self.db_operations.delete("criminalRecord", criminalRecord_id)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
     else:
        messagebox.showerror("Error", "Criminal ID is required.")
    


    def clearFrame(self):
     for widget in self.frame.winfo_children():
        widget.destroy()

    def selectionPage(self):
      self.clearFrame()
      custom_font = font.Font(family="Times New Roman", size=15)

      optionsFrame = LabelFrame(self.frame, text="Options",bg="#79AC78")
      optionsFrame.grid(row=0, column=0, padx=350, pady=10)

      addCriminalRecordButton = Button(optionsFrame, text='Add Criminal Record',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=20, padx=20, pady=20, command=self.addCriminalRecordScreen)
      addCriminalRecordButton.grid(row=0,column=0,padx=100, pady=10)

      updateCriminalRecordButton = Button(optionsFrame, text='Update Criminal Record',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=20, padx=20, pady=20, command=self.updateCriminalRecordScreen)
      updateCriminalRecordButton.grid(row=1,column=0,padx=100, pady=10)

      deleteCriminalRecordButton = Button(optionsFrame, text='Delete Criminal Record', bg="#7AB2B2",fg="black",font=custom_font,height=2, width=20, padx=20, pady=20, command=self.deleteCriminalRecordScreen)
      deleteCriminalRecordButton.grid(row=0,column=1,padx=100, pady=10)

      viewCriminalRecordsButton = Button(optionsFrame, text='View Criminal Records',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=20, padx=20, pady=20, command=self.viewCriminalRecordsScreen)
      viewCriminalRecordsButton.grid(row=1,column=1,padx=100, pady=10)
      if self.back_callback:
            backButton = Button(optionsFrame, text="Back", command=self.back_callback)
            backButton.grid(row=3, column=1, padx=20, pady=10)
 
   
if __name__ == "__main__":
    root = Tk()
    app = CriminalRecordManagementSystem(root)
    root.mainloop()
