import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('D:\VirtualKey\emotions.db')
cursor = conn.cursor()

# Retrieve all records from the Emotions table
cursor.execute('SELECT * FROM Emotions')
records = cursor.fetchall()

# Display the records
for record in records:
    print("ID:", record[0])
    print("Joy:", record[1])
    print("Anger:", record[2])
    print("Love:", record[3])
    print("Sadness:", record[4])
    print("Fear:", record[5])
    print("Surprise:", record[6])
    print("Timestamp:", record[7])
    print("\n")

# Close the connection
conn.close()