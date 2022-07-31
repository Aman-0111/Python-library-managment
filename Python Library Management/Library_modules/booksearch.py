from database import display_data
import tkinter as tk


def Search(tab,entry):
    """
    Function asks for a book title and calls function to
    display the data based on the users input into tkinter

    Parameters: tab - The tab everyting is displayed on
    entry - Tkinter variable that stores what the user enters

    No values returned.
    """
    #Label and field created to ask for book title and store it in entry
    tk.Label(tab,text = "Enter book title to search").pack(pady = 10)
    search_field = tk.Entry(tab,textvariable = entry)
    search_field.pack(pady = 10)
    #Button to run display_data function
    tk.Button(tab,text = "Search",
    command = lambda:display_data(tab,entry,Search)).pack()


#Tests the only function in the module
if __name__ == "__main__":
    Search()
    print("Module Test Complete")
