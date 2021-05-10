import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    # Tuple that contains data about employees. Initiated via controller
    name_tuple = []
    surname_tuple = []
    position_tuple = []
    age_tuple = []
    salary_tuple = []

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        #     GUI variables
        frame = tk.Frame(height=100, width=100)

        self.name = tk.StringVar()
        self.name_entry = tk.Entry(frame, textvariable=self.name)

        self.surname = tk.StringVar()
        self.surname_entry = tk.Entry(frame, textvariable=self.surname)

        self.age = tk.IntVar()
        self.age_entry = tk.Entry(frame, textvariable=self.age)

        self.position = tk.StringVar()
        self.position_entry = tk.Entry(frame, textvariable=self.position)

        self.salary = tk.IntVar()
        self.salary_entry = tk.Entry(frame, textvariable=self.salary)

        self.send_btn = tk.Button(frame, text="Send", command=self.send_data)
        self.test_btn = tk.Button(frame, text="test retrieve", command=self.retrieve_employees_data)

        self.tree_view_test = ttk.Treeview(frame, selectmode="browse")

        self.scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree_view_test.yview())
        self.scrollbar.pack(side='right', fill='x')

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

        # TODO get index of clicked row
        # self.tree_view_test.bind('<ButtonRelease-1>', self.selectItem)

        frame.pack()
        self.name_entry.pack()
        self.surname_entry.pack()
        self.age_entry.pack()
        self.position_entry.pack()
        self.salary_entry.pack()
        self.send_btn.pack()
        self.test_btn.pack()
        self.tree_view_test.pack()

    # Get data from tuples, and pass it into TreeView to display all of the employees data
    def retrieve_employees_data(self):
        self.controller.get_employees_name()
        self.controller.get_employees_surname()
        self.controller.get_employees_age()
        self.controller.get_employees_position()
        self.controller.get_employees_salary()

        for item in zip(self.name_tuple, self.surname_tuple, self.age_tuple, self.position_tuple, self.salary_tuple):
            self.tree_view_test.insert("", "end", values=item)

    # Pass data from entry widgets to the controller
    def send_data(self):
        self.controller.add_new_employee(self.name.get(), self.surname.get(), self.age.get(),
                                         self.position.get(), self.salary.get())

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
        self.mainloop()
