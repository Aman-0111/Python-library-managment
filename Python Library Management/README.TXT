Special Instructions

-A copy of the logfile and database are in the Library_modules package so that when 
testing these modules they do not affect the actual database and logfile.
-A copy of the database module was put in the Library_modules, this is allows the
assessor to test all modules of the program without altering the actual database
and logfile.
-When testing database module its location does not matter but preferably
the one in the Library_modules file should be run as it is an exact copy and will
not affect the actual database and logfile.
-If testing other modules before the database module then make sure bookID 6 is 
available as bookID 6 is the book used in testing the database module.
-When running the program regularly make sure database module is in the same
location as the menu program so no errors when importing the database occur.

Code explanation

-check_bookID function - Database Module
    -The If statment (if str(bookID) == line.strip()[0:(length)]:) is uses
     the length of the bookID to check if the line that is being checked
     corresponds to the correct book. Length of bookID is required so that it
     does not check the entire line as the ISBN number of another book more
     than likely contains the bookID of the book the user is searching for which
     lead to errors later in the program.

-loan_book function - Database Module
    -This function opens the database in read mode and utilises a for loop to go
     through each line and store it in a variable(new_line). Then before it adds
     the variable to the recreation of the database (new_data) it checks if the
     line matches the bookID that is being loaned using the same IF statment as
     the check_bookID function above. When it finds the correct line it uses
     .replace to get rid of the "-" for the memberID to signify that the book has
     been taken out.