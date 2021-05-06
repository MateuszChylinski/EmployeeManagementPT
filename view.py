import tkinter as tk
from tkinter import ttk


class View(tk.Tk):

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        #     GUI variables
        frame = ttk.Frame(height=100, width=100)

        self.name = tk.StringVar()
        self.name_entry = ttk.Entry(frame, textvariable=self.name)

        self.surname = tk.StringVar()
        self.surname_entry = ttk.Entry(frame, textvariable=self.surname)

        self.age = tk.IntVar()
        self.age_entry = ttk.Entry(frame, textvariable=self.age)

        self.position = tk.StringVar()
        self.position_entry = ttk.Entry(frame, textvariable=self.position)

        self.salary = tk.IntVar()
        self.salary_entry = ttk.Entry(frame, textvariable=self.salary)

        self.send_btn = ttk.Button(frame, text="Send", command=self.send_data)

        frame.pack()
        self.name_entry.pack()
        self.surname_entry.pack()
        self.age_entry.pack()
        self.position_entry.pack()
        self.salary_entry.pack()
        self.send_btn.pack()

    # Pass data from entry widgets to the controller
    def send_data(self):
        self.controller.add_new_employee(self.name.get(), self.surname.get(), self.age.get(),
                                         self.position.get(), self.salary.get())

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
