from tkinter import *
from tkinter import ttk, messagebox,font
import mysql.connector
from database_operations import db_ops, DatabaseModel
from case import Case_info
from victim_gui import *
from witness_gui import *
from suspect_gui import *
from evidence_gui import *



# Establishing a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)

class CaseManagementSystem:
    def __init__(self, window, back_callback=None):
     self.window = window
     self.back_callback = back_callback
     self.frame = Frame(self.window,bg="#1a4d2e")
     self.frame.pack(fill=BOTH, expand=True)
     self.db_operations = db_ops(db)
     
     self.CaseSelectionPage()
       


    def addCaseScreen(self):
        self.clearFrame()
        
        caseDetailsFrame = LabelFrame(self.frame, text="Add New Case",bg="#79AC78")
        caseDetailsFrame.grid(row=0, column=0, padx=20, pady=10)

        idLabel = Label(caseDetailsFrame, text="Case ID",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.idEntry = Entry(caseDetailsFrame)
        self.idEntry.grid(row=0, column=1, padx=5, pady=5)

        firIdLabel = Label(caseDetailsFrame, text="FIR ID",bg="#79AC78")
        firIdLabel.grid(row=1, column=0, padx=5, pady=5)
        self.firIdEntry = Entry(caseDetailsFrame)
        self.firIdEntry.grid(row=1, column=1, padx=5, pady=5)

        

        nameLabel = Label(caseDetailsFrame, text="Case Name",bg="#79AC78")
        nameLabel.grid(row=2, column=0, padx=5, pady=5)
        self.nameEntry = Entry(caseDetailsFrame)
        self.nameEntry.grid(row=2, column=1, padx=5, pady=5)

        typeLabel = Label(caseDetailsFrame, text="Case Type",bg="#79AC78")
        typeLabel.grid(row=3, column=0, padx=5, pady=5)
        self.typeEntry = Entry(caseDetailsFrame)
        self.typeEntry.grid(row=3, column=1, padx=5, pady=5)

        statusLabel = Label(caseDetailsFrame, text="Case Status",bg="#79AC78")
        statusLabel.grid(row=4, column=0, padx=5, pady=5)
        self.statusEntry = Entry(caseDetailsFrame)
        self.statusEntry.grid(row=4, column=1, padx=5, pady=5)

        openedLabel = Label(caseDetailsFrame, text="Case Opened",bg="#79AC78")
        openedLabel.grid(row=5, column=0, padx=5, pady=5)
        self.openedEntry = Entry(caseDetailsFrame)
        self.openedEntry.grid(row=5, column=1, padx=5, pady=5)

        closedLabel = Label(caseDetailsFrame, text="Case Closed",bg="#79AC78")
        closedLabel.grid(row=6, column=0, padx=5, pady=5)
        self.closedEntry = Entry(caseDetailsFrame)
        self.closedEntry.grid(row=6, column=1, padx=5, pady=5)

        remarksLabel = Label(caseDetailsFrame, text="Case Remarks",bg="#79AC78")
        remarksLabel.grid(row=7, column=0, padx=5, pady=5)
        self.remarksEntry = Entry(caseDetailsFrame)
        self.remarksEntry.grid(row=7, column=1, padx=5, pady=5)

        chargesLabel = Label(caseDetailsFrame, text="Charges Filed",bg="#79AC78")
        chargesLabel.grid(row=8, column=0, padx=5, pady=5)
        self.chargesEntry = Entry(caseDetailsFrame)
        self.chargesEntry.grid(row=8, column=1, padx=5, pady=5)

        addButton = Button(caseDetailsFrame, text="Save Case Details", command=self.addCase)
        addButton.grid(row=9, columnspan=2, padx=20, pady=10)

        backButton = Button(caseDetailsFrame, text="Back", command=self.CaseSelectionPage)
        backButton.grid(row=10, columnspan=2, padx=20, pady=10)

    def updateCaseScreen(self):
        self.clearFrame()

        updateIdLabel = Label(self.frame, text="Enter Case ID to Update:",bg="#79AC78")
        updateIdLabel.pack(padx=10, pady=10)
        self.updateIdEntry = Entry(self.frame)
        self.updateIdEntry.pack(padx=10, pady=10)

        updateButton = Button(self.frame, text="Update", command=lambda: self.updateCase(self.updateIdEntry.get()))
        updateButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.CaseSelectionPage)
        backButton.pack(padx=10, pady=10)

    def updateCase(self, case_info_id=None):
        if case_info_id is None:
            case_info_id = self.updateIdEntry.get()
        if case_info_id:
            success, case = self.db_operations.read("Case_info", case_info_id)
            if success and case is not None:
                self.clearFrame()

                updateCaseFrame = LabelFrame(self.frame, text="Update Case",bg="#79AC78")
                updateCaseFrame.pack(padx=20, pady=10)

                idLabel = Label(updateCaseFrame, text="Case ID",bg="#79AC78")
                idLabel.grid(row=0, column=0, padx=5, pady=5)
                self.idUpdateEntry = Entry(updateCaseFrame)
                self.idUpdateEntry.insert(0, case[0])
                self.idUpdateEntry.grid(row=0, column=1, padx=5, pady=5)
                self.idUpdateEntry.config(state='disabled')

                firIdLabel = Label(updateCaseFrame, text="FIR ID",bg="#79AC78")
                firIdLabel.grid(row=1, column=0, padx=5, pady=5)
                self.firIdUpdateEntry = Entry(updateCaseFrame)
                self.firIdUpdateEntry.insert(0, case[1])
                self.firIdUpdateEntry.grid(row=1, column=1, padx=5, pady=5)

                

                nameLabel = Label(updateCaseFrame, text="Case Name",bg="#79AC78")
                nameLabel.grid(row=2, column=0, padx=5, pady=5)
                self.nameUpdateEntry = Entry(updateCaseFrame)
                self.nameUpdateEntry.insert(0, case[2])
                self.nameUpdateEntry.grid(row=2, column=1, padx=5, pady=5)

                typeLabel = Label(updateCaseFrame, text="Case Type",bg="#79AC78")
                typeLabel.grid(row=3, column=0, padx=5, pady=5)
                self.typeUpdateEntry = Entry(updateCaseFrame)
                self.typeUpdateEntry.insert(0, case[3])
                self.typeUpdateEntry.grid(row=3, column=1, padx=5, pady=5)

                statusLabel = Label(updateCaseFrame, text="Case Status",bg="#79AC78")
                statusLabel.grid(row=4, column=0, padx=5, pady=5)
                self.statusUpdateEntry = Entry(updateCaseFrame)
                self.statusUpdateEntry.insert(0, case[4])
                self.statusUpdateEntry.grid(row=4, column=1, padx=5, pady=5)

                openedLabel = Label(updateCaseFrame, text="Case Opened",bg="#79AC78")
                openedLabel.grid(row=5, column=0, padx=5, pady=5)
                self.openedUpdateEntry = Entry(updateCaseFrame)
                self.openedUpdateEntry.insert(0, case[5])
                self.openedUpdateEntry.grid(row=5, column=1, padx=5, pady=5)

                closedLabel = Label(updateCaseFrame, text="Case Closed",bg="#79AC78")
                closedLabel.grid(row=6, column=0, padx=5, pady=5)
                self.closedUpdateEntry = Entry(updateCaseFrame)
                self.closedUpdateEntry.insert(0, case[6])
                self.closedUpdateEntry.grid(row=6, column=1, padx=5, pady=5)

                remarksLabel = Label(updateCaseFrame, text="Case Remarks",bg="#79AC78")
                remarksLabel.grid(row=7, column=0, padx=5, pady=5)
                self.remarksUpdateEntry = Entry(updateCaseFrame)
                self.remarksUpdateEntry.insert(0, case[7])
                self.remarksUpdateEntry.grid(row=7, column=1, padx=5, pady=5)

                chargesLabel = Label(updateCaseFrame, text="Charges Filed",bg="#79AC78")
                chargesLabel.grid(row=8, column=0, padx=5, pady=5)
                self.chargesUpdateEntry = Entry(updateCaseFrame)
                self.chargesUpdateEntry.insert(0, case[8])
                self.chargesUpdateEntry.grid(row=8, column=1, padx=5, pady=5)

                updateButton = Button(updateCaseFrame, text="Update Case", command=lambda: self.performUpdate(case_info_id))
                updateButton.grid(row=9, columnspan=2, padx=20, pady=10)

                backButton = Button(updateCaseFrame, text="Back", command=self.CaseSelectionPage)
                backButton.grid(row=10, columnspan=2, padx=20, pady=10)
            else:
                messagebox.showerror("Error", "Case not found.")
        else:
            messagebox.showerror("Error", "Case ID is required.")

    def deleteCaseScreen(self):
        self.clearFrame()

        deleteIdLabel = Label(self.frame, text="Enter Case ID to Delete:",bg="#79AC78")
        deleteIdLabel.pack(padx=10, pady=10)
        self.deleteIdEntry = Entry(self.frame)
        self.deleteIdEntry.pack(padx=10, pady=10)

        deleteButton = Button(self.frame, text="Delete", command=lambda: self.deleteCase(self.deleteIdEntry.get()))
        deleteButton.pack(padx=10, pady=10)

        backButton = Button(self.frame, text="Back", command=self.CaseSelectionPage)
        backButton.pack(padx=10, pady=10)

    def deleteCase(self, case_info_id):
        if case_info_id:
            success = self.db_operations.delete("Case_info", case_info_id)
            if success:
                messagebox.showinfo("Success", "Case deleted successfully.")
            else:
                messagebox.showerror("Error", "Failed to delete case.")
        else:
            messagebox.showerror("Error", "Case ID is required.")

    def viewCasesScreen(self):
        self.clearFrame()
        
        viewCaseFrame = LabelFrame(self.frame, text="Cases",bg="#79AC78")
        viewCaseFrame.pack(padx=20, pady=10)

        success, cases = self.db_operations.read_all("Case_info")
        if success:


         tree = ttk.Treeview (viewCaseFrame, columns=("case_info_id", "fir_id", "case_name", "case_type", "case_status", "case_opened", "case_closed", "case_remarks", "charges_filed"))
         tree.heading("#0", text="", anchor="center") 
         tree.heading("case_info_id", text="Case ID",anchor="center")
         tree.heading("fir_id", text="FIR ID",anchor="center")
         tree.heading("case_name", text="Case Name",anchor="center")
         tree.heading("case_type", text="Case Type",anchor="center")
         tree.heading("case_status", text="Case Status",anchor="center")
         tree.heading("case_opened", text="Case Opened",anchor="center")
         tree.heading("case_closed", text="Case Closed",anchor="center")
         tree.heading("case_remarks", text="Case Remarks",anchor="center")
         tree.heading("charges_filed", text="Charges Filed",anchor="center")

         tree.column("#0", width=0, stretch=NO)
         tree.column("case_info_id", anchor="center", width=80)
         tree.column("fir_id",anchor="center",width=90)
         tree.column("case_name", anchor="center", width=120)
         tree.column("case_type", anchor="center", width=150)
         tree.column("case_status", anchor="center", width=100)
         tree.column("case_opened", anchor="center", width=100)
         tree.column("case_closed", anchor="center", width=100)
         tree.column("case_remarks", anchor="center", width=100)
         tree.column("charges_filed", anchor="center", width=100)   

         for case in cases:
            tree.insert("", "end", values=case)
        tree.pack()


        backButton = Button(viewCaseFrame, text="Back", command=self.CaseSelectionPage)
        backButton.pack(padx=10, pady=10)

    def addCase(self):
        case_info_id = self.idEntry.get()
        fir_id = self.firIdEntry.get()
        case_name = self.nameEntry.get()
        case_type = self.typeEntry.get()
        case_status = self.statusEntry.get()
        case_opened = self.openedEntry.get()
        case_closed = self.closedEntry.get()
        case_remarks = self.remarksEntry.get()
        charges_filed = self.chargesEntry.get()

        if case_info_id and fir_id  and case_name and case_type and case_status and case_opened and case_closed and case_remarks and charges_filed:
            new_case = Case_info(None, fir_id, case_name, case_type, case_status, case_opened, case_closed, case_remarks, charges_filed)

            success = self.db_operations.create("Case_info",case_info_id=case_info_id,fir_id=fir_id,case_name=case_name,case_type=case_type,case_status=case_status,case_opened=case_opened,case_closed=case_closed,case_remarks=case_remarks,charges_filed=charges_filed)
            if success:
                messagebox.showinfo("Success", "Case added successfully.")
               
            else:
                messagebox.showerror("Error", "Failed to add case.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def performUpdate(self, case_info_id):
     fir_id = self.firIdUpdateEntry.get()
     case_name = self.nameUpdateEntry.get()
     case_type = self.typeUpdateEntry.get()
     case_status = self.statusUpdateEntry.get()
     case_opened = self.openedUpdateEntry.get()
     case_closed = self.closedUpdateEntry.get()
     case_remarks = self.remarksUpdateEntry.get()
     charges_filed = self.chargesUpdateEntry.get()
     if fir_id and case_name and case_type and case_status and case_opened and case_closed and case_remarks and charges_filed:
        updated_case = Case_info(case_info_id, fir_id, case_name, case_type, case_status, case_opened, case_closed, case_remarks, charges_filed)

        success = self.db_operations.update("Case_info", record_id=case_info_id, case_info_id=case_info_id, fir_id=fir_id, case_name=case_name, case_type=case_type, case_status=case_status, case_opened=case_opened, case_closed=case_closed, charges_filed=charges_filed)
        if success:
            messagebox.showinfo("Success", "Case updated successfully.")
        else:
            messagebox.showerror("Error", "Failed to update case.")
     else:
        messagebox.showerror("Error", "All fields are required.")



        messagebox.showerror("Error", "All fields are required.")



    def showVictimManagement(self):
        self.clearFrame()
        self.victim_management = VictimManagementSystem(self.frame, self.CaseSelectionPage)

     
    def showWitnessManagement(self):
        self.clearFrame()
        self.witness_management = WitnessManagementSystem(self.frame,self.CaseSelectionPage) #Oi bilol meine iss ki instance idhar create ki thi because it was showing up on every page of case_management
    def showEvidenceManagement(self):
        self.clearFrame()
        self.EvidenceManagement=EvidenceManagementSystem(self.frame,self.CaseSelectionPage)
    def showSuspectManagement(self):
        self.clearFrame()
        self.SuspectManagement=SuspectManagementSystem(self.frame,self.CaseSelectionPage)

    
 
    def CaseSelectionPage(self):
     self.clearFrame()  # Clear the current frame
     
     optionsFrame = LabelFrame(self.frame, text="Options",bg="#79AC78")
     optionsFrame.grid(row=0, column=0, padx=300, pady=10)
     custom_font = font.Font(family="Times New Roman", size=15)
     
     addCaseButton = Button(optionsFrame, text='Add Case',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=50, pady=10, command=self.addCaseScreen)
     addCaseButton.grid(row=0, column=0, padx=100, pady=10)

     updateCaseButton = Button(optionsFrame, text='Update Case',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=50, pady=10, command=self.updateCaseScreen)
     updateCaseButton.grid(row=1, column=0, padx=100, pady=10)

     deleteCaseButton = Button(optionsFrame, text='Delete Case',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=50, pady=10, command=self.deleteCaseScreen)
     deleteCaseButton.grid(row=2, column=0, padx=100, pady=10)

     viewCasesButton = Button(optionsFrame, text='View Cases',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15,padx=50, pady=10, command=self.viewCasesScreen)
     viewCasesButton.grid(row=3, column=0, padx=100, pady=10)

     manageVictimButton = Button(optionsFrame, text="Manage Victims",bg="#7AB2B2",fg="black",font=custom_font,height=2, width=15, padx=50, pady=10,command=self.showVictimManagement)
     manageVictimButton.grid(row=0, column=1, padx=100, pady=10)
     
     manageWitnessButton = Button(optionsFrame, text="Manage Witnesses",bg="#7AB2B2",fg="black",font=custom_font,height=2, width=15, padx=50, pady=10, command=self.showWitnessManagement)
     manageWitnessButton.grid(row=1, column=1, padx=100, pady=10)
     
     manageWitnessButton = Button(optionsFrame, text="Manage Suspects",bg="#7AB2B2",fg="black",font=custom_font,height=2, width=15, padx=50, pady=10, command=self.showSuspectManagement)
     manageWitnessButton.grid(row=2, column=1, padx=100, pady=10)
     
     manageEvidenceButton = Button(optionsFrame, text="Manage Evidence",bg="#7AB2B2",fg="black",font=custom_font,height=2, width=15, padx=50, pady=10, command=self.showEvidenceManagement)
     manageEvidenceButton.grid(row=3, column=1, padx=100, pady=10)
     
     if self.back_callback:
            backButton = Button(optionsFrame, text="Back", command=self.back_callback)
            backButton.grid(row=4, column=1, padx=20, pady=10)

    def clearFrame(self):
     if self.frame.winfo_exists():
        for widget in self.frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = Tk()
    app = CaseManagementSystem(root)
    root.mainloop()




