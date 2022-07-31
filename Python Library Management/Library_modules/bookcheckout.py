from database import *
import tkinter as tk


def get_memberID(tab,entry):
    """
    Function gets a memberID from user through tkinter

    Parameters:tab - The tab this is being displyed on
    entry - The variable the memberID is stored in
    
    Returns no values.
    """
    
    tk.Label(tab,text = "Enter MemberID").pack(pady = 10)
    #Creates a field to allow user to enter data and stores it in entry
    member_field = tk.Entry(tab,textvariable = entry)
    member_field.pack(pady = 10)
    #Button to call function to check the memberID
    tk.Button(tab,text = "Check MemberID",
    command = lambda:check_memberID(tab,entry)).pack()


def check_memberID(tab,entry):
    """
    Function checks if user entered a valid memberID

    Parameters:tab - The tab this is being displyed on
    entry - The variable the memberID is stored in

    Returns no value.
    """
    #Obtains string from Tkinter variable
    memberID = entry.get()
    #Checks if memberID is a valid ID and runs get_bookID function if it is
    #Displays a clear screen button if invalid memberID is entered
    if memberID.isdigit():      
        if len(memberID) != 4:
            tk.Label(tab,text = "Invalid MemberID").pack()
            tk.Button(tab,text = "Clear Screen",
    command = lambda:update_search_return_check(tab,entry,get_memberID)).pack()
        else:
            tk.Label(tab,text = "Valid MemberID").pack()
            get_bookID(tab,memberID)
    else:
        tk.Label(tab,text = "Invalid MemberID").pack()
        tk.Button(tab,text = "Clear Screen",
    command = lambda:update_search_return_check(tab,entry,get_memberID)).pack()

   
def get_bookID(tab,memberID):
    """
    Function gets a bookID based on the users input into Tkinter

    Parameters:tab - The tab this is being displyed on
    memberID - Holds the memberID

    Returns no value.
    """
    #Tkinter variable to store what is entered in field created below
    entry = tk.StringVar()
    tk.Label(tab,text = "Enter BookID").pack(pady = 10)
    book_field = tk.Entry(tab,textvariable = entry)
    book_field.pack(pady = 10)
    #Button to run check_bookID function with checkout set to true
    tk.Button(tab,text = "Check BookID",
    command = lambda:check_bookID(tab,entry,memberID,True,get_memberID)).pack()


#Test for this module and its functions
if __name__ == "__main__":
    Checkout()
    print("Module Test Complete")
