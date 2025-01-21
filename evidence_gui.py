from tkinter import *
from tkinter import ttk, messagebox
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

class EvidenceManagementSystem:
    def __init__(self, window, back_callback=None):
        self.window = window
        self.back_callback = back_callback
        self.frame = Frame(self.window)
        self.frame.pack(fill=BOTH, expand=True)
        
        self.db_operations = db_ops(db)

        self.evidenceSelectionPage()

    def evidenceSelectionPage(self):
        self.clearFrame()

        optionsFrame = LabelFrame(self.window, text="Options",bg="#79AC78")
        optionsFrame.pack(padx=350, pady=5)
        custom_font = font.Font(family="Times New Roman", size=15)


        addEvidenceButton = Button(optionsFrame, text='Add Evidence',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.addEvidenceScreen)
        addEvidenceButton.grid(row=0,column=0,padx=100, pady=10)

        updateEvidenceButton = Button(optionsFrame, text='Update Evidence',bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=20, pady=20, command=self.updateEvidenceScreen)
        updateEvidenceButton.grid(row=1,column=0,padx=100, pady=10)

        deleteEvidenceButton = Button(optionsFrame, text='Delete Evidence',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.deleteEvidenceScreen)
        deleteEvidenceButton.grid(row=0,column=1,padx=100, pady=10)

        viewEvidenceButton = Button(optionsFrame, text='View Evidence',bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=20, pady=20, command=self.viewEvidenceScreen)
        viewEvidenceButton.grid(row=1,column=1,padx=100, pady=10)
        
        backButton = Button(optionsFrame, text="Back", command=self.back_callback)
        backButton.grid(row=4, column=1, padx=20, pady=10)

    def addEvidenceScreen(self):
        self.clearFrame()
        
        evidenceDetailsFrame = LabelFrame(self.window, text="Add New Evidence",bg="#79AC78")
        evidenceDetailsFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(evidenceDetailsFrame, text="Evidence ID",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.idEntry = Entry(evidenceDetailsFrame)
        self.idEntry.grid(row=0, column=1, padx=5, pady=5)

        caseIdLabel = Label(evidenceDetailsFrame, text="Case ID",bg="#79AC78")
        caseIdLabel.grid(row=1, column=0, padx=5, pady=5)
        self.caseIdEntry = Entry(evidenceDetailsFrame)
        self.caseIdEntry.grid(row=1, column=1, padx=5, pady=5)

        typeLabel = Label(evidenceDetailsFrame, text="Type",bg="#79AC78")
        typeLabel.grid(row=2, column=0, padx=5, pady=5)
        self.typeEntry = Entry(evidenceDetailsFrame)
        self.typeEntry.grid(row=2, column=1, padx=5, pady=5)

        descriptionLabel = Label(evidenceDetailsFrame, text="Description",bg="#79AC78")
        descriptionLabel.grid(row=3, column=0, padx=5, pady=5)
        self.descriptionEntry = Text(evidenceDetailsFrame, height=5, width=30)
        self.descriptionEntry.grid(row=3, column=1, padx=5, pady=5)

        addButton = Button(evidenceDetailsFrame, text="Save Evidence Details", command=self.addEvidence)
        addButton.grid(row=4, columnspan=2, padx=20, pady=10)

        backButton = Button(evidenceDetailsFrame, text="Back", command=self.evidenceSelectionPage)
        backButton.grid(row=5, columnspan=2, padx=20, pady=10)

    def updateEvidenceScreen(self):
        self.clearFrame()

        updateEvidenceFrame = LabelFrame(self.window, text="Update Evidence",bg="#79AC78")
        updateEvidenceFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(updateEvidenceFrame, text="Evidence ID to Update",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.updateIdEntry = Entry(updateEvidenceFrame)
        self.updateIdEntry.grid(row=0, column=1, padx=5, pady=5)

        updateButton = Button(updateEvidenceFrame, text="Update", command=self.updateEvidence)
        updateButton.grid(row=1, columnspan=2, padx=10, pady=10)

        backButton = Button(updateEvidenceFrame, text="Back", command=self.evidenceSelectionPage)
        backButton.grid(row=2, columnspan=2, padx=10, pady=10)

    def updateEvidence(self):
        evidence_id = self.updateIdEntry.get()
        if evidence_id:
            success, evidence = self.db_operations.read("evidence", evidence_id)
            if success:
                self.clearFrame()

                updateEvidenceFrame = LabelFrame(self.frame, text="Update Evidence",bg="#79AC78")
                updateEvidenceFrame.grid(row=0, column=0, padx=350, pady=10)

                caseIdLabel = Label(updateEvidenceFrame, text="Case ID",bg="#79AC78")
                caseIdLabel.grid(row=0, column=0, padx=5, pady=5)
                self.caseIdUpdateEntry = Entry(updateEvidenceFrame)
                self.caseIdUpdateEntry.insert(0, evidence[1])
                self.caseIdUpdateEntry.grid(row=0, column=1, padx=5, pady=5)

                typeLabel = Label(updateEvidenceFrame, text="Type",bg="#79AC78")
                typeLabel.grid(row=1, column=0, padx=5, pady=5)
                self.typeUpdateEntry = Entry(updateEvidenceFrame)
                self.typeUpdateEntry.insert(0, evidence[2])
                self.typeUpdateEntry.grid(row=1, column=1, padx=5, pady=5)

                descriptionLabel = Label(updateEvidenceFrame, text="Description",bg="#79AC78")
                descriptionLabel.grid(row=2, column=0, padx=5, pady=5)
                self.descriptionUpdateEntry = Text(updateEvidenceFrame, height=5, width=30)
                self.descriptionUpdateEntry.insert(END, evidence[3])
                self.descriptionUpdateEntry.grid(row=2, column=1, padx=5, pady=5)

                updateButton = Button(updateEvidenceFrame, text="Update Evidence", command=lambda: self.performUpdate(evidence_id))
                updateButton.grid(row=3, columnspan=2, padx=20, pady=10)

                backButton = Button(updateEvidenceFrame, text="Back", command=self.evidenceSelectionPage)
                backButton.grid(row=4, columnspan=2, padx=20, pady=10)
            else:
                messagebox.showerror("Error", "Evidence not found.")
        else:
            messagebox.showerror("Error", "Evidence ID is required.")

    def deleteEvidenceScreen(self):
        self.clearFrame()

        deleteEvidenceFrame = LabelFrame(self.window, text="Delete Evidence",bg="#79AC78")
        deleteEvidenceFrame.grid(row=0, column=0, padx=350, pady=10)

        idLabel = Label(deleteEvidenceFrame, text="Evidence ID to Delete",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.deleteIdEntry = Entry(deleteEvidenceFrame)
        self.deleteIdEntry.grid(row=0, column=1, padx=5, pady=5)

        deleteButton = Button(deleteEvidenceFrame, text="Delete", command=self.deleteEvidence)
        deleteButton.grid(row=1, columnspan=2, padx=10, pady=10)

        backButton = Button(deleteEvidenceFrame, text="Back", command=self.evidenceSelectionPage)
        backButton.grid(row=2, columnspan=2, padx=10, pady=10)

    def viewEvidenceScreen(self):
        self.clearFrame()

        allEvidenceFrame = LabelFrame(self.window, text="All Evidence",bg="#79AC78")
        allEvidenceFrame.grid(row=0, column=0, padx=350, pady=10)

        success, evidences = self.db_operations.read_all("evidence")
        if success:
            tree = ttk.Treeview(allEvidenceFrame, columns=("Evidence ID", "Case ID", "Type", "Description"), show="headings")
            tree.heading("Evidence ID", text="Evidence ID")
            tree.heading("Case ID", text="Case ID")
            tree.heading("Type", text="Type")
            tree.heading("Description", text="Description")
            
            for evidence in evidences:
                tree.insert("", "end", values=(evidence[0], evidence[1], evidence[2], evidence[3]))
            
            tree.pack()

        backButton = Button(allEvidenceFrame, text="Back", command=self.evidenceSelectionPage)
        backButton.pack(pady=10)

    def clearFrame(self):
        try:
            for widget in self.window.winfo_children():
                widget.destroy()
        except Exception as e:
            print(f"Error in clearFrame: {str(e)}")

    def addEvidence(self):
        evidence_id = self.idEntry.get()
        case_id = self.caseIdEntry.get()
        type = self.typeEntry.get()
        description = self.descriptionEntry.get("1.0", "end-1c")

        if evidence_id and case_id and type and description:
            success, message = self.db_operations.create("evidence", Evidence_id=evidence_id, case_info_id=case_id, Evidence_type=type, Evidence_found_location=description)
            if success:
                messagebox.showinfo("Success", message)
                self.clearEntries([self.idEntry, self.caseIdEntry, self.typeEntry, self.descriptionEntry])
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def performUpdate(self, evidence_id):
        case_id = self.caseIdUpdateEntry.get()
        type = self.typeUpdateEntry.get()
        description = self.descriptionUpdateEntry.get("1.0", "end-1c")

        if case_id and type and description:
            success, message = self.db_operations.update("evidence", evidence_id, case_id=case_id, type=type, description=description)
            if success:
                messagebox.showinfo("Success", message)
                self.clearEntries([self.caseIdUpdateEntry, self.typeUpdateEntry, self.descriptionUpdateEntry])
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def deleteEvidence(self):
        evidence_id = self.deleteIdEntry.get()
        if evidence_id:
            success, message = self.db_operations.delete("evidence", evidence_id)
            if success:
                messagebox.showinfo("Success", message)
                self.deleteIdEntry.delete(0, END)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "Evidence ID is required.")

    def clearEntries(self, entries):
        for entry in entries:
            if isinstance(entry, Entry):
                entry.delete(0, END)
            elif isinstance(entry, Text):
                entry.delete("1.0", END)

if __name__ == "__main__":
    root = Tk()
    app = EvidenceManagementSystem(root)
    root.mainloop()
