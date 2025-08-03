# sqlite.py

import sqlite3

# Connect to database

# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("customer.db")

# create a cursor. CURSOR: tells the database what you want to do
c = conn.cursor()

# Delete Table
c.execute("DROP TABLE customers")
conn.commit()


# Delete Records
# c.execute("DELETE from customers WHERE rowid = 9")


# Update Records
# c.execute(""" UPDATE customers SET first_name = 'mehmet'
#           WHERE rowid = 4
# """)

# conn.commit()

# Query The Database
# c.execute("SELECT  rowid, * FROM customers WHERE first_name = 'zeynep'")
# c.execute("SELECT  rowid, * FROM customers WHERE last_name LIKE 'Na%' ")
# c.execute("SELECT  rowid, * FROM customers WHERE email LIKE '%gmail.com' ")
# c.execute("SELECT  rowid, * FROM customers")
# c.execute("SELECT  rowid, * FROM customers LIMIT 2")


# Order Results By
# c.execute("SELECT  rowid, * FROM customers ORDER BY rowid DESC")
c.execute("SELECT  rowid, * FROM customers ORDER BY rowid DESC LIMIT 4")




# print(c.fetchone())
# print(c.fetchmany(3))
# print(c.fetchall())

# Format Results
# print(c.fetchone()[0])  #The result is a tuple so you can access subelements with index

items = c.fetchall()
for item in items:
    print(item)

# Create a table
# c.execute("""CREATE TABLE customers (
#           first_name text,
#           last_name text,
#           email text
#           )
# """)

# many_customers = [
#     ('Muhammed', 'NAMLI', 'mvelinamli@gmail.com'),
#     ('Veli', 'NAMLI', 'sadeceveli@gmail.com'),
#     ('Lorem', 'Ipsum', 'Dolor')
# ]

#  INSERT DATA
# c.execute("INSERT INTO customers VALUES ('zeynep', 'namli', 'mzeynepnamli@gmail.com')")   #insert one record into table

# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)   #insert many recor into table


#   DATATYPES:
#   NULL : DOESN'T EXIST
#   INTEGER : NUMBERS
#   REAL : DECIMAL (FLOAT)
#   TEXT : STRINGS
#   BLOB : OTHERS (IMAGES, MP3 ETC.)

# Commit our command. Thats common side other databases. 
conn.commit()

# Close our connection
conn.close()