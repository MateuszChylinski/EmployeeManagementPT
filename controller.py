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

    # Delete employee using given ID
    def delete_employee_by_id(self, id):
        self.model.delete_employee(id)

    # Delete all employees from the table
    def delete_all_employees(self):
        self.model.delete_all_employees()

    # Retrieve data about specified by id employee, and fill entry widgets with suitable data
    def get_employee_data_by_id(self, id):
        data = self.model.get_employee_data_by_id(id)

        for i in data:
            self.view.edit_employee_name.set(i[0])
            self.view.edit_employee_surname.set(i[1])
            self.view.edit_employee_age.set(i[2])
            self.view.edit_employee_position.set(i[3])
            self.view.edit_employee_salary.set(i[4])

    # Update specified employee
    def update_employee_data(self, name, surname, age, position, salary, id):

        print("name")
        print(repr(name), type(name))
        print("\nsurname")
        print(repr(surname), type(surname))

        print("\nage")
        print(repr(age), type(age))
        print("\nposition")
        print(repr(position), type(position))

        print("\nsalary")
        print(repr(salary), type(salary))
        print("\nid")
        print(repr(id), type(id))

        self.model.update_employee_data(name, surname, age, position, salary, id)


if __name__ == '__main__':
    controller = Controller()
    controller.main()
