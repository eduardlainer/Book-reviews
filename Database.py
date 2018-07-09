import mysql.connector
import Models


class Database:

    # connecting to database and add cursor

    connection = mysql.connector.connect(user='root', host='127.0.0.1', database='bookreviews')
    cursor = connection.cursor()

    # Add user

    def add_user(self, username, password, email):
        user = Models.Users(username, password, email)
        query = ("INSERT INTO users (username,password,email) VALUES (%s, %s, %s)")
        self.cursor.execute(query, (user.username, user.password, user.email))
        self.connection.commit()

    # get user with that username and password

    def user_exist(self, username, password):
        query = ("SELECT COUNT(*) FROM users WHERE username=%s AND password=%s")
        self.cursor.execute(query, (username, password))
        result = self.cursor.fetchone()[0]
        if result > 0:
            return True
        else:
            return False

    # Check username exist

    def username_exist(self, username):
        query = ("SELECT COUNT(*) FROM users WHERE username=%s")
        self.cursor.execute(query, (username,))
        result = self.cursor.fetchone()[0]
        if result > 0:
            return True
        else:
            return False

    # Check correct password

    def check_password(self, username):
        query = ("SELECT password FROM users WHERE username=%s")
        self.cursor.execute(query, (username,))
        result = self.cursor.fetchone()[0]
        return result

    # Check if email exist

    def email_exist(self, email):
        query = ("SELECT COUNT(*) FROM users WHERE email=%s")
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchone()[0]
        if result > 0:
            return True
        else:
            return False

    # Get searched book info

    def search_books(self, info):
        query = ("SELECT id, isbn, title, author, year FROM books")
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        list = []
        finallist = []
        for res in result:
            list.append(res)
        for i in list:
            for j in i:
                if str(info).lower() in str(j).lower():
                    finallist.append(i)
        return finallist

    # Get searched book more details

    def book_details(self, info):
        query = ("SELECT id, isbn, title, author, year FROM books WHERE id=%s")
        self.cursor.execute(query, (info,))
        result = self.cursor.fetchall()
        list = []
        for res in result:
            list.append(res)
        return list
