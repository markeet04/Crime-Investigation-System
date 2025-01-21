from tkinter import *
from tkinter import ttk, messagebox
from database_operations import db_ops
from crime import Crime
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tkinter import font

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)

class CrimeManagementSystem:
    def __init__(self, window, back_callback=None):
        self.window = window
        self.back_callback = back_callback
        self.frame = Frame(self.window,bg="#1a4d2e")
        self.frame.pack(fill=BOTH, expand=True)
        self.db_operations = db_ops(db)
        
        self.selectionPage()
    def clearFrame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def selectionPage(self):
        self.clearFrame()

        optionsFrame = LabelFrame(self.frame, text="Options",bg="#79AC78")
        optionsFrame.grid(row=0, column=0, padx=350, pady=10)
        custom_font = font.Font(family="Times New Roman", size=15)


        addCrimeButton = Button(optionsFrame, text='Add Crime',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.addCrimeScreen)
        addCrimeButton.grid(row=0,column=0,padx=100, pady=10)

        updateCrimeButton = Button(optionsFrame, text='Update Crime',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.updateCrimeScreen)
        updateCrimeButton.grid(row=1,column=0,padx=100, pady=10)

        deleteCrimeButton = Button(optionsFrame, text='Delete Crime',bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=20, pady=20, command=self.deleteCrimeScreen)
        deleteCrimeButton.grid(row=0,column=1,padx=100, pady=10)

        viewCrimesButton = Button(optionsFrame, text='View Crimes', bg="#7AB2B2",fg="black",font=custom_font,height=2, width=15, padx=20, pady=20, command=self.viewCrimesScreen)
        viewCrimesButton.grid(row=1,column=1,padx=100, pady=10)

        plotGraphButton = Button(optionsFrame, text='Plot Graph',bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=20, pady=20, command=self.plotGraph)
        plotGraphButton.grid(row=2,column=0,padx=100, pady=10)
        if self.back_callback:
            backButton = Button(optionsFrame, text="Back", command=self.back_callback)
            backButton.grid(row=3, column=1, padx=20, pady=10)

    def addCrimeScreen(self):
        self.clearFrame()
        
        crimeDetailsFrame = LabelFrame(self.frame, text="Add New Crime",bg="#79AC78")
        crimeDetailsFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(crimeDetailsFrame, text="ID",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.idEntry = Entry(crimeDetailsFrame)
        self.idEntry.grid(row=0, column=1, padx=5, pady=5)

        locationLabel = Label(crimeDetailsFrame, text="Location",bg="#79AC78")
        locationLabel.grid(row=1, column=0, padx=5, pady=5)
        self.locationEntry = Entry(crimeDetailsFrame)
        self.locationEntry.grid(row=1, column=1, padx=5, pady=5)

        datetimeLabel = Label(crimeDetailsFrame, text="Date/Time",bg="#79AC78")
        datetimeLabel.grid(row=2, column=0, padx=5, pady=5)
        self.datetimeEntry = Entry(crimeDetailsFrame)
        self.datetimeEntry.grid(row=2, column=1, padx=5, pady=5)

        typeLabel = Label(crimeDetailsFrame, text="Type",bg="#79AC78")
        typeLabel.grid(row=3, column=0, padx=5, pady=5)
        self.typeEntry = Entry(crimeDetailsFrame)
        self.typeEntry.grid(row=3, column=1, padx=5, pady=5)

        descriptionLabel = Label(crimeDetailsFrame, text="Description",bg="#79AC78")
        descriptionLabel.grid(row=4, column=0, padx=5, pady=5)
        self.descriptionEntry = Entry(crimeDetailsFrame)
        self.descriptionEntry.grid(row=4, column=1, padx=5, pady=5)

        addButton = Button(crimeDetailsFrame, text="Save Crime Details", command=self.addCrime)
        addButton.grid(row=5, columnspan=2, padx=20, pady=10)

        backButton = Button(crimeDetailsFrame, text="Back", command=self.selectionPage)
        backButton.grid(row=6, columnspan=2, padx=20, pady=10)

    def updateCrimeScreen(self):
        self.clearFrame()

        idLabel = Label(self.frame, text="Enter Crime ID to Update:",bg="#79AC78")
        idLabel.pack(padx=350, pady=10)
        self.updateIdEntry = Entry(self.frame)
        self.updateIdEntry.pack(padx=10, pady=10)

        updateButton = Button(self.frame, text="Update", command=self.updateCrime)
        updateButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def deleteCrimeScreen(self):
        self.clearFrame()

        idLabel = Label(self.frame, text="Enter Crime ID to Delete:",bg="#79AC78")
        idLabel.pack(padx=350, pady=10)
        self.deleteIdEntry = Entry(self.frame)
        self.deleteIdEntry.pack(padx=10, pady=10)

        deleteButton = Button(self.frame, text="Delete", command=self.deleteCrime)
        deleteButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def viewCrimesScreen(self):
        self.clearFrame()

        allCrimesFrame = LabelFrame(self.frame, text="All Crimes",bg="#79AC78")
        allCrimesFrame.pack(padx=20, pady=10)

        success, crimes = self.db_operations.read_all("Crime")
        if success:
            tree = ttk.Treeview(allCrimesFrame, columns=("ID", "Location", "Date/Time", "Type", "Description"))
            tree.heading("#0", text="", anchor="center") 
            tree.heading("ID", text="ID", anchor="center")
            tree.heading("Location", text="Location", anchor="center")
            tree.heading("Date/Time", text="Date/Time", anchor="center")
            tree.heading("Type", text="Type", anchor="center")
            tree.heading("Description", text="Description", anchor="center")
            
            for crime in crimes:
                tree.insert("", "end", values=crime)
            
            tree.pack()

        backButton = Button(self.frame, text="Back", command=self.selectionPage)
        backButton.pack(padx=10, pady=10)

    def addCrime(self):
        crime_id = self.idEntry.get()
        crime_location = self.locationEntry.get()  
        crime_datetime = self.datetimeEntry.get()
        crime_type = self.typeEntry.get()
        crime_description = self.descriptionEntry.get()

        if crime_id and crime_location and crime_datetime and crime_type and crime_description:
            new_crime = Crime(None, crime_location, crime_datetime, crime_type, crime_description)

            success, message = self.db_operations.create("Crime", crime_id=crime_id, crime_location=crime_location, crime_datetime=crime_datetime, crime_type=crime_type, crime_description=crime_description)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def updateCrime(self):
        crime_id = self.updateIdEntry.get()
        if crime_id:
            success, crime = self.db_operations.read("Crime", crime_id)
            if success:
                self.clearFrame()

                updateCrimeFrame = LabelFrame(self.frame, text="Update Crime",bg="#79AC78")
                updateCrimeFrame.pack(padx=350, pady=10)

                locationLabel = Label(updateCrimeFrame, text="Location",bg="#79AC78")
                locationLabel.grid(row=0, column=0, padx=5, pady=5)
                self.locationUpdateEntry = Entry(updateCrimeFrame)
                self.locationUpdateEntry.insert(0, crime[1])
                self.locationUpdateEntry.grid(row=0, column=1, padx=5, pady=5)

                datetimeLabel = Label(updateCrimeFrame, text="Date/Time",bg="#79AC78")
                datetimeLabel.grid(row=1, column=0, padx=5, pady=5)
                self.datetimeUpdateEntry = Entry(updateCrimeFrame)
                self.datetimeUpdateEntry.insert(0, crime[2])
                self.datetimeUpdateEntry.grid(row=1, column=1, padx=5, pady=5)

                typeLabel = Label(updateCrimeFrame, text="Type",bg="#79AC78")
                typeLabel.grid(row=2, column=0, padx=5, pady=5)
                self.typeUpdateEntry = Entry(updateCrimeFrame)
                self.typeUpdateEntry.insert(0, crime[3])
                self.typeUpdateEntry.grid(row=2, column=1, padx=5, pady=5)

                descriptionLabel = Label(updateCrimeFrame, text="Description",bg="#79AC78")
                descriptionLabel.grid(row=3, column=0, padx=5, pady=5)
                self.descriptionUpdateEntry = Entry(updateCrimeFrame)
                self.descriptionUpdateEntry.insert(0, crime[4])
                self.descriptionUpdateEntry.grid(row=3, column=1, padx=5, pady=5)

                updateButton = Button(updateCrimeFrame, text="Update Crime", command=lambda: self.performUpdate(crime_id))
                updateButton.grid(row=4, columnspan=2, padx=20, pady=10)

                backButton = Button(updateCrimeFrame, text="Back", command=self.selectionPage)
                backButton.grid(row=5, columnspan=2, padx=20, pady=10)

    def performUpdate(self, crime_id):
        crime_location = self.locationUpdateEntry.get()
        crime_datetime = self.datetimeUpdateEntry.get()
        crime_type = self.typeUpdateEntry.get()
        crime_description = self.descriptionUpdateEntry.get()

        if crime_location and crime_datetime and crime_type and crime_description:
            updated_crime = Crime(crime_id, crime_location, crime_datetime, crime_type, crime_description)

            success, message = self.db_operations.update("Crime", crime_id=crime_id, crime_location=crime_location, crime_datetime=crime_datetime, crime_type=crime_type, crime_description=crime_description)
            if success:
                messagebox.showinfo("Success", message)
                self.selectionPage()
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def deleteCrime(self):
        crime_id = self.deleteIdEntry.get()
        if crime_id:
            success, message = self.db_operations.delete("Crime", crime_id)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "Crime ID is required.")

    def plotGraph(self):
        success, crimes = self.db_operations.read_all("Crime")
        if success:
            # Example data extraction for plotting
            crime_types = {}
            for crime in crimes:
                crime_type = crime[3]  # Assuming crime type is at index 3
                if crime_type in crime_types:
                    crime_types[crime_type] += 1
                else:
                    crime_types[crime_type] = 1

            types = list(crime_types.keys())
            counts = list(crime_types.values())

            fig, ax = plt.subplots()
            bars = ax.bar(types, counts)

            def update(frame):
                for bar, new_height in zip(bars, counts):
                    bar.set_height(new_height)

            ani = FuncAnimation(fig, update, frames=range(1), repeat=False)
            plt.xlabel('Crime Types')
            plt.ylabel('Number of Crimes')
            plt.title('Crime Types vs. Number of Crimes')
            plt.show()

        else:
            messagebox.showerror("Error", "Could not retrieve crime data.")

if __name__ == "__main__":
    root = Tk()
    app = CrimeManagementSystem(root)
    root.mainloop()

