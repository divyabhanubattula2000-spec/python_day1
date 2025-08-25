# ================================================================
# MySQL CRUD Operations with Python (mysql.connector)
# ================================================================
import mysql.connector

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

mycursor = mydb.cursor()


# ------------------------------------------------
# 2. READ (Select Records)
# ------------------------------------------------
mycursor.execute("SELECT * FROM account limit 10")
rows = mycursor.fetchall()
for row in rows:
    print("\n=== READ Records ===")
print(row)



mycursor.execute("SELECT * FROM account limit 10")
for row in mycursor.fetchall():
    print(row)

# --------------------------------
# ------------------------------------------------
# Close Connection
# ------------------------------------------------
mycursor.close()
mydb.close()
print("\nDatabase connection closed.")
