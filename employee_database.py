import sqlite3


class Database:

    def create_database(self):
        # create database and cursor to manage data in it
        connection = sqlite3.connect('employees_database.db')
        cursor = connection.cursor()

        # create employees table
        employees_table = """CREATE TABLE IF NOT EXISTS 
                        employees(id INTEGER PRIMARY KEY, name TEXT, surname TEXT, age INTEGER,
                        position TEXT, salary INTEGER)"""

        cursor.execute(employees_table)
