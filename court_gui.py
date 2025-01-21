from tkinter import *
from tkinter import ttk, messagebox
from database_operations import db_ops
from court import Court
import mysql.connector
from tkinter import font

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)

class CourtManagementSystem:
    def __init__(self, window, back_callback=None):
        self.window = window
        self.back_callback = back_callback
        self.frame = Frame(self.window,bg="#1a4d2e")
        self.frame.pack(fill=BOTH, expand=True)
        self.db_operations = db_ops(db)
        
        self.CourtSelectionPage()

    def addCourtScreen(self):
     self.clearFrame()
    
     courtDetailsFrame = LabelFrame(self.frame, text="Add New Court",bg="#79AC78")
     courtDetailsFrame.grid(row=0, column=0, padx=350, pady=10)

     idLabel = Label(courtDetailsFrame, text="ID",bg="#79AC78")
     idLabel.grid(row=0, column=0, padx=5, pady=5)
     self.idEntry = Entry(courtDetailsFrame)
     self.idEntry.grid(row=0, column=1, padx=5, pady=5)

     nameLabel = Label(courtDetailsFrame, text="Name",bg="#79AC78")
     nameLabel.grid(row=1, column=0, padx=5, pady=5)
     self.nameEntry = Entry(courtDetailsFrame)
     self.nameEntry.grid(row=1, column=1, padx=5, pady=5)

     locationLabel = Label(courtDetailsFrame, text="Location",bg="#79AC78")
     locationLabel.grid(row=2, column=0, padx=5, pady=5)
     self.locationEntry = Entry(courtDetailsFrame)
     self.locationEntry.grid(row=2, column=1, padx=5, pady=5)

     levelLabel = Label(courtDetailsFrame, text="Level",bg="#79AC78")
     levelLabel.grid(row=3, column=0, padx=5, pady=5)
     self.levelEntry = Entry(courtDetailsFrame)
     self.levelEntry.grid(row=3, column=1, padx=5, pady=5)

     addButton = Button(courtDetailsFrame, text="Save Court Details", command=self.addCourt)
     addButton.grid(row=4, columnspan=2, padx=20, pady=10)

     backButton = Button(courtDetailsFrame, text="Back", command=self.CourtSelectionPage)
     backButton.grid(row=5, columnspan=2, padx=20, pady=10)

    def updateCourtScreen(self):
     self.clearFrame()

     idLabel = Label(self.frame, text="Enter Court ID to Update:",bg="#79AC78")
     idLabel.pack(padx=350, pady=10)
     self.updateIdEntry = Entry(self.frame)
     self.updateIdEntry.pack(padx=10, pady=10)

     updateButton = Button(self.frame, text="Update", command=self.updateCourt)
     updateButton.pack(padx=10, pady=10)

     backButton = Button(self.frame, text="Back", command=self.CourtSelectionPage)
     backButton.pack(padx=10, pady=10)

    def deleteCourtScreen(self):
     self.clearFrame()

     idLabel = Label(self.frame, text="Enter Court ID to Delete:",bg="#79AC78")
     idLabel.pack(padx=350, pady=10)
     self.deleteIdEntry = Entry(self.frame)
     self.deleteIdEntry.pack(padx=10, pady=10)

     deleteButton = Button(self.frame, text="Delete", command=self.deleteCourt)
     deleteButton.pack(padx=10, pady=10)

     backButton = Button(self.frame, text="Back", command=self.CourtSelectionPage)
     backButton.pack(padx=10, pady=10)

    def viewCourtsScreen(self):
     self.clearFrame()

     allCourtsFrame = LabelFrame(self.frame, text="All Courts",bg="#79AC78")
     allCourtsFrame.pack(padx=20, pady=20)

     success, courts = self.db_operations.read_all("Court")
     if success:
        tree = ttk.Treeview(allCourtsFrame, columns=("ID", "Name", "Location", "Level"))
        tree.heading("#0", text="", anchor="center") 
        tree.heading("ID", text="ID", anchor="center")
        tree.heading("Name", text="Name", anchor="center")
        tree.heading("Location", text="Location", anchor="center")
        tree.heading("Level", text="Level", anchor="center")
        
        tree.column("#0", width=0, stretch=NO)
        tree.column("ID", anchor="center", width=80)
        tree.column("Name", anchor="center", width=120)
        tree.column("Location", anchor="center", width=150)
        tree.column("Level", anchor="center", width=100)

        for court in courts:
            tree.insert("", "end", values=court)
        
        tree.pack()

     backButton = Button(allCourtsFrame, text="Back", command=self.CourtSelectionPage)
     backButton.pack(padx=10, pady=10)

    def addCourt(self):
     court_id = self.idEntry.get()
     court_name = self.nameEntry.get()
     court_location = self.locationEntry.get()
     court_level = self.levelEntry.get()

     if court_id and court_name and court_location and court_level:
        new_court = Court(None, court_name, court_location, court_level)

        success, message = self.db_operations.create("Court", Court_id=court_id, Court_name=court_name, Court_location=court_location, Court_level=court_level)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
     else:
        messagebox.showerror("Error", "All fields are required.")

    def updateCourt(self):
     court_id = self.updateIdEntry.get()
     if court_id:
        success, court = self.db_operations.read("Court", court_id)
        if success and court is not None:
            self.clearFrame()

            updateCourtFrame = LabelFrame(self.frame, text="Update Court",bg="#79AC78")
            updateCourtFrame.pack(padx=350, pady=10)

            idLabel = Label(updateCourtFrame, text="ID",bg="#79AC78")
            idLabel.grid(row=0, column=0, padx=5, pady=5)
            self.idUpdateEntry = Entry(updateCourtFrame)
            self.idUpdateEntry.insert(0, court[0])  # Make sure court[0] exists and contains the ID
            self.idUpdateEntry.grid(row=0, column=1, padx=5, pady=5)
            self.idUpdateEntry.config(state='disabled')

            nameLabel = Label(updateCourtFrame, text="Name",bg="#79AC78")
            nameLabel.grid(row=1, column=0, padx=5, pady=5)
            self.nameUpdateEntry = Entry(updateCourtFrame)
            self.nameUpdateEntry.insert(0, court[1])
            self.nameUpdateEntry.grid(row=1, column=1, padx=5, pady=5)

            locationLabel = Label(updateCourtFrame, text="Location",bg="#79AC78")
            locationLabel.grid(row=2, column=0, padx=5, pady=5)
            self.locationUpdateEntry = Entry(updateCourtFrame)
            self.locationUpdateEntry.insert(0, court[2])
            self.locationUpdateEntry.grid(row=2, column=1, padx=5, pady=5)

            levelLabel = Label(updateCourtFrame, text="Level",bg="#79AC78")
            levelLabel.grid(row=3, column=0, padx=5, pady=5)
            self.levelUpdateEntry = Entry(updateCourtFrame)
            self.levelUpdateEntry.insert(0, court[3])
            self.levelUpdateEntry.grid(row=3, column=1, padx=5, pady=5)

            updateButton = Button(updateCourtFrame, text="Update Court", command=lambda: self.performUpdate(court_id))
            updateButton.grid(row=4, columnspan=2, padx=20, pady=10)

            backButton = Button(updateCourtFrame, text="Back", command=self.CourtSelectionPage)
            backButton.grid(row=5, columnspan=2, padx=20, pady=10)
        elif not success:
            messagebox.showerror("Error", "Failed to retrieve court data.")
        else:
            messagebox.showerror("Error", "Court not found.")
     else:
        messagebox.showerror("Error", "Court ID is required.")
        
    def performUpdate(self, court_id):
        court_name = self.nameUpdateEntry.get()
        court_location = self.locationUpdateEntry.get()
        court_level = self.levelUpdateEntry.get()

        if court_name and court_location and court_level:
            updated_court = Court(court_id, court_name, court_location, court_level)

            success, message = self.db_operations.update("Court", court_id, Court_name=court_name, Court_location=court_location, Court_level=court_level)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")    

    def deleteCourt(self):
        court_id = self.deleteIdEntry.get()
        if court_id:
            success, message = self.db_operations.delete("Court", court_id)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "Court ID is required.")

    def clearFrame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def CourtSelectionPage(self):
        self.clearFrame()
        custom_font = font.Font(family="Times New Roman", size=15)

        optionsFrame = LabelFrame(self.frame, text="Options",bg="#79AC78")
        optionsFrame.grid(row=0, column=0, padx=350, pady=10)

        addCourtButton = Button(optionsFrame, text='Add Court',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.addCourtScreen)
        addCourtButton.grid(row=0,column=0,padx=100, pady=10)

        updateCourtButton = Button(optionsFrame, text='Update Court', bg="#7AB2B2",fg="black",height=2,font=custom_font, width=15, padx=20, pady=20, command=self.updateCourtScreen)
        updateCourtButton.grid(row=1,column=0,padx=100, pady=10)

        deleteCourtButton = Button(optionsFrame, text='Delete Court',bg="#7AB2B2",fg="black",font=custom_font,height=2, width=15, padx=20, pady=20, command=self.deleteCourtScreen)
        deleteCourtButton.grid(row=0,column=1,padx=100, pady=10)

        viewCourtsButton = Button(optionsFrame, text='View Courts',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.viewCourtsScreen)
        viewCourtsButton.grid(row=1,column=1,padx=100, pady=10)
        if self.back_callback:
            backButton = Button(optionsFrame, text="Back", command=self.back_callback)
            backButton.grid(row=2, column=1, padx=20, pady=10)

if __name__ == "__main__":
    root = Tk()
    app = CourtManagementSystem(root)
    root.mainloop()
