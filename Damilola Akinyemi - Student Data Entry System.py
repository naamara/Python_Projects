import sqlite3

# Establishing a connection with the database
con = sqlite3.connect("my_database.db")

# Cursor object is connected using the connection created
cur = con.cursor()


def create_student_table(con):
    cur = con.cursor()

# Creates student table
    cur.execute("CREATE TABLE IF NOT EXISTS students(roll_no INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL,"
                   " age INTEGER NOT NULL, course TEXT NOT NULL, email TEXT NOT NULL, phone INTEGER)")



def insert_student_table(roll_no, name, age, course, email, phone):
    cur = con.cursor()

# Inserts values into table created
    cur.execute("INSERT OR REPLACE INTO students VALUES(?, ?, ?, ?, ?, ?)",  (roll_no, name, age, course, email, phone))

con.commit()


create_student_table(con)
insert_student_table(1, 'Wendy', 17, 'English Language', 'charles10@gmail.com', 8123456787)
insert_student_table(2, 'Peter', 15, 'Chemical Engineering', 'peter20@yahoo.com', 9654676734)
insert_student_table(3, 'Mercy', 19, 'Theatre Arts', 'mercy30@gmail.com', 8056765476)
insert_student_table(4, 'Micheal', 16, 'Accounting', 'micheal40@gmail,com', 906742110)
insert_student_table(5, 'Tina', 20, 'Statistics', 'tina50@yahoo.com', 812300780)


def select_student_table():
    cur = con.cursor()

# Select all the table
    cur.execute("SELECT * FROM students")

con.commit()

def fetch_student_table():
    cur = con.cursor()
# This fetches all the rows in the table
    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()
    for row in rows:
        print(row)

# This returns a single row where the condition is met
    cur.execute("SELECT * FROM students age = 18")
    result = cur.fetchone()
    print(result)

# Selecting a row with conditions
    cur.execute("SELECT course,email FROM students WHERE age <= 17")
    rows = cur.fetchall()

    for row in rows:
        print(row)


def update_student_table():
    cur = con.cursor()

# Updating a table's info
    cur.execute("UPDATE students SET age = 23 WHERE name = 'Tina'")

    con.commit()


def delete_student_table():
    cur = con.cursor()

# Deleting a table row
    cur.execute("DELETE FROM students WHERE name = 'Tina'")

    con.commit()

# Deleting a table
    cur.execute("DROP TABLE IF NOT EXISTS students")

    con.commit()
