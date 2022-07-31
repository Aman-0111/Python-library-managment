from database import *
import tkinter as tk

def Return(tab,entry):
    """
    Function updates database and logfile
    to represent returns of bookID entered into tkinter

    Parameters: tab - The tab the data is displayed on
    entry - Tkinter variable that stores what the user enters.

    No values returned.
    """
    #Label and field created to ask for bookID and store it in entry
    tk.Label(tab,text = "Enter bookID to return").pack(pady = 10)
    return_field = tk.Entry(tab,textvariable = entry)
    return_field.pack(pady = 10)
    #Button to run check_bookID function with checkout set to false
    tk.Button(tab,text = "Return Book",
    command = lambda:check_bookID(tab,entry,None,False,Return)).pack()


    
#Tests the only function in the module
if __name__ == "__main__":
    Return()
    print("Module Test Complete")
