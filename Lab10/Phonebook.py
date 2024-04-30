import psycopg2
import csv

conn = psycopg2.connect(host = "localhost", dbname = "postgres", user="postgres", password = "damir2005d", port = "5432")
conn.autocommit = True
with conn.cursor() as cur:
   cur.execute(
        """CREATE TABLE Phonebook(
            id serial PRIMARY KEY,
            username VARCHAR(255),
            number VARCHAR(20));
             """)
with conn.cursor() as cur:
    cur.execute("INSERT INTO Phonebook (username, number) VALUES ('Damir', '+77083162100'), ('Ais', '+77017155141')")   


#Entering username/number from console

#Updating data
with conn.cursor() as cur:
    cur.execute(f"UPDATE Phonebook SET number = '+77084566789' WHERE username = 'Damir'")
    
#Querying data
with conn.cursor() as cur:
    cur.execute("SELECT * FROM Phonebook WHERE LENGTH(username) > 3")
    results = cur.fetchone()
    print(results)

#Deleting data
with conn.cursor() as cur:
    cur.execute("DELETE FROM Phonebook WHERE username = 'Tima'")
    