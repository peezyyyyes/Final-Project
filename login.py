import sqlite3  # Import the sqlite3 module to work with SQLite databases
import hashlib  # Import the hashlib module for hashing passwords
# Connect to the SQLite database 'userdata.db' (creates it if it doesn't exist)
conn = sqlite3.connect('userdata.db')
# Create a cursor object to interact with the database
cur = conn.cursor()

# Execute a SQL command to create the 'userdata' table if it doesn't already exist
cur.execute("""CREATE TABLE IF NOT EXISTS userdata(
            Id INTEGER PRIMARY KEY, 
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
            )""")

# Define usernames and hash their corresponding passwords
username1, password1 = "Jamal", hashlib.sha256("12312312".encode()).hexdigest()
username2, password2 = "Miles", hashlib.sha256("67676767".encode()).hexdigest()
username3, password3 = "Shauna", hashlib.sha256("12367cats".encode()).hexdigest()
username4, password4 = "Ebony", hashlib.sha256("abcd123123".encode()).hexdigest()
username5, password5 = "Riley", hashlib.sha256("watermelon22".encode()).hexdigest()

# Insert the user data into the 'userdata' table
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username5, password5))



conn.commit()