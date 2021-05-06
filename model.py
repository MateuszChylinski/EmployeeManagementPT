import sqlite3


class Model:

    def __init__(self, name='', surname='', age='', position='', salary=''):
        self.name = name
        self.surname = surname
        self.age = age
        self.position = position
        self.salary = salary

    # Temporary way to populate database
    def insert_dummy_data(self):
        connection = sqlite3.connect("employees_database.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO
        employees (name, surname, age, position , salary)
        VALUES
        ('Lorem','Ipsum',1,'Position1',0000)""")

        connection.commit()

        cursor.close()
        connection.close()

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

    def get_all_employees(self):
        connection = sqlite3.connect("employees_database.db")
        cursor = connection.cursor()
        cursor.execute("""
        SELECT name FROM employees
        """)

        rows = cursor.fetchall()

        cursor.close()
        connection.close()
        return rows
