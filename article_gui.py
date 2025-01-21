from tkinter import *
from tkinter import ttk, messagebox
from article import Article
from database_operations import db_ops
import mysql.connector
from tkinter import *
from tkinter import font

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)

class ArticleManagementSystem:
    def __init__(self, window, back_callback=None):
        self.window = window
        
        self.back_callback = back_callback
        self.window = Frame(self.window,bg="#1a4d2e")
        self.window.pack(fill=BOTH, expand=True)
        self.db_operations = db_ops(db)
        
        self.ArticleSelectionPage()
    # Function to display the screen for adding a new article
    def addArticleScreen(self):
        self.clearFrame()

        # Label frame to organize widgets
        articleDetailsFrame = LabelFrame(self.window, text="Add New Article",bg="#79AC78")
        articleDetailsFrame.grid(row=0, column=0, padx=450, pady=10)

        # Labels and Entry fields for article details
        nameLabel = Label(articleDetailsFrame, text="Article Name:",bg="#79AC78")
        nameLabel.grid(row=0, column=0, padx=5, pady=5)
        self.nameEntry = Entry(articleDetailsFrame)
        self.nameEntry.grid(row=0, column=1, padx=5, pady=5)

        numberLabel = Label(articleDetailsFrame, text="Article Number:",bg="#79AC78")
        numberLabel.grid(row=1, column=0, padx=5, pady=5)
        self.numberEntry = Entry(articleDetailsFrame)
        self.numberEntry.grid(row=1, column=1, padx=5, pady=5)

        punishmentTypeLabel = Label(articleDetailsFrame, text="Punishment Type:",bg="#79AC78")
        punishmentTypeLabel.grid(row=2, column=0, padx=5, pady=5)
        self.punishmentTypeEntry = Entry(articleDetailsFrame)
        self.punishmentTypeEntry.grid(row=2, column=1, padx=5, pady=5)

        timePeriodLabel = Label(articleDetailsFrame, text="Punishment Time Period:",bg="#79AC78")
        timePeriodLabel.grid(row=3, column=0, padx=5, pady=5)
        self.timePeriodEntry = Entry(articleDetailsFrame)
        self.timePeriodEntry.grid(row=3, column=1, padx=5, pady=5)

        # Button to add the article
        addButton = Button(articleDetailsFrame, text="Save Article Details", command=self.addArticle)
        addButton.grid(row=4, columnspan=2, padx=20, pady=10)

        # Button to go back to the selection page
        backButton = Button(articleDetailsFrame, text="Back", command=self.ArticleSelectionPage)
        backButton.grid(row=5, columnspan=2, padx=20, pady=10)

    # Function to add a new article to the database
    def addArticle(self):
        # Retrieve article details from entry fields
        article_name = self.nameEntry.get()
        article_number = self.numberEntry.get()
        punishment_type = self.punishmentTypeEntry.get()
        punishment_time_period = self.timePeriodEntry.get()

        # Check if all fields are filled
        if article_name and article_number and punishment_type and punishment_time_period:
            try:
                new_article = Article( article_number, article_name, punishment_type)

                # Execute SQL INSERT query using db_ops
                success, message = self.db_operations.create("Article", article_name=article_name, article_number=article_number, punishment_type=punishment_type, punishment_time_period=punishment_time_period)
                if success:
                    messagebox.showinfo("Success", message)
                else:
                    messagebox.showerror("Error", message)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showerror("Error", "All fields are required.")

 # Function to display the screen for updating an article
    def updateArticleScreen(self):
        self.clearFrame()

        # Label and entry for entering the article ID to update
        idLabel = Label(self.window, text="Enter Article ID to Update:",bg="#79AC78")
        idLabel.pack(padx=350, pady=10)
        self.updateIdEntry = Entry(self.window)
        self.updateIdEntry.pack(padx=10, pady=10)

        # Button to initiate the update process
        updateButton = Button(self.window, text="Update", command=lambda: self.updateArticle(self.updateIdEntry.get()))
        updateButton.pack(padx=10, pady=10)

        # Button to go back to the selection page
        backButton = Button(self.window, text="Back", command=self.ArticleSelectionPage)
        backButton.pack(padx=10, pady=10)

    # Function to display the screen for deleting an article
    def deleteArticleScreen(self):
        self.clearFrame()

        # Label frame to organize widgets
        deleteArticleFrame = LabelFrame(self.window, text="Delete Article",bg="#79AC78")
        deleteArticleFrame.grid(row=0, column=0, padx=350, pady=10)

        # Label and Entry field for article ID
        idLabel = Label(deleteArticleFrame, text="Enter Article ID to Delete:",bg="#79AC78")
        idLabel.grid(row=0, column=0, padx=5, pady=5)
        self.deleteIdEntry = Entry(deleteArticleFrame)
        self.deleteIdEntry.grid(row=1, column=0, padx=5, pady=5)

        # Button to delete the article
        deleteButton = Button(deleteArticleFrame, text="Delete", command=self.deleteArticle)
        deleteButton.grid(row=2, columnspan=1, padx=20, pady=10)

        # Button to go back to the selection page
        backButton = Button(deleteArticleFrame, text="Back", command=self.ArticleSelectionPage)
        backButton.grid(row=3, columnspan=1, padx=10, pady=10)

    def updateArticle(self, article_id=None):
        if article_id is None:
            article_id = self.updateIdEntry.get()
        if article_id:
            try:
                # Retrieve the article data from the database using db_ops
                success, article = self.db_operations.read("Article", article_id)
                if success and article is not None:
                    # Clear the frame and display the update form
                    self.clearFrame()

                    updateArticleFrame = LabelFrame(self.window, text="Update Article",bg="#79AC78")
                    updateArticleFrame.pack(padx=20, pady=10)

                    # Entry fields to update article details
                    idLabel = Label(updateArticleFrame, text="ID",bg="#79AC78")
                    idLabel.grid(row=0, column=0, padx=5, pady=5)
                    self.idUpdateEntry = Entry(updateArticleFrame)
                    self.idUpdateEntry.insert(0, article[0])
                    self.idUpdateEntry.grid(row=0, column=1, padx=5, pady=5)
                    self.idUpdateEntry.config(state='disabled')

                    nameLabel = Label(updateArticleFrame, text="Name",bg="#79AC78")
                    nameLabel.grid(row=1, column=0, padx=5, pady=5)
                    self.nameUpdateEntry = Entry(updateArticleFrame)
                    self.nameUpdateEntry.insert(0, article[1])
                    self.nameUpdateEntry.grid(row=1, column=1, padx=5, pady=5)

                    numberLabel = Label(updateArticleFrame, text="Number",bg="#79AC78")
                    numberLabel.grid(row=2, column=0, padx=5, pady=5)
                    self.numberUpdateEntry = Entry(updateArticleFrame)
                    self.numberUpdateEntry.insert(0, article[2])
                    self.numberUpdateEntry.grid(row=2, column=1, padx=5, pady=5)

                    punishmentTypeLabel = Label(updateArticleFrame, text="Punishment Type",bg="#79AC78")
                    punishmentTypeLabel.grid(row=3, column=0, padx=5, pady=5)
                    self.punishmentTypeUpdateEntry = Entry(updateArticleFrame)
                    self.punishmentTypeUpdateEntry.insert(0, article[3])
                    self.punishmentTypeUpdateEntry.grid(row=3, column=1, padx=5, pady=5)

                    timePeriodLabel = Label(updateArticleFrame, text="Time Period",bg="#79AC78")
                    timePeriodLabel.grid(row=4, column=0, padx=5, pady=5)
                    self.timePeriodUpdateEntry = Entry(updateArticleFrame)
                    self.timePeriodUpdateEntry.insert(0, article[4])
                    self.timePeriodUpdateEntry.grid(row=4, column=1, padx=5, pady=5)

                    # Button to perform the update
                    updateButton = Button(updateArticleFrame, text="Update Article", command=lambda: self.performUpdate(article_id))
                    updateButton.grid(row=5, columnspan=2, padx=20, pady=10)

                    # Button to go back to the selection page
                    backButton = Button(updateArticleFrame, text="Back", command=self.ArticleSelectionPage)
                    backButton.grid(row=6, columnspan=2, padx=20, pady=10)
                elif not success:
                    messagebox.showerror("Error", "Failed to retrieve article data.")
                else:
                    messagebox.showerror("Error", "Article not found.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showerror("Error", "Article ID is required.")

    # Function to perform the update operation
    def performUpdate(self, article_id):
        # Retrieve updated values from entry fields
        article_name = self.nameUpdateEntry.get()
        article_number = self.numberUpdateEntry.get()
        punishment_type = self.punishmentTypeUpdateEntry.get()
        time_period = self.timePeriodUpdateEntry.get()

        # Check if all fields are provided
        if article_name and article_number and punishment_type and time_period:
            try:
                # Execute the update operation using db_ops
                
                
                updated_article = Article( article_number, article_name, punishment_type)

                success, message = self.db_operations.update("Article", article_id, Article_name=article_name, Article_number=article_number, punishment_type=punishment_type, punishment_time_period=time_period)
                if success:
                    messagebox.showinfo("Success", message)
                else:
                    messagebox.showerror("Error", message)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showerror("Error", "All fields are required.")


    # Function to delete an article from the database
    def deleteArticle(self):
        # Retrieve article ID from entry field
        article_id = self.deleteIdEntry.get()

        # Check if article ID is provided
        if article_id:
            try:
                # Execute SQL DELETE query using db_ops
                success, message = self.db_operations.delete("Article", article_id)
                if success:
                    messagebox.showinfo("Success", message)
                else:
                    messagebox.showerror("Error", message)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showerror("Error", "Article ID is required.")

    # Function to display the screen for viewing all articles
    def viewArticlesScreen(self):
        self.clearFrame()

        # Label frame to organize widgets
        viewArticlesFrame = LabelFrame(self.window, text="View All Articles",bg="#79AC78")
        viewArticlesFrame.grid(row=0, column=0, padx=150, pady=10)

        try:
            # Retrieve all articles from the database using db_ops
            success, articles = self.db_operations.read_all("Article")
            if success:
                # Display articles in a Treeview widget
                tree = ttk.Treeview(viewArticlesFrame, columns=("ID", "Name", "Number", "Punishment Type", "Time Period"))
                tree.heading("#0", text="", anchor="center")
                tree.heading("ID", text="ID", anchor="center")
                tree.heading("Name", text="Name", anchor="center")
                tree.heading("Number", text="Number", anchor="center")
                tree.heading("Punishment Type", text="Punishment Type", anchor="center")
                tree.heading("Time Period", text="Time Period", anchor="center")

                for article in articles:
                    tree.insert("", "end", values=article)

                tree.pack()
            else:
                messagebox.showerror("Error", articles)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

        # Button to go back to the selection page
        backButton = Button(viewArticlesFrame, text="Back", command=self.ArticleSelectionPage)
        backButton.pack(padx=10, pady=10)

    # Function to clear the frame
    def clearFrame(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    # Function to display the selection page
    def ArticleSelectionPage(self):
     self.clearFrame()

     # Label frame to organize widgets
     optionsFrame = LabelFrame(self.window, text="Options",bg="#79AC78")
     optionsFrame.grid(row=0, column=0, padx=350, pady=10)
     custom_font = font.Font(family="Times New Roman", size=15)


     # Buttons to navigate to different screens
     addArticleButton = Button(optionsFrame, text='Add Article', bg="#7AB2B2",fg="black",height=2,font=custom_font, width=15, padx=20, pady=20, command=self.addArticleScreen)
     addArticleButton.grid(row=0,column=0,padx=100, pady=10)
     # Button to navigate to the update screen
     updateArticleButton = Button(optionsFrame, text='Update Article',bg="#7AB2B2",fg="black",font=custom_font, height=2, width=15, padx=20, pady=20, command=self.updateArticleScreen)
     updateArticleButton.grid(row=1,column=0,padx=100, pady=10)
     
     deleteArticleButton = Button(optionsFrame, text='Delete Article', bg="#7AB2B2",fg="black",font=custom_font,height=2, width=15, padx=20, pady=20, command=self.deleteArticleScreen)
     deleteArticleButton.grid(row=0,column=1,padx=100, pady=10)

     viewArticlesButton = Button(optionsFrame, text='View Articles',bg="#7AB2B2",fg="black", font=custom_font,height=2, width=15, padx=20, pady=20, command=self.viewArticlesScreen)
     viewArticlesButton.grid(row=1,column=1,padx=100, pady=10)
     if self.back_callback:
            backButton = Button(optionsFrame, text="Back", command=self.back_callback)
            backButton.grid(row=4, column=1, padx=20, pady=10)


if __name__ == "__main__":
    root = Tk()
    app = ArticleManagementSystem(root)
    root.mainloop()

