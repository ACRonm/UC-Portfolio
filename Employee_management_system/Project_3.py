from tkinter import *
import Employee
import pickle

root = Tk()
root.title("Employee lookup")
root.geometry("400x450")
root.configure(bg="#c6eafa")

try:
    pickled_file = open("employee_data.txt", "rb")
    dictionary = pickle.load(pickled_file)
except:
    dictionary = {}


def searchEmployees():
    search_window = Toplevel(root)
    search_window.title("Search Employees")
    search_window.geometry("450x400")
    Label(search_window, text="Enter employee ID").pack(padx=10, pady=5)
    employeeID = Entry(search_window)
    employeeID.pack(pady=5)

    def search():
        output_text.delete("1.0", END)
        if employeeID.get() in dictionary:
            output_text.insert(END, dictionary[employeeID.get()])
        else:
            print("This employee ID does not exist.")

    search_button = Button(search_window, text="Search", command=search)
    search_button.pack(pady=5)
    output_text = Text(search_window, width=50, height=5)
    output_text.pack(pady=5)


def newEmployeeWindow():
    new_window = Toplevel(root)
    new_window.title("Add a new employee")
    new_window.geometry("400x400")
    Label(new_window, text="Employee Name").grid(row=0, column=0)
    Label(new_window, text="Employee ID").grid(row=1, column=0)
    Label(new_window, text="Department").grid(row=2, column=0)
    Label(new_window, text="Job Title").grid(row=3, column=0)
    new_name = Entry(new_window)
    new_name.grid(row=0, column=1)
    new_id = Entry(new_window)
    new_id.grid(row=1, column=1)
    new_department = Entry(new_window)
    new_department.grid(row=2, column=1)
    new_job_title = Entry(new_window)
    new_job_title.grid(row=3, column=1)

    def addEmployee():
        name = new_name.get()
        employeeID = new_id.get()
        department = new_department.get()
        title = new_job_title.get()
        entry = Employee.Employee(employeeID, name, department, title)
        dictionary[employeeID] = entry
        print("Employee added successfully")
        output = open("employee_data.txt", "wb")
        pickle.dump(dictionary, output)
        output.close()
        new_name.delete(0, END)
        new_id.delete(0, END)
        new_department.delete(0, END)
        new_job_title.delete(0, END)

    quitButton = Button(new_window, text="Quit", command=new_window.destroy)
    quitButton.grid(row=4, column=1)
    submitButton = Button(new_window, text="Submit", command=addEmployee)
    submitButton.grid(row=4, column=0)


def shiftEmployee():
    new_window = Toplevel(root)
    new_window.title("Add a new shift employee")
    new_window.geometry("400x400")
    Label(new_window, text="Employee Name").grid(row=0, column=0)
    Label(new_window, text="Employee ID").grid(row=1, column=0)
    Label(new_window, text="Department").grid(row=2, column=0)
    Label(new_window, text="Job Title").grid(row=3, column=0)
    Label(new_window, text="Shift number").grid(row=4, column=0)
    Label(new_window, text="Hourly rate").grid(row=5, column=0)
    new_name = Entry(new_window)
    new_name.grid(row=0, column=1)
    new_id = Entry(new_window)
    new_id.grid(row=1, column=1)
    new_department = Entry(new_window)
    new_department.grid(row=2, column=1)
    new_job_title = Entry(new_window)
    new_job_title.grid(row=3, column=1)
    new_shift = Entry(new_window)
    new_shift.grid(row=4, column=1)
    new_hourly_rate = Entry(new_window)
    new_hourly_rate.grid(row=5, column=1)

    def addEmployee():
        name = new_name.get()
        employee_id = new_id.get()
        department = new_department.get()
        title = new_job_title.get()
        shift_number = new_shift.get()
        hourly_rate = new_hourly_rate.get()
        entry = Employee.ShiftEmployee(employee_id, name, department, title, shift_number, hourly_rate)
        dictionary[employee_id] = entry
        print("Shift employee added successfully")
        output = open("employee_data.txt", "wb")
        pickle.dump(dictionary, output)
        output.close()
        new_name.delete(0, END)
        new_id.delete(0, END)
        new_department.delete(0, END)
        new_job_title.delete(0, END)
        new_shift.delete(0, END)
        new_hourly_rate.delete(0, END)

    quit_button = Button(new_window, text="Quit", command=new_window.destroy)
    quit_button.grid(row=6, column=1)
    submit_button = Button(new_window, text="Submit", command=addEmployee)
    submit_button.grid(row=6, column=0)


def changeEmployee():
    searchWindow = Toplevel(root)
    searchWindow.title("Change Employee details")
    searchWindow.geometry("400x400")
    Label(searchWindow, text="Employee Name").grid(row=0, column=0)
    Label(searchWindow, text="Employee ID").grid(row=1, column=0)
    Label(searchWindow, text="Department").grid(row=2, column=0)
    Label(searchWindow, text="Job Title").grid(row=3, column=0)
    nameChange = Entry(searchWindow)
    nameChange.grid(row=0, column=1)
    IDChange = Entry(searchWindow)
    IDChange.grid(row=1, column=1)
    departmentChange = Entry(searchWindow)
    departmentChange.grid(row=2, column=1)
    titleChange = Entry(searchWindow)
    titleChange.grid(row=3, column=1)

    def changeDetails():
        if IDChange.get() in dictionary:
            name = nameChange.get()
            employeeID = IDChange.get()
            department = departmentChange.get()
            title = titleChange.get()
            entry = Employee.Employee(employeeID, name, department, title)
            dictionary[employeeID] = entry
            print("Details changed successfully")
        else:
            print("That employee ID does not exist.")

    submitButton = Button(searchWindow, text="Submit", command=changeDetails)
    submitButton.grid(row=4, column=0)


def deleteEmployee():
    delete_window = Toplevel(root)
    delete_window.title("Enter an employee ID to delete.")
    delete_window.geometry("400x400")
    Label(delete_window, text="Enter Employee ID to delete").grid(row=0, column=0)
    deleteID = Entry(delete_window)
    deleteID.grid(row=0, column=1)

    def deleteAction():
        employeeID = deleteID.get()
        if employeeID in dictionary:
            del dictionary[employeeID]
            print("Employee removed successfully")
        else:
            print("That employee ID does not exist")

    deleteButton = Button(delete_window, text="Delete", command=deleteAction)
    deleteButton.grid(row=1, column=0)


def saveAndQuit():
    output = open("employee_data.txt", "wb")
    pickle.dump(dictionary, output)
    output.close()
    root.quit()


spacer = Label(root, bg="#c6eafa").pack(pady=15)

openSearchEmployee = Button(root, text="Search Employees", command=searchEmployees, width=25, pady=5)
openSearchEmployee.pack()

openNewEmployee = Button(root, text="Add a new employee", command=newEmployeeWindow, width=25, pady=5)
openNewEmployee.pack()

newShiftEmployee = Button(root, text="Add a new shift employee", command=shiftEmployee, width=25, pady=5)
newShiftEmployee.pack()

openChangeEmployee = Button(root, text="Change employee details", command=changeEmployee, width=25, pady=5)
openChangeEmployee.pack()

openDeleteEmployee = Button(root, text="Delete an employee", command=deleteEmployee, width=25, pady=5)
openDeleteEmployee.pack()

quitButton = Button(root, text="Save and quit", command=saveAndQuit, width=25, pady=5)
quitButton.pack()
root.mainloop()
