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

    # Get values from entry widgets, from the view class then pass it to the model to function responsible for
    # Adding a new record for database
    def add_new_employee(self, name, surname, age, position, salary):
        self.model.add_new_employee(name, surname, age, position, salary)

    # Getter methods - getting specified value from database, such as name, surname etc.
    # And pass all of it to the tuple in View
    def get_employees_name(self):
        rows = self.model.get_employees_name()
        for i in rows:
            self.view.name_tuple.append(i)

    def get_employees_surname(self):
        rows = self.model.get_employees_surname()
        for i in rows:
            self.view.surname_tuple.append(i)

    def get_employees_age(self):
        rows = self.model.get_employees_age()
        for i in rows:
            self.view.age_tuple.append(i)

    def get_employees_position(self):
        rows = self.model.get_employees_position()
        for i in rows:
            self.view.position_tuple.append(i)

    def get_employees_salary(self):
        rows = self.model.get_employees_salary()
        for i in rows:
            self.view.salary_tuple.append(i)


if __name__ == '__main__':
    controller = Controller()
    controller.main()
