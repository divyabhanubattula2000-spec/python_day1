import sql.connector
import pandas as pd
import matplotlib.pyplot as plt
# ------------------------------------------------
# Connect to MySQL Database
# ------------------------------------------------
mydb = mysql.connector.connect(
    host="project-b-dr-cluster.cluster-cprsywmazgvp.ap-southeast-1.rds.amazonaws.com",
    user="dr_etl_user",
    password="8Y5MjUh7SB&gE4A#",
    port="3306",
    database="ccbuser"
)


df_sql = pd.read_sql("SELECT * FROM employees", conn)
print("=== Employees Data from SQLite ===")
print(df_sql)




print("\n=== Employees with Salary > 55,000 ===")
high_salary = df_sql[df_sql['price_charged'] > 55]
print(high_salary)

print("\n=== Employees aged below 30 ===")
young_employees = df_sql[df_sql['quantity'] < 30]
print(young_employees)

conn.close()
print("\nDatabase connection closed.")