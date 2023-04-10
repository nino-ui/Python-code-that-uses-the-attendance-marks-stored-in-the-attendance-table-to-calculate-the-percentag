in this code, we first connect to the company.db database using the sqlite3 module. We then prompt the user to enter a date for which they want to calculate the percentage of employees present.

We then count the total number of employees in the employees table using a SELECT COUNT(*) statement. We use a similar SELECT COUNT(*) statement to count the number of employees who were present on the given date and store the result in the present_employees variable.

We then calculate the percentage of employees present by dividing the number of present employees by the total number of employees and multiplying by 100. If there are no employees in the database, we set the percentage to 0.

Finally, we display the results to the user using an f-string that includes the date, number of present employees, total number of employees, and percentage of employees prese