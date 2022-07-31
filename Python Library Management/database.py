from datetime import *
import datetime
import tkinter as tk

       
def update_data_display(tab,function):
    """
    Function destroy all added widgets on a tab to
    clear it for tabs that do not require inputs
    Database, logfile and weeding tabs

    Parameters: tab - the tab that is being cleared fo all its data
    function - the function that is being called to return the tab
    to its original state

    No values are returned.
    """
    for widget in tab.winfo_children():
        widget.destroy()
    function(tab)

def update_search_return_check(tab,entry,function):
    """
    Function destroy all added widgets on a tab to
    clear it for tabs that require inputs
    Search,Return and Checkout tabs

    Parameters: tab - the tab that is being cleared fo all its data
    entry - the variable that will store any inputs in the tab once it is reset
    function - the function that is being called to return the tab
    to its original state

    No values are returned.
    """
    for widget in tab.winfo_children():
        widget.destroy()
    function(tab,entry)


def check_bookID(tab,entry,memberID,checkout,function):
    """
    Function loops through database to check if the bookID is valid and will
    either return the book or check it out depending on the checkout variable
    in the parameter.

    Parameter: tab - the tab the the user entered data into to check the bookID
    entry - the tkinter variable that contains the bookID the user entered
    memberID - the memberID the useer entered earlier in the program (only used
    when checking out a book)
    checkout - A boolean variable that tells the function if a book is being
    checked out or returned
    function - The function that needs to be called when clear screen button is
    pressed

    Returns no values.
    """

    #Obtaains bookID from tkinter variable
    bookID = entry.get()
    length = len(bookID)
    database = open("database.txt","r")
    available = False
    #Loops through each line in the database
    for line in database:
        #Checks if the first "length" characters equal the bookID
        #Explained more in README file
        if str(bookID) == line.strip()[0:(length)]:
            notfound = False
            #A "-" would not be present if the book was unavailable to be loaned
            if "-" in line.strip():
                available = True
                break
            else:
                available = False
                break
        else:
            notfound = True
    database.close()

    #Checks how to interpret notfound and available based on
    #if a book is being checked out being returned
    if checkout:
        #Checks the boolean variables and will either
        #display an error message or checkout the book
        if notfound:
            tk.Label(tab,text = "BookID is not found").pack()
        elif available:
            tk.Label(tab,text = "Book has been checked out").pack()
            new_data = loan_book(memberID,bookID)
            update_database(new_data)
            checkout_logs(bookID)
        else:
            tk.Label(tab,text = "Book is on loan").pack()
    else:
        #Checks the boolean variables and will either
        #display an error message or return the book
        if notfound == False and available == False:
            new_data = book_return(bookID)
            tk.Label(tab,text = "Book has been returned").pack()
            update_database(new_data)
            return_logs(bookID)

        elif notfound:
            tk.Label(tab,text = "BookID is invalid").pack()
            
        else:
            tk.Label(tab,text = "Book has not been checked out").pack()

    #Button to clear the screen
    tk.Button(tab,text = "Clear Screen",
    command = lambda:update_search_return_check(tab,entry,function)).pack()

    



def loan_book(memberID,bookID):
    """
    Function stores the contents of the databse in a string with the
    - replaced by the memberID for the bookID that they want to loan

    Parameters: memberID - memberID is required as a string
    to be copied into the database
    bookID - bookID is required to find the correct line that
    corresponds to the book the member wants to loan

    Return: new_data - A string that contains a copy of the database with the
    memberID in place of the - on the line of the book they want to loan.
    """
    #Explained in README file
    database = open("database.txt","r")
    new_data = ""
    for line in database:
        new_line = line.strip()
        if bookID == new_line[0:len(bookID)]:
            new_line = new_line.replace("-",memberID)

        new_data += new_line + "\n"
    database.close()

    return new_data


def book_return(bookID):
    """
    Function stores the contents of the databse in a string with the
    memberID replaced by a - for the bookID that they want to return

    Parameter: bookID - bookID is used to find the line of the book
    that the user wants to return

    Return: new_data - A string that contains a copy of the database with a
    - in place of the memberID on the line of the book they want to return.
    """
    #Explanation is almost identical to the loan_book function in README
    database = open("database.txt","r")
    new_data = ""
    for line in database:
        new_line = line.strip()
        if bookID == new_line[0:len(bookID)]:
            #The last 4 characters of the line will be stored as the memberID
            #Then .replace() is used to get rid of the memberId
            #and replace it with a - to signify the book is now available
            memberID = new_line[-4:]
            new_line = new_line.replace(memberID,"-")

        new_data += new_line + "\n"
    database.close()
    return new_data


def update_database(new_data):
    """
    Function overwrites the database with the new_data
    to update the availability of the books

    Parameters: new_data - A string that is a copy of the original database
    with the updated availability of certain books give by either the
    loan_book function or the book_return function

    No values are returned.
    """
    
    data_update = open("database.txt","w")
    data_update.write(new_data)
    data_update.close()


    

def display_database(tab):
    """
    Function displays the database in tkinter

    Parameters: tab - the tab the database is displayed in

    No values are returned.
    """
    
    database = open("database.txt","r")
    #Labels are created to display the headings and
    #contents of the database in a neat format
    tk.Label(tab,text = "BookID | ISBN | Title | Author \
| Purchase Date | Availability").pack()

    tk.Label(tab,text = "-"*65).pack()

    tk.Label(tab,text = database.read()).pack()
    #Button to refresh the database incase a book was taken out or returned
    tk.Button(tab,text="Refresh Database",
    command = lambda:update_data_display(tab,display_database)).pack()

def display_logfile(tab):
    """
    Function displays the logfile in tkinter

    Parameters: tab - the tab the logfile is displayed in

    No values are returned.
    """
    
    logs = open("logfile.txt","r")
    #Labels are created to display the headings and
    #contents of the logfile in a neat format
    tk.Label(tab,text = "ID|  Checkout  |  Return").pack()

    tk.Label(tab,text = "-"*30).pack()

    tk.Label(tab,text = logs.read()).pack()
    #Button to refresh the logfile incase a book was taken out or returned
    tk.Button(tab,text="Refresh logfile",
    command = lambda:update_data_display(tab,display_logfile)).pack()



def display_data(tab,entry,Search):
    """
    Function displays all the books that match the book title in tkinter

    Parameter: tab - the tab the books will be displayed in
    entry - the tkinter variable that stores what the user entered
    Search - the search function that should be called to clear the screen

    No values are returned.
    """
    
    found = False
    
    database = open("database.txt","r")
    #Displays the headings and a line to seperate the headings from the books
    tk.Label(tab,text = "BookID | ISBN | Title | Author \
| Purchase Date | Availability").pack()

    tk.Label(tab,text = "-"*65).pack()

    #Gets a string value from the tkinter variable
    book = entry.get()
    book = book.upper()

    #Checks database if book exists and will display the line if it does
    for line in database:
        if book in line.strip():
            tk.Label(tab,text = line.strip()).pack()
            found = True

    #Displays an error message if no book was found
    if found:
        pass
    else:
        tk.Label(tab,text = "Book not found").pack()

    #Button to clear screen
    tk.Button(tab,text="Clear Screen",
    command = lambda:update_search_return_check(tab,entry,Search)).pack()
    

    database.close()


def checkout_logs(bookID):
    """
    Function creates a new line in the logfile when a book is checked out using
    the same method as updating the database in loan_book
    and book_return functions

    Parameter: bookID - The bookID is needed so that when the logs are updated
    the correct bookID is added to the line

    No values are Returned.
    """
    #Using the datetime module to find the date in the correct format
    today = date.today()
    today =str(today.strftime("%d/%m/%Y"))
    log = bookID+" | "+today+" | -\n"
    #Same concept as loan_book and book_return function
    #Did not open file in append mode due to empty lines appearing in the file
    logs = open("logfile.txt","r")
    new_logs = ""
    for lines in logs:
        new_line = lines.strip()
        new_logs += new_line+"\n"
    #Adds new log to the end of the recreated logfile
    #with a - inplace of the return date
    new_logs += log
    logs.close()
    #updates logfile
    update_logs(new_logs)



def return_logs(bookID):
    """
    Function updates the logfile and replaces the -
    in the incomplete log in the logfile with todays date

    Parameter: bookID - is used to find the line in the
    logfile with the correct book

    No values are Returned.
    """
    today = date.today()
    today =str(today.strftime("%d/%m/%Y"))
    #Same concept as loan_book and book_return function
    logs = open("logfile.txt","r")
    new_logs = ""
    for line in logs:
        new_line = line.strip()
        if bookID == new_line[0:len(bookID)]:
            if "-" in new_line:
                new_line = new_line.replace("-",today)

        new_logs += new_line+"\n"
    logs.close()
    #updates logfile
    update_logs(new_logs)

def update_logs(new_logs):
    """
    Function overwrites the logfile with the new_logs
    to update the transactions

    Parameters: new_logs - A string that is a copy of the original logfile
    with the updated transactions given by return_logs or checkout_logs

    No values are returned.
    """
    logs = open("logfile.txt","w")
    logs.write(new_logs)
    logs.close()


def weed_books():
    """
    Function finds all the bookIDs, how many times each book has been loaned
    and appends each line of the database to a list

    No parameters are required

    Returns: BookIDs - A list of all the bookIDs
    ID_Used - A list of how many times each bookID has been used
    """
    BookIDs = []
    ID_Used = []
    database = open("database.txt","r")
    books = 0
    #Finds how many books there are in the database
    for line in database:
        books += 1       
    database.close()
    #Uses the number of books in the database to
    #append all the bookIDs to the list
    for Id in range(1,books+1):
        BookIDs.append(Id)
    #Uses a nested loop to count how many times an ID appears in the logfile
    for Id in range(1,books+1):
        used = 0
        logs = open("logfile.txt","r")
        for line in logs:
            #Checks if the first characters in the log are equal to the bookID
            if str(Id) == line.strip()[0:len(str(Id))]:
                used += 1
        logs.close()
        ID_Used.append(used)


    return BookIDs, ID_Used



#Tests this module
#Note if every other module is tested before this then all
#functions within this module will have been tested
if __name__ == "__main__":
    notfound, available = check_bookID(6)
    new_data = loan_book("1111","6")
    update_database(new_data)
    new_data = book_return("6")
    update_database(new_data)
    display_database()
    display_data("DRAGON")
    checkout_logs("6")
    return_logs("6")
    display_logs()
    weed_books()
    
    
    


