from tkinter import *
from tkinter import ttk, messagebox
from database_operations import db_ops
import mysql.connector
from forensic import Forensic
from tkinter import font

# Database connection
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)

class ForensicManagementSystem:

    def __init__(self, window, back_callback=None):
        self.window = window
        self.back_callback = back_callback
        self.frame = Frame(self.window, bg="#1a4d2e")
        self.frame.pack(fill=BOTH, expand=True)
        self.db_operations = db_ops(db)
        self.ForensicSelectionPage()

    def ForensicSelectionPage(self):
        self.clearFrame()
        optionsFrame = LabelFrame(self.frame, text="Options", bg="#79AC78")
        optionsFrame.grid(row=0, column=0, padx=350, pady=10)
        custom_font = font.Font(family="Times New Roman", size=15)


        addForensicButton = Button(optionsFrame, text='Add Forensic', bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.addForensicScreen)
        addForensicButton.grid(row=0, column=0, padx=100, pady=10)

        updateForensicButton = Button(optionsFrame, text='Update Forensic', bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=20, pady=20, command=self.updateForensicScreen)
        updateForensicButton.grid(row=1, column=0, padx=100, pady=10)

        deleteForensicButton = Button(optionsFrame, text='Delete Forensic', bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=20, pady=20, command=self.deleteForensicScreen)
        deleteForensicButton.grid(row=0, column=1, padx=100, pady=10)

        viewForensicsButton = Button(optionsFrame, text='View Forensics', bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.viewForensicsScreen)
        viewForensicsButton.grid(row=1, column=1, padx=100, pady=10)

        if self.back_callback:
            backButton = Button(optionsFrame, text="Back", command=self.backCallback)
            backButton.grid(row=2, column=0, columnspan=2, pady=10)

    def clearFrame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def addForensicScreen(self):
        self.clearFrame()
        forensicDetailsFrame = LabelFrame(self.frame, text="Add New Forensic",bg="#79AC78")
        forensicDetailsFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(forensicDetailsFrame, text="ID",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.idEntry = Entry(forensicDetailsFrame)
        self.idEntry.grid(row=0, column=1, padx=5, pady=5)

        evidenceIdLabel = Label(forensicDetailsFrame, text="Evidence ID",bg="#79AC78")
        evidenceIdLabel.grid(row=1, column=0, padx=5, pady=5)
        self.evidenceIdEntry = Entry(forensicDetailsFrame)
        self.evidenceIdEntry.grid(row=1, column=1, padx=5, pady=5)

        analystNameLabel = Label(forensicDetailsFrame, text="Analyst Name",bg="#79AC78")
        analystNameLabel.grid(row=2, column=0, padx=5, pady=5)
        self.analystNameEntry = Entry(forensicDetailsFrame)
        self.analystNameEntry.grid(row=2, column=1, padx=5, pady=5)

        analysisDateLabel = Label(forensicDetailsFrame, text="Analysis Date",bg="#79AC78")
        analysisDateLabel.grid(row=3, column=0, padx=5, pady=5)
        self.analysisDateEntry = Entry(forensicDetailsFrame)
        self.analysisDateEntry.grid(row=3, column=1, padx=5, pady=5)

        labLabel = Label(forensicDetailsFrame, text="Lab",bg="#79AC78")
        labLabel.grid(row=4, column=0, padx=5, pady=5)
        self.labEntry = Entry(forensicDetailsFrame)
        self.labEntry.grid(row=4, column=1, padx=5, pady=5)

        resultLabel = Label(forensicDetailsFrame, text="Result",bg="#79AC78")
        resultLabel.grid(row=5, column=0, padx=5, pady=5)
        self.resultEntry = Entry(forensicDetailsFrame)
        self.resultEntry.grid(row=5, column=1, padx=5, pady=5)

        addButton = Button(forensicDetailsFrame, text="Save Forensic Details", command=self.addForensic)
        addButton.grid(row=6, columnspan=2, padx=20, pady=10)

        backButton = Button(forensicDetailsFrame, text="Back", command=self.ForensicSelectionPage)
        backButton.grid(row=7, columnspan=2, padx=20, pady=10)

    def addForensic(self):
        forensic_id = self.idEntry.get()
        evidence_id = self.evidenceIdEntry.get()
        analyst_name = self.analystNameEntry.get()
        analysis_date = self.analysisDateEntry.get()
        lab = self.labEntry.get()
        result = self.resultEntry.get()

        if forensic_id and evidence_id and analyst_name and analysis_date and lab and result:
            new_forensic = Forensic(forensic_id, evidence_id, analyst_name, analysis_date, lab, result)
            success, message = self.db_operations.create("forensic", 
                                                          forensic_id=forensic_id, 
                                                          evidence_id=evidence_id, 
                                                          forensic_analyst_name=analyst_name, 
                                                          forensic_analysis_date=analysis_date, 
                                                          forensic_lab=lab, 
                                                          forensic_analysis_result=result)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def updateForensicScreen(self):
        self.clearFrame()
        idLabel = Label(self.frame, text="Enter Forensic ID to Update:",bg="#79AC78")
        idLabel.pack(padx=350, pady=10)
        self.updateIdEntry = Entry(self.frame)
        self.updateIdEntry.pack(padx=10, pady=10)

        updateButton = Button(self.frame, text="Update", command=lambda: self.updateForensic(self.updateIdEntry.get()))
        updateButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.ForensicSelectionPage)
        backButton.pack(padx=10, pady=10)

    def updateForensic(self, forensic_id=None):
        if forensic_id is None:
            forensic_id = self.updateIdEntry.get()

        if forensic_id:
            forensic_data = Forensic.load_from_database(self.db_operations, forensic_id)
            if forensic_data:
                self.clearFrame()
                forensicDetailsFrame = LabelFrame(self.frame, text="Update Forensic",bg="#79AC78")
                forensicDetailsFrame.grid(row=0, column=0, padx=350, pady=10)

                idLabel = Label(forensicDetailsFrame, text="ID",bg="#79AC78")
                idLabel.grid(row=0, column=0, padx=5, pady=5)
                self.idEntry = Entry(forensicDetailsFrame)
                self.idEntry.insert(0, forensic_data[0])
                self.idEntry.grid(row=0, column=1, padx=5, pady=5)

                evidenceIdLabel = Label(forensicDetailsFrame, text="Evidence ID",bg="#79AC78")
                evidenceIdLabel.grid(row=1, column=0, padx=5, pady=5)
                self.evidenceIdEntry = Entry(forensicDetailsFrame)
                self.evidenceIdEntry.insert(0, forensic_data[1])
                self.evidenceIdEntry.grid(row=1, column=1, padx=5, pady=5)

                analystNameLabel = Label(forensicDetailsFrame, text="Analyst Name",bg="#79AC78")
                analystNameLabel.grid(row=2, column=0, padx=5, pady=5)
                self.analystNameEntry = Entry(forensicDetailsFrame)
                self.analystNameEntry.insert(0, forensic_data[2])
                self.analystNameEntry.grid(row=2, column=1, padx=5, pady=5)

                analysisDateLabel = Label(forensicDetailsFrame, text="Analysis Date",bg="#79AC78")
                analysisDateLabel.grid(row=3, column=0, padx=5, pady=5)
                self.analysisDateEntry = Entry(forensicDetailsFrame)
                self.analysisDateEntry.insert(0, forensic_data[3])
                self.analysisDateEntry.grid(row=3, column=1, padx=5, pady=5)

                labLabel = Label(forensicDetailsFrame, text="Lab",bg="#79AC78")
                labLabel.grid(row=4, column=0, padx=5, pady=5)
                self.labEntry = Entry(forensicDetailsFrame)
                self.labEntry.insert(0, forensic_data[4])
                self.labEntry.grid(row=4, column=1, padx=5, pady=5)

                resultLabel = Label(forensicDetailsFrame, text="Result",bg="#79AC78")
                resultLabel.grid(row=5, column=0, padx=5, pady=5)
                self.resultEntry = Entry(forensicDetailsFrame)
                self.resultEntry.insert(0, forensic_data[5])
                self.resultEntry.grid(row=5, column=1, padx=5, pady=5)

                updateButton = Button(forensicDetailsFrame, text="Save Changes", command=self.saveUpdatedForensic)
                updateButton.grid(row=6, columnspan=2, padx=20, pady=10)

                backButton = Button(forensicDetailsFrame, text="Back", command=self.ForensicSelectionPage)
                backButton.grid(row=7, columnspan=2, padx=20, pady=10)
            else:
                messagebox.showerror("Error", "Forensic record not found.")
        else:
            messagebox.showerror("Error", "Forensic ID is required.")

    def saveUpdatedForensic(self):
        forensic_id = self.idEntry.get()
        evidence_id = self.evidenceIdEntry.get()
        analyst_name = self.analystNameEntry.get()
        analysis_date = self.analysisDateEntry.get()
        lab = self.labEntry.get()
        result = self.resultEntry.get()

        if forensic_id and evidence_id and analyst_name and analysis_date and lab and result:
            updated_forensic = Forensic(forensic_id, evidence_id, analyst_name, analysis_date, lab, result)
            success, message = self.db_operations.update("forensic", forensic_id, 
                                                          forensic_id=forensic_id, 
                                                          evidence_id=evidence_id, 
                                                          forensic_analyst_name=analyst_name, 
                                                          forensic_analysis_date=analysis_date, 
                                                          forensic_lab=lab, 
                                                          forensic_analysis_result=result)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def deleteForensicScreen(self):
        self.clearFrame()
        idLabel = Label(self.frame, text="Enter Forensic ID to Delete:",bg="#79AC78")
        idLabel.pack(padx=10, pady=10)
        self.deleteIdEntry = Entry(self.frame)
        self.deleteIdEntry.pack(padx=10, pady=10)

        deleteButton = Button(self.frame, text="Delete", command=self.deleteForensic)
        deleteButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.ForensicSelectionPage)
        backButton.pack(padx=10, pady=10)

    def deleteForensic(self):
        forensic_id = self.deleteIdEntry.get()
        if forensic_id:
            success, message = self.db_operations.delete("forensic", forensic_id)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "Forensic ID is required.")

    def viewForensicsScreen(self):
        self.clearFrame()
        forensicDataFrame = LabelFrame(self.frame, text="All Forensics",bg="#79AC78")
        forensicDataFrame.grid(row=0, column=0, padx=350, pady=10)

        columns = ("forensic_id", "evidence_id", "analyst_name", "analysis_date", "lab", "result")
        self.tree = ttk.Treeview(forensicDataFrame, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.grid(row=0, column=0, sticky='nsew')
            self.tree.column(col, width=100)

        scrollbar = ttk.Scrollbar(forensicDataFrame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        success, records = self.db_operations.read_all("forensic")
        if success:
            for record in records:
                self.tree.insert('', 'end', values=record)
        else:
            messagebox.showerror("Error", records)

        backButton = Button(forensicDataFrame, text="Back", command=self.ForensicSelectionPage)
        backButton.grid(row=1, column=0, padx=20, pady=10)

    def backCallback(self):
        if self.back_callback:
            self.back_callback()

if __name__ == "__main__":
    root = Tk()
    root.title("Forensic Management System")
    root.geometry("800x600")
    app = ForensicManagementSystem(root)
    root.mainloop()
