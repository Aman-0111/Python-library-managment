from database import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk



def Weeding(tab):
    """
    Function creates a bar chart button and finds out
    how many times each book haas been taken out

    Parameters: tab - The tab the button will be displayed in

    No values returned.
    """
    #BookIDs = List of BookIDs
    #ID_Used = List of the amount of times each Book has been loaned
    BookIDs, ID_Used = weed_books()
    #Button that calls display_chart function
    tk.Button(tab,text = "Display Bar Chart",
    command=lambda:display_chart(tab,BookIDs,ID_Used)).pack(pady = 10)


def display_chart(tab,BookIDs,ID_Used):
    """
    Function Creates the bar chart using the bookIDs
    and the amount of times they have been used

    Parameters: tab - The tab the button will be displayed in
    BookIDs - List of bookIDs in the database
    ID_Used - List of the amount of times each ID has been used

    No values returned.
    """
    #Button to clear screen
    tk.Button(tab,text = "Clear Screen",
    command=lambda:update_data_display(tab,Weeding)).pack(pady = 5)
 
    #Creates a Bar chart Using the list BookIDs and ID_Used
    fig = Figure(figsize=(10,6), dpi=100)
    axis = fig.add_subplot(111)
    axis.set_ylabel("Number of Loans")
    axis.set_xlabel("BookIDs")
    chart = axis.bar(BookIDs,ID_Used,width = 0.4, color = "r")
    #Draws the Bar chart to the tkinter window
    canvas = FigureCanvasTkAgg(fig, master=tab)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    #Implements the toolbar in matplotlib into tkinter
    toolbar = NavigationToolbar2Tk(canvas,tab)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    
#Tests the function in this module
if __name__ == "__main__":
    Weeding()
    print("Module Test Complete")
