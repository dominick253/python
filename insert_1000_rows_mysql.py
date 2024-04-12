import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)
cursor = connection.cursor()

# Insert 1,000 rows
for i in range(1000):
    cursor.execute("INSERT INTO views (id) VALUES (NULL)")
    print(f"Inserted row {i + 1}")

# Commit changes and close connection
connection.commit()
cursor.close()
connection.close()
z