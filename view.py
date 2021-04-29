import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    PADDING = 15

    btn_captions = [
        'Add employee', 'Delete employee', "Display all employees", "Edit employee data"
    ]

    def __init__(self, controller):
        super().__init__()

        self.testInputVar = ""
        self.controller = controller

        # GUI
        self.title("Employee management")
        self._make_main_frame()
        self._make_entry()
        self._make_buttons

    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(padx=self.PADDING, pady=self.PADDING)

    def _make_entry(self):
        test_entry = ttk.Entry(self.frame, textvariable=self.testInputVar)
        test_entry.pack(fill='x')

    def _make_buttons(self):
        outer_btn_frame = ttk.Frame(self.frame)
        outer_btn_frame.pack()

        btn_frame = ttk.Frame(outer_btn_frame)
        btn_frame.pack()

        for caption in self.btn_captions:
            btn = ttk.Button(
                btn_frame, text=caption, command=(lambda button=caption: self.controller.on_button_click())
            )
            btn.pack(side='left')
