import sqlite3
import os


def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor


def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE Students (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        age INTEGER,
        email VARCHAR UNIQUE,
        city VARCHAR)
        ''')

    cursor.execute('''
        CREATE TABLE Courses (
            id INTEGER PRIMARY KEY,
            course name VARCHAR NOT NULL,
            instructor TEXT,
            credits INTEGER)
            ''')


def insert_sample_data(cursor):
    student = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle'),
    ]

    cursor.executemany('INSERT INTO Students VALUES (?,?,?,? ,?)', student)

    courses = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2),
    ]

    cursor.executemany('INSERT INTO Courses VALUES (?,?,?,?)', courses)

    print("Sample Data Inserted successfully")


def basic_sql_operations(cursor):
    #1) SELECT ALL
    print("---------------Select ALL -------------------")
    cursor.execute(" SELECT * FROM Students ")
    records = cursor.fetchall()
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}")

    # 2) SELECT Columns
    print("---------------Select Columns -------------------")
    cursor.execute(" SELECT name,age FROM Students ")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # 3) WHERE clause
    print("---------------WHERE clause -------------------")
    cursor.execute(" SELECT * FROM Students WHERE age = 20")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # 4) WHERE with string
    print("---------------WHERE city = New York -------------------")
    cursor.execute(" SELECT * FROM Students WHERE city = 'New York'")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # 5) ORDER BY
    print("---------------Order by age -------------------")
    cursor.execute(" SELECT * FROM Students ORDER BY age")
    records = cursor.fetchall()
    for row in records:
        print(row)


    # 6) LIMIT
    print("---------------limit by 3 -------------------")
    cursor.execute(" SELECT * FROM Students LIMIT 3 ")
    records = cursor.fetchall()
    for row in records:
        print(row)

def sql_update_delete_insert_operations(conn, cursor):

    #1)Insert
    cursor.execute("INSERT INTO Students VALUES (6, 'Frank Miller', 23, 'frank@gmail.com', 'Miami')")
    conn.commit()

    #2) UPDATE
    cursor.execute(" UPDATE Students SET age = 24 WHERE id = 6 ")
    conn.commit()

    #3) DELETE
    cursor.execute(" DELETE FROM Students WHERE id = 6")
    conn.commit()


def aggregate_functions(cursor):
    #1) Count
    print("---------------Aggregate Functions  Count-------------------")
    cursor.execute("SELECT COUNT(*) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    #2) Avarage
    print("---------------Aggregate Functions  Avarage-------------------")
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    #3) MAX - MIN
    print("---------------Aggregate Functions  max- min -------------------")
    cursor.execute("SELECT MAX(age),MIN(age) FROM Students")
    result = cursor.fetchone()
    max_age, min_age = result
    print(max_age)
    print(min_age)

    # 4) GROUP BY
    print("---------------Aggregate Functions  Group by -------------------")
    cursor.execute("SELECT city, COUNT(*) FROM Students GROUP BY city")
    result = cursor.fetchall()
    print(result)

def questions():
    '''
    Basit
    1) Bütün kursların bilgilerini getirin
    2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin
    3) Sadece 21 yaşındaki öğrencileri getirin
    4) Sadece Chicago'da yaşayan öğrencileri getirin
    5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    6) Sadece ismi 'A' ile başlayan öğrencileri getirin
    7) Sadece 3 ve üzeri kredi olan dersleri getirin

    Detaylı
    1) Öğrencileri alphabetic şekilde dizerek getirin
    2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin
    3) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin
    4) Sadece 'New York' ta yaşamayan öğrencileri getirin
    '''


def answers(cursor):
    print("----------Sınav Cevapları----------")
    # Basit
    print("1. Bütün kursların bilgilerini getirin")
    cursor.execute("SELECT * FROM Courses")
    print(cursor.fetchall())

    print("2. Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin")
    cursor.execute("SELECT course_name, instructor FROM Courses")
    print(cursor.fetchall())

    print("3. Sadece 21 yaşındaki öğrencileri getirin")
    cursor.execute("SELECT * FROM Students WHERE age = 21")
    print(cursor.fetchall())

    print("4. Sadece Chicago'da yaşayan öğrencileri getirin")
    cursor.execute("SELECT * FROM Students WHERE city = 'Chicago'")
    print(cursor.fetchall())

    print("5. Sadece 'Dr. Anderson' tarafından verilen dersleri getirin")
    cursor.execute("SELECT * FROM Courses WHERE instructor = 'Dr. Anderson'")
    print(cursor.fetchall())

    print("6. Sadece ismi 'A' ile başlayan öğrencileri getirin")
    cursor.execute("SELECT * FROM Students WHERE name LIKE 'A%'")
    print(cursor.fetchall())

    print("7. Sadece 3 ve üzeri kredi olan dersleri getirin")
    cursor.execute("SELECT * FROM Courses WHERE credits >= 3")
    print(cursor.fetchall())

    # Detaylı

    print("1. Öğrencileri alphabetic şekilde dizerek getirin")
    cursor.execute("SELECT * FROM Students ORDER BY name")
    print(cursor.fetchall())

    print("2. 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin")
    cursor.execute("SELECT name, age FROM Students WHERE age > 20 ORDER BY name")
    print(cursor.fetchall())

    print("3. Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin")
    cursor.execute("SELECT name, city FROM Students WHERE city IN ('New York', 'Chicago')")
    print(cursor.fetchall())

    print("4. Sadece 'New York' ta yaşamayan öğrencileri getirin")
    cursor.execute("SELECT name, city FROM Students WHERE city != 'New York'")
    print(cursor.fetchall())

def main():
    conn, cursor = create_database()

    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_update_delete_insert_operations(conn, cursor)
        aggregate_functions(cursor)
        answers(cursor)
        conn.commit()

    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == "__main__":
    main()

