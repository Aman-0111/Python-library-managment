import tkinter as tk
from tkinter import ttk
import Library_modules.booksearch
import Library_modules.bookcheckout
import Library_modules.bookreturn
import Library_modules.bookweed
from database import *


def select(x,notebook):
    """
    Function is used with buttons below to display correct tab when pressed
    Parameters - x is the tab to open and notebook is the note book being used.
    """
    notebook.select(x)
    
def main_menu():
    """
    Function uses Tkinter to create a GUI for the user to use.
    """
    #Creates Screen, sets dimensions and title
    screen = tk.Tk()
    screen.geometry("800x800")
    screen.title("Library Management")

    #Notebook is used to create and store all tabs
    notebook = ttk.Notebook(screen)
    notebook.pack()

    #All tabs are created and stored in notebook
    tab1 = tk.Frame(notebook,width=800,height=800)
    tab2 = tk.Frame(notebook,width=800,height=800)
    tab3 = tk.Frame(notebook,width=800,height=800)
    tab4 = tk.Frame(notebook,width=800,height=800)
    tab5 = tk.Frame(notebook,width=800,height=800)
    tab6 = tk.Frame(notebook,width=800,height=800)
    tab7 = tk.Frame(notebook,width=800,height=800)
    
    tab1.pack(fill = "both", expand = 1)
    tab2.pack(fill = "both", expand = 1)
    tab3.pack(fill = "both", expand = 1)
    tab4.pack(fill = "both", expand = 1)
    tab5.pack(fill = "both", expand = 1)
    tab6.pack(fill = "both", expand = 1)
    tab7.pack(fill = "both", expand = 1)
    
    notebook.add(tab1, text = "Main Menu")
    notebook.add(tab2, text = "Database")
    notebook.add(tab3, text = "Logfile")
    notebook.add(tab4, text = "Search")
    notebook.add(tab5, text = "Checkout")
    notebook.add(tab6, text = "Return")
    notebook.add(tab7, text = "Weeding")

    #Buttons are created to navigate to each of tabs
    tk.Button(tab1,text="Display Database",height = "5",
       width = "30",command=lambda:select(1,notebook)).pack(pady = 10)
    tk.Button(tab1,text="Display Logfile",height = "5",
       width = "30",command=lambda:select(2,notebook)).pack(pady = 10)
    tk.Button(tab1,text="Search",height = "5",
       width = "30",command=lambda:select(3,notebook)).pack(pady = 10)
    tk.Button(tab1,text="Checkout",height = "5",
       width = "30",command=lambda:select(4,notebook)).pack(pady = 10)
    tk.Button(tab1,text="Return",height = "5",
       width = "30",command=lambda:select(5,notebook)).pack(pady = 10)
    tk.Button(tab1,text="Weeding",height = "5",
       width = "30",command=lambda:select(6,notebook)).pack(pady = 10)
    tk.Button(tab1,text="Exit",height = "5",
       width = "30",command=exit).pack(pady = 10)

    #Variable used to store data created by user
    entry = tk.StringVar()
    #Functions are run on each tab when tab is selected
    Display_tab = display_database(tab2)
    Logfile_tab = display_logfile(tab3)
    Search_tab = Library_modules.booksearch.Search(tab4,entry)
    Checkout_tab = Library_modules.bookcheckout.get_memberID(tab5,entry)
    Return_tab = Library_modules.bookreturn.Return(tab6,entry)
    Weeding_tab = Library_modules.bookweed.Weeding(tab7)

    
    screen.mainloop()
    


#Tests this module and used for actual program
if __name__ == "__main__":
    main_menu()
