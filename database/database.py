import sqlite3

def open_connection():
    connection = sqlite3.connect("exercise.db")
    cursor = connection.cursor()
    return connection, cursor

def close_connection(connection, cursor):
    connection.close()

def db_query(query, params = None):
    try:
        connection, cursor = open_connection()
        if params:
            cursor.execute(query)
            connection.commit()
        else:
            for row in cursor.execute(query):
                print(row)
    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        close_connection(connection, cursor)

def exercise1():
    query = "SELECT first_name, last_name FROM employees WHERE salary BETWEEN 10000 AND 15000"
    db_query(query)

def exercise2():
    query = "SELECT first_name, last_name, department_id FROM employees WHERE department_id BETWEEN 30 AND 100 ORDER BY department_id ASC"
    db_query(query)

def exercise3():
    query = "SELECT first_name, last_name, salary FROM employees WHERE salary BETWEEN 10000 AND 15000 limit 30"
    db_query(query)

def exercise4():
    query = "SELECT first_name, last_name, FROM employees WHERE first_name LIKE '%B%C%'"
    db_query(query)

def exercise5():
    query = "SELECT first_name, last_name, salary, job_id FROM employees WHERE job_id LIKE '%CLERK' OR 'IT%'"
    db_query(query)

def exercise6():
    query = "SELECT first_name, last_name FROM employees WHERE LENGTH(last_name) = 6"
    db_query(query)

def exercise7():
    query = "SELECT first_name, last_name FROM employees WHERE last_name LIKE '__e%'"
    db_query(query)




def exercise_1():
    query = "SELECT DISTINCT job_id FROM employees"
    db_query(query)

def exercise_2():
    query = "SELECT SUM(salary) as total_salary FROM employees"
    db_query(query)

def exercise_3():
    query = "SELECT salary FROM employees ORDER by salary ASC LIMIT 1"
    db_query(query)

def exercise_4():
    query = "SELECT salary FROM employees ORDER by salary DESC LIMIT 1"
    db_query(query)

def exercise_5():
    query = "SELECT AVG(salary) as avg_salary, COUNT(employee_id) FROM employees WHERE department_id = 90"
    db_query(query)

def exercise_6():
    query = "SELECT MIN(salary), MAX(salary), SUM(salary), AVG(salary) FROM employees"
    db_query(query)

def exercise_7():
    query = "SELECT job_id, COUNT(*)  FROM employees GROUP BY job_id"
    db_query(query)

def exercise_8():
    query = "SELECT (MAX(salary) - MIN(salary)) as DIF_salary FROM employees"
    db_query(query)

def exercise_9():
    query = "SELECT department_id, SUM(salary) FROM employees GROUP BY department_id"
    db_query(query)

def exercise_10():
    query = "SELECT AVG(salary), job_id FROM employees WHERE job_id NOT LIKE 'IT%'"
    db_query(query)

#exercise_10()

def create_view():
    query = """CREATE VIEW IF NOT EXISTS names
            as
            SELECT
                first_name,
                last_name
            FROM employees"""
    query_database(query)
    query_database("SELECT * FROM names")


# create_view()

def get_all():
    query = "SELECT * FROM employees"
    db_query(query)


def get_3_1():
    query = """SELECT first_name, last_name, salary  FROM employees
    WHERE salary > (SELECT salary FROM employees WHERE last_name="Bull")"""
    db_query(query)


def get_3_2():
    query = """SELECT first_name, last_name, job_id, manager_id  FROM employees
    WHERE employee_id IN (SELECT manager_id FROM employees)"""
    db_query(query)


def get_3_3():
    query = """SELECT first_name, last_name, salary FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)"""
    db_query(query)


def get_3_4():
    query = """SELECT first_name, job_id, last_name, salary 
        FROM employees
        WHERE salary = (SELECT min_salary FROM jobs WHERE employees.job_id = jobs.job_id)"""
    db_query(query)


def get_3_5():
    query = """SELECT first_name, last_name, salary FROM employees
        WHERE department_id IN (SELECT department_id FROM departments WHEREdepartment_name LIKE "IT%")"""
    db_query(query)

def get_3_6():
    query = """SELECT salary FROM employees
        WHERE salary IN (SELECT salary FROM employees ORDER BY salary DESC LIMIT 3)"""
    db_query(query)

def get_3_7():
    query = """SELECT first_name, last_name FROM employees
        WHERE salary IN (SELECT salary FROM employees ORDER BY salary DESC LIMIT 3)"""
    db_query(query)

def get_3_8():
    query = """SELECT * FROM locations"""
    db_query(query)

# get_3_2()
# get_all()
# get_3_1()
# get_3_3()
# get_3_4()
get_3_5()
# get_3_6()
#get_3_7()
#get_3_8()