import tkinter as tk
from tkinter import ttk, messagebox


class View(tk.Tk):
    # Tuple that contains data about employees. Initiated via controller
    employee_data = []
    name_tuple = []
    surname_tuple = []
    position_tuple = []
    age_tuple = []
    salary_tuple = []
    # Index which will be passing as ID of employees.
    # It'll be needed in case if user decide to update/delete employee data
    index = -1

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        #     GUI variables (these views are for main_frame)
        self.main_frame = tk.Frame(height=100, width=100)

        self.delete_btn = tk.Button(self.main_frame, text="Delete employee", command=lambda: self.delete_employee())
        self.delete_all_btn = tk.Button(self.main_frame, text="Delete all employees", command=self.delete_all_employees)
        self.add_employee_btn = tk.Button(self.main_frame, text="Add employee", command=self.change_frame_to_add_employee)

        self.tree_view_test = ttk.Treeview(self.main_frame, selectmode="browse")

        self.scrollbar = ttk.Scrollbar(self.main_frame, command=self.tree_view_test.yview())
        self.scrollbar.grid(sticky = "n")

        self.tree_view_test.configure(xscrollcommand=self.scrollbar.set)
        self.tree_view_test["columns"] = ("name", "surname", "age", "position", "salary")
        self.tree_view_test["show"] = "headings"

        self.tree_view_test.column("name", width=90, anchor='se')
        self.tree_view_test.column("surname", width=90, anchor='se')
        self.tree_view_test.column("age", width=90, anchor='se')
        self.tree_view_test.column("position", width=90, anchor='se')
        self.tree_view_test.column("salary", width=90, anchor='se')

        self.tree_view_test.heading("name", text="Name")
        self.tree_view_test.heading("surname", text="Surname")
        self.tree_view_test.heading("age", text="Age")
        self.tree_view_test.heading("position", text="Position")
        self.tree_view_test.heading("salary", text="Salary")
        # Get index of clicked row and save it as ID to update/delete
        self.tree_view_test.bind('<ButtonRelease-1>', lambda e: self.clicked_index())

        self.main_frame.grid()
        self.delete_btn.grid()
        self.delete_all_btn.grid()
        self.add_employee_btn.grid()
        self.tree_view_test.grid()

        # GUI variables (these widgets are for edit_employee frame)

        self.edit_employee_frame = tk.Frame(height=100, width=100, background="red")

        self.go_to_update_employee = tk.Button(self.main_frame, text="Edit employee data",
                                               command=lambda: self.change_frame_to_update_employee())
        self.update_employee_data = tk.Button(self.edit_employee_frame, text="Update", command=self.update_data)

        self.edit_employee_name = tk.StringVar()
        self.edit_employee_name_entry = tk.Entry(self.edit_employee_frame, textvariable=self.edit_employee_name)
        # By using "insert" statement, we can load the data about specified employee
        self.edit_employee_name_entry.insert(0, "Name")

        self.edit_employee_surname = tk.StringVar()
        self.edit_employee_surname_entry = tk.Entry(self.edit_employee_frame, textvariable=self.edit_employee_surname)
        # By using "insert" statement, we can load the data about specified employee
        self.edit_employee_surname_entry.insert(0, "Surname")

        self.edit_employee_age = tk.IntVar()
        self.edit_employee_age_entry = tk.Entry(self.edit_employee_frame, textvariable=self.edit_employee_age)
        # Using the "delete" statement, we can clear out the entry.
        self.edit_employee_age_entry.delete(0, "end")
        # By using "insert" statement, we can load the data about specified employee
        self.edit_employee_age_entry.insert(0, "Age")

        self.edit_employee_position = tk.StringVar()
        self.edit_employee_position_entry = tk.Entry(self.edit_employee_frame, textvariable=self.edit_employee_position)
        # By using "insert" statement, we can load the data about specified employee
        self.edit_employee_position_entry.insert(0, "Position")

        self.edit_employee_salary = tk.IntVar()
        self.edit_employee_salary_entry = tk.Entry(self.edit_employee_frame, textvariable=self.edit_employee_salary)
        # Using the "delete" statement, we can clear out the entry.
        self.edit_employee_salary_entry.delete(0, "end")
        # By using "insert" statement, we can load the data about specified employee
        self.edit_employee_salary_entry.insert(0, "Salary")

        self.edit_employee_frame.grid()
        self.edit_employee_frame.grid_forget()

        self.go_to_update_employee.grid()
        self.update_employee_data.grid()
        self.edit_employee_name_entry.grid()
        self.edit_employee_surname_entry.grid()
        self.edit_employee_age_entry.grid()
        self.edit_employee_position_entry.grid()
        self.edit_employee_salary_entry.grid()

        # GUI variables (these widgets are for edit_employee frame)
        self.add_employee_frame = tk.Frame(height=100, width=100)


        self.name = tk.StringVar()
        self.add_employee_name_label = tk.Label(self.add_employee_frame, text="Name: ")
        self.name_entry = tk.Entry(self.add_employee_frame, textvariable=self.name)

        self.surname = tk.StringVar()
        self.add_employee_surname_label = tk.Label(self.add_employee_frame, text="Surname: ")
        self.surname_entry = tk.Entry(self.add_employee_frame, textvariable=self.surname)

        self.age = tk.IntVar()
        self.add_employee_age_label = tk.Label(self.add_employee_frame, text="Age: ")
        self.age_entry = tk.Entry(self.add_employee_frame, textvariable=self.age)

        self.position = tk.StringVar()
        self.add_employee_position_label = tk.Label(self.add_employee_frame, text="Position: ")
        self.position_entry = tk.Entry(self.add_employee_frame, textvariable=self.position)

        self.salary = tk.IntVar()
        self.add_employee_salary_label = tk.Label(self.add_employee_frame, text="Salary: ")
        self.salary_entry = tk.Entry(self.add_employee_frame, textvariable=self.salary)

        self.send_btn = tk.Button(self.add_employee_frame, text="Add employee", command=self.send_data)

        self.add_employee_frame.grid()
        self.add_employee_frame.grid_forget()

        self.name_entry.grid()
        self.add_employee_name_label.grid()

        self.surname_entry.grid()
        self.add_employee_surname_label.grid()

        self.age_entry.grid()
        self.add_employee_age_label.grid()

        self.position_entry.grid()
        self.add_employee_position_label.grid()

        self.salary_entry.grid()
        self.add_employee_salary_label.grid()

        self.send_btn.grid()

    def clicked_index(self):
        print("clicked index")
        # Get index of clicked row. Had to add here 1, because database starting index is 0,
        # so I had to increment it by one.
        self.index = self.tree_view_test.index(self.tree_view_test.selection()[0]) + 1
        print(self.index)

    # Change frame and proceed to updating data about employee
    def change_frame_to_update_employee(self, event=None):
        if self.index == -1:
            messagebox.showwarning("Missing Value",
                                   "You have to select proper row to proceed updating data of specified employee")
        else:
            self.main_frame.grid_forget()
            self.edit_employee_frame.grid()
            self.controller.get_employee_data_by_id(self.index)

    def change_frame_to_add_employee(self, event=None):
        self.main_frame.grid_forget()
        self.add_employee_frame.grid()

    # Check if every entry widget is filled and proceed to update data
    def update_data(self):

        if len(self.edit_employee_name.get() and self.edit_employee_surname.get() and
               self.edit_employee_position.get()) == 0:
            messagebox.showwarning("Missing Values", "Fill empty entries")
        elif (self.edit_employee_age.get() and self.edit_employee_salary.get()) < 1:
            messagebox.showwarning("Missing Values", "Fill empty entries")
        else:
            # self.controller.update_employee_data("Name123", "Surname123", 999, "Position123", 11111111, 1)
            self.controller.update_employee_data(self.edit_employee_name, self.edit_employee_surname,
                                                 self.edit_employee_age, self.edit_employee_position,
                                                 self.edit_employee_salary, self.index)
        self.edit_employee_frame.grid_forget()
        self.main_frame.grid()

        self.edit_employee_name_entry.delete(0, "end")
        self.edit_employee_surname_entry.delete(0, "end")
        self.edit_employee_age_entry.delete(0, "end")
        self.edit_employee_position_entry.delete(0, "end")
        self.edit_employee_salary_entry.delete(0, "end")
        print("Update")

    # Get data from tuples, and pass it into TreeView to display all of the employees data
    def retrieve_employees_data(self):
        print("retrieve employees data")
        self.controller.get_employees_name()
        self.controller.get_employees_surname()
        self.controller.get_employees_age()
        self.controller.get_employees_position()
        self.controller.get_employees_salary()

        for item in zip(self.name_tuple, self.surname_tuple, self.age_tuple, self.position_tuple, self.salary_tuple):
            self.tree_view_test.insert("", "end", values=item)

    # Pass data from entry widgets to the controller
    def send_data(self):
        print("send_data")
        if len(self.name.get() and self.surname.get() and
               self.position.get()) == 0:
            messagebox.showwarning("Missing Values", "Fill empty entries")

        elif (self.age.get() and self.salary.get()) < 1:
            messagebox.showwarning("Missing Values", "Fill empty entries")
        else:
            self.controller.add_new_employee(self.name.get(), self.surname.get(), self.age.get(),
                                             self.position.get(), self.salary.get())

    # Proceed to delete employee with suitable ID
    def delete_employee(self):
        print("Delete employee")
        self.controller.delete_employee_by_id(self.index)

    # Proceed to delete all employees from table
    def delete_all_employees(self):
        print("Delete all employees")
        self.controller.delete_all_employees()
        self.main_frame.update_idletasks()

    # Method that center GUI
    def _center_window(self):
        self.update()

        width = self.winfo_width()
        height = self.winfo_height()

        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2

        self.geometry(
            f'{width}x{height}+{x_offset}+{y_offset}'
        )

    def main(self):
        self.retrieve_employees_data()
        self._center_window()
        self.mainloop()
