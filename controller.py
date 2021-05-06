from model import Model
from view import View
from employee_database import Database


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.employee_database = Database()

    def main(self):
        self.employee_database.create_database()
        self.view.main()

    # Get values from entry widgets, from the view class then pass it to the model to function responsible for adding a new record for database
    def add_new_employee(self, name, surname, age, position, salary):
        self.model.add_new_employee(name, surname, age, position, salary)


if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
