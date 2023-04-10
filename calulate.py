
import sqlite3

# connect to the database
conn = sqlite3.connect('company.db')
c = conn.cursor()

# get date from user
date = input("Enter date (YYYY-MM-DD): ")

# count total number of employees
c.execute("SELECT COUNT(*) FROM employees")
total_employees = c.fetchone()[0]

# count number of employees present on given date
c.execute("SELECT COUNT(*) FROM attendance WHERE date = ? AND status = 'P'", (date,))
present_employees = c.fetchone()[0]

# calculate percentage of employees present
if total_employees > 0:
    percent_present = (present_employees / total_employees) * 100
else:
    percent_present = 0

# display results
print(f"On {date}, {present_employees} out of {total_employees} employees ({percent_present:.2f}%) were present.")

# close the database connection
conn.close()
