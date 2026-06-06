import sqlite3
from index import *

conn = sqlite3.connect("32_SQLite/employee.db")

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
# first text,
# last text,
# pay integer
#     )""")

emp1 = Employee("Chotiya","Bhutiya",10101010)
emp2 = Employee("Bulla","Kholla",9999999999)
emp3 = Employee("Amitabh","Baccha",222222222)

employees = [emp1,emp2,emp3]

# for emp in employees:
#     c.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{
#         "first":emp.first,
#         "last":emp.last,
#         "pay":emp.pay
#     })

conn.commit()
# c.execute("INSERT INTO employees VALUES ('Gopal','Sharma',6969696)")
# c.execute("INSERT INTO employees VALUES ('Gopal','Verma',78787878)")
# c.execute("INSERT INTO employees VALUES ('Ram','Verma',676767)")
# c.execute("INSERT INTO employees VALUES ('Ram','Sharma',91919919)")

c.execute("SELECT * FROM employees WHERE first=?",("Chotiya",))



print(c.fetchall())

conn.commit()
conn.close()