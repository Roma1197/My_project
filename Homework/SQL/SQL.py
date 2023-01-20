import sqlite3
from sqlite3 import Error

persons_table = '''
    CREATE DATABASE staff
'''


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection("D:\\sm_app.sqlite")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


persons_table = '''
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    birthdate TEXT NOT NULL
);
'''
execute_query(connection, persons_table)

create_persons = '''
INSERT INTO persons 
VALUES 
    (1, "Viktor_Zhitko", "11.04.1992"),
    (2, "Mykola_Melnyk", "15.05.1993")
'''
execute_query(connection, create_persons)

employees_table = '''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY, 
    position TEXT NOT NULL, 
    salary TEXT NOT NULL, 
    id_person INTEGER NOT NULL
);
'''
execute_query(connection, employees_table)

create_employees = '''
INSERT INTO employees 
VALUES
    (1, "Manager", "1000", 1),
    (2, "Sales_manager", "1500", 2)
'''
execute_query(connection, create_employees)

contacts_table = '''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY, 
    type TEXT NOT NULL, 
    value TEXT NOT NULL, 
    id_employees INTEGER NOT NULL,
    FOREIGN KEY (id_employees) REFERENCES employees (id)
);
'''
execute_query(connection, contacts_table)

create_contacts = '''
INSERT INTO contacts 
VALUES
    (1, "mobile_telephone", "+380675864125", 1),
    (2, "telegram", "@ZhitkoV", 1)
'''
execute_query(connection, create_contacts)


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


select_position_for_contact = '''
SELECT 
    contacts.type, 
    contacts.value, 
    employees.position 
FROM 
    employees 
INNER JOIN contacts ON employees.id = contacts.id_employees
'''

staff_positions = execute_read_query(connection, select_position_for_contact)
for staff_position in staff_positions:
    print(staff_position)

select_contacts_for_position = '''
SELECT 
    employees.position, 
    contacts.type, 
    contacts.value
FROM 
    contacts
INNER JOIN employees ON contacts.id_employees = employees.id
WHERE employees.id = 1
'''

staff_contacts = execute_read_query(connection, select_contacts_for_position)
print(staff_contacts)