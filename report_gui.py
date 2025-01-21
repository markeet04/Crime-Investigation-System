from tkinter import *
from tkinter import ttk, messagebox
from database_operations import db_ops
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)

class PublicReportSubmission:
    def __init__(self, window, back_callback=None):
        self.window = window
        self.back_callback = back_callback
        self.frame = Frame(self.window,bg="#1a4d2e")
        self.frame.pack(fill=BOTH, expand=True)
        self.db_operations = db_ops(db)

        
        self.createReportForm()

    def createReportForm(self):
        reportFormFrame = LabelFrame(self.frame, text="Submit a Report/Complaint", bg="#79AC78")
        reportFormFrame.grid(row=0, column=0, padx=500, pady=200)

        # Reporter CNIC
        cnicLabel = Label(reportFormFrame, text="Reporter CNIC", bg="#79AC78")
        cnicLabel.grid(row=0, column=0, padx=5, pady=5)
        self.cnicEntry = Entry(reportFormFrame)
        self.cnicEntry.grid(row=0, column=1, padx=5, pady=5)

        # Reporter Name
        nameLabel = Label(reportFormFrame, text="Reporter Name", bg="#79AC78")
        nameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.nameEntry = Entry(reportFormFrame)
        self.nameEntry.grid(row=1, column=1, padx=5, pady=5)

        # Reporter Province
        provinceLabel = Label(reportFormFrame, text="Reporter Province", bg="#79AC78")
        provinceLabel.grid(row=2, column=0, padx=5, pady=5)
        self.provinceCombo = ttk.Combobox(reportFormFrame, values=["Punjab", "Sindh", "Kpk", "Balochistan", "Gilgit"])
        self.provinceCombo.grid(row=2, column=1, padx=5, pady=5)

        # Reporter City
        cityLabel = Label(reportFormFrame, text="Reporter City", bg="#79AC78")
        cityLabel.grid(row=3, column=0, padx=5, pady=5)
        self.cityCombo = ttk.Combobox(reportFormFrame, values=[
            'Lahore', 'Faisalabad', 'Multan', 'Rawalpindi', 'Gujranwala', 'Karachi', 
            'Hyderabad', 'Sukkur', 'Larkana', 'Mirpur Khas', 'Peshawar', 'Mardan', 
            'Abbottabad', 'Swat', 'Kohat', 'Quetta', 'Khuzdar', 'Gwadar', 'Turbat', 
            'Sibi', 'Gilgit', 'Skardu', 'Hunza', 'Nagar', 'Chilas'
        ])
        self.cityCombo.grid(row=3, column=1, padx=5, pady=5)

        # Reporter Contact
        contactLabel = Label(reportFormFrame, text="Reporter Contact", bg="#79AC78")
        contactLabel.grid(row=4, column=0, padx=5, pady=5)
        self.contactEntry = Entry(reportFormFrame)
        self.contactEntry.grid(row=4, column=1, padx=5, pady=5)

        # Reporter Age
        ageLabel = Label(reportFormFrame, text="Reporter Age", bg="#79AC78")
        ageLabel.grid(row=5, column=0, padx=5, pady=5)
        self.ageEntry = Entry(reportFormFrame)
        self.ageEntry.grid(row=5, column=1, padx=5, pady=5)

        # Report Type
        typeLabel = Label(reportFormFrame, text="Report Type", bg="#79AC78")
        typeLabel.grid(row=6, column=0, padx=5, pady=5)
        self.typeEntry = Entry(reportFormFrame)
        self.typeEntry.grid(row=6, column=1, padx=5, pady=5)

        # Report Description
        descriptionLabel = Label(reportFormFrame, text="Report Description", bg="#79AC78")
        descriptionLabel.grid(row=7, column=0, padx=5, pady=5)
        self.descriptionEntry = Text(reportFormFrame, height=5, width=40)
        self.descriptionEntry.grid(row=7, column=1, padx=5, pady=5)

        # Submit Button
        submitButton = Button(reportFormFrame, text="Submit", command=self.submitReport)
        submitButton.grid(row=8, columnspan=2, padx=20, pady=10)
        
        if self.back_callback:
            backButton = Button(reportFormFrame, text="Back", command=self.back_callback)
            backButton.grid(row=9, columnspan=2, pady=10)

    def submitReport(self):
        # Get values from the form
        cnic = self.cnicEntry.get()
        name = self.nameEntry.get()
        province = self.provinceCombo.get()
        city = self.cityCombo.get()
        contact = self.contactEntry.get()
        age = self.ageEntry.get()
        report_type = self.typeEntry.get()
        description = self.descriptionEntry.get("1.0", END).strip()

        # Check if all fields are filled
        if not all([cnic, name, province, city, contact, age, report_type, description]):
            messagebox.showerror("Error", "All fields are required.")
            return

        # Insert the report into the database using db_ops class
        report_data = {
            "Reporter_CNIC": cnic,
            "Reporter_name": name,
            "Reporter_Province": province,
            "Reporter_City": city,
            "Reporter_contact": contact,
            "Reporter_age": age,
            "Report_type": report_type,
            "Report_description": description
        }

        success, message = self.db_operations.create("Report_Complain", **report_data)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

if __name__ == "__main__":
    root = Tk()
    app = PublicReportSubmission(root)
    root.mainloop()