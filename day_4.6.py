# ================================================================
# SQLite3 CRUD Operations in Python (Without Pandas)
# ================================================================
import sqlite3

# ------------------------------------------------
# Connect to Database (creates if not exists)
# ------------------------------------------------
conn = sqlite3.connect("company.db")
cursor = conn.cursor()



# ------------------------------------------------
# 2. READ (Select Records)
# ------------------------------------------------
print("\n=== READ Records ===")
cursor.execute("SELECT * FROM ")
rows = cursor.fetchall()
for row in rows:
    print(row)

# ------------------------------------------------
# Close Connection
# ------------------------------------------------
conn.close()
print("\nDatabase connection closed.")




"""
cursor.execute() → Executes SQL commands.

? placeholders → Prevent SQL injection (safer queries).

conn.commit() → Saves changes (important after INSERT/UPDATE/DELETE).

fetchall() → Retrieves query results.



"""