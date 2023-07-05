from tkinter import *
from tkinter import ttk

def main():
    #Initializes root
    root = Tk()
    root.geometry("920x520")
    root.resizable(False, False)
    root.title("Gamma")

    #Initializes viewmodel
    content = ttk.Frame(root)

    #Variables
    nameFirst = "Nathaniel"
    nameLast = "Bamshen"
    student_gpa = 0.6
    semester = 1
    markingPeriod = 2 

    #Modules
    student_name = ttk.Label(content, text = nameLast + ", " + nameFirst)
    student_grade = ttk.Label(content, text = student_gpa)
    period = ttk.Label(content, text = f"Semester: {semester} \n Marking-period: {markingPeriod}")

    #Positioning    
    content.grid(row=0, column=0)
    student_name.grid(row=0, column=1)
    student_grade.grid(row = 0, column = 2)
    period.grid(row = 0, column = 3)

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)

    root.mainloop()


main()