import csv
import mysql.connector

connection = mysql.connector.connect(user='root', host='127.0.0.1', database='bookreviews')
cursor = connection.cursor()

csv_data = csv.reader(open('books.csv'), delimiter=",")
for row in csv_data:
    cursor.execute("INSERT INTO books(isbn, title, author, year) VALUES(%s, %s, %s, %s)", row)

# close the connection to the database.


connection.commit()
cursor.close()
print("done!")
