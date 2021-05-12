import sqlite3


class Model:

    def __init__(self, name='', surname='', age='', position='', salary=''):
        self.name = name
        self.surname = surname
        self.age = age
        self.position = position
        self.salary = salary

    # Function responsible for adding new employee to the database
    def add_new_employee(self, name, surname, age, position, salary):
        connection = sqlite3.connect("employees_database.db")
        cursor = connection.cursor()

        cursor.execute("""
                INSERT INTO
                employees (name, surname, age, position , salary)
                VALUES
                (?, ?, ?, ?, ?)""", (name, surname, age, position, salary))

        connection.commit()

        cursor.close()
        connection.close()

    # Simple getters functions to retrieve data about employees

    def get_employees_name(self):
        connection = sqlite3.connect("employees_database.db")
        cursor = connection.cursor()
        cursor.execute("""
        SELECT name FROM employees
        """)

        rows = cursor.fetchall()

        connection.commit()
        cursor.close()
        connection.close()
        return rows

    def get_employees_surname(self):
        connection = sqlite3.connect("employees_database.db")
        cursor = connection.cursor()
        cursor.execute("""
        SELECT surname FROM employees
        """)

        rows = cursor.fetchall()

        connection.commit()
        cursor.close()
        connection.close()
        return rows

    def get_employees_position(self):
        connection = sqlite3.connect("employees_database.db")
        cursor = connection.cursor()
        cursor.execute("""
        SELECT position FROM employees
        """)

        rows = cursor.fetchall()

        connection.commit()
        cursor.close()
        connection.close()
        return rows

    def get_employees_age(self):
        connection = sqlite3.connect("employees_database.db")
        cursor = connection.cursor()
        cursor.execute("""
        SELECT age FROM employees
        """)

        rows = cursor.fetchall()

        connection.commit()
        cursor.close()
        connection.close()
        return rows

    def get_employees_salary(self):
        connection = sqlite3.connect("employees_database.db")
        cursor = connection.cursor()
        cursor.execute("""
        SELECT salary FROM employees
        """)

        rows = cursor.fetchall()

        connection.commit()
        cursor.close()
        connection.close()
        return rows

    # Delete employee with given id
    def delete_employee(self, id):
        connection = sqlite3.connect("employees_database.db")

        connection.commit()
        cursor = connection.cursor()
        cursor.execute("""
            DELETE from employees WHERE ID = ?
            """, (id,))

        connection.commit()
        cursor.close()
        connection.close()

    # Delete all employees from the table
    def delete_all_employees(self):
        connection = sqlite3.connect("employees_database.db")

        cursor = connection.cursor()
        cursor.execute("""
            DELETE from employees
            """)

        connection.commit()
        cursor.close()
        connection.close()

    # Getter which is responsible for retrieving data about specified by ID employee
    def get_employee_data_by_id(self, id):
        connection = sqlite3.connect("employees_database.db")
        cursor = connection.cursor()
        cursor.execute("""
            SELECT name, surname, age, position, salary from employees WHERE ID = ?""", (id,))

        data = cursor.fetchall()

        connection.commit()
        cursor.close()
        connection.close()
        return data

    # Update data about specified by ID employee
    def update_employee_data(self, name, surname, age, position, salary, id):
        connection = sqlite3.connect("employees_database.db")
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE employees 
            SET name = ? , surname = ?, age = ?, position = ?, salary = ? WHERE ID = ?
             """, (name, surname, age, position, salary, id,))

        connection.commit()
        cursor.close()
        connection.close()
