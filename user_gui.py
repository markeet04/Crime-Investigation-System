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

class UserManagementSystem:
    def __init__(self, window, back_callback=None):
        self.window = window
        self.back_callback = back_callback
        self.frame = Frame(self.window,bg="#1a4d2e")
        self.frame.pack(fill=BOTH, expand=True)
        self.db_operations = db_ops(db)

        # Initial screen
        self.selectionPage()

    # Function to display the screen for adding a new user
    def addUserScreen(self):
        self.clearFrame()

        # Label frame to organize widgets
        userDetailsFrame = LabelFrame(self.frame, text="Add New User")
        userDetailsFrame.grid(row=0, column=0, padx=20, pady=10)

        # Labels and Entry fields for user details
        nameLabel = Label(userDetailsFrame, text="User Name:")
        nameLabel.grid(row=0, column=0, padx=5, pady=5)
        self.nameEntry = Entry(userDetailsFrame)
        self.nameEntry.grid(row=0, column=1, padx=5, pady=5)

        passwordLabel = Label(userDetailsFrame, text="Password:")
        passwordLabel.grid(row=1, column=0, padx=5, pady=5)
        self.passwordEntry = Entry(userDetailsFrame, show="*")
        self.passwordEntry.grid(row=1, column=1, padx=5, pady=5)

        # Button to add the user
        addButton = Button(userDetailsFrame, text="Save User Details", command=self.addUser)
        addButton.grid(row=2, columnspan=2, padx=20, pady=10)

        # Button to go back to the selection page
        backButton = Button(userDetailsFrame, text="Back", command=self.selectionPage)
        backButton.grid(row=3, columnspan=2, padx=20, pady=10)

    # Function to add a new user to the database
    def addUser(self):
        # Retrieve user details from entry fields
        user_name = self.nameEntry.get()
        user_password = self.passwordEntry.get()

        # Check if all fields are filled
        if user_name and user_password:
            try:
                # Execute SQL INSERT query using db_ops
                success, message = self.db_operations.create("Users", User_name=user_name, User_password=user_password)
                if success:
                    messagebox.showinfo("Success", message)
                else:
                    messagebox.showerror("Error", message)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showerror("Error", "All fields are required.")

    # Function to clear the frame
    def clearFrame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    # Function to display the selection page
    def selectionPage(self):
        self.clearFrame()

        # Label frame to organize widgets
        optionsFrame = LabelFrame(self.frame, text="Options",bg="#79AC78")
        optionsFrame.grid(row=0, column=0, padx=20, pady=10)
        custom_font = font.Font(family="Times New Roman", size=15)


        # Buttons to navigate to different screens
        addUserButton = Button(optionsFrame, text='Add User',font=custom_font, bg="#7AB2B2",fg="black",height=2, width=15, padx=20, pady=20, command=self.addUserScreen)
        addUserButton.grid(row=2, column=1, padx=20, pady=10)

        if self.back_callback:
            backButton = Button(optionsFrame, text="Back", command=self.back_callback)
            backButton.grid(row=3, column=1, padx=20, pady=10)

if __name__ == "__main__":
    root = Tk()
    app = UserManagementSystem(root)
    root.mainloop()
