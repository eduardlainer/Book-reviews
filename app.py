from flask import Flask, session, render_template, redirect, url_for, request
import Database
import os
import requests

app = Flask(__name__)
app.secret_key = os.urandom(26)
db = Database.Database()


@app.route("/")
def index():
    if 'username' in session:
        return render_template("index.html")
    return render_template("login.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if db.username_exist(username) and db.check_password(username) != password:
            return render_template("login.html", message="Password incorrect!", alerttype="alert-danger")
        if db.user_exist(username, password):
            session['username'] = username
            return redirect(url_for('index'))
        return render_template("login.html", message="The user doesn't exist!", alerttype="alert-danger")
    return render_template("login.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        if db.username_exist(username):
            return render_template("registration.html", message="Username already exist!", alerttype="alert-danger")
        elif db.email_exist(email):
            return render_template("registration.html", message="Email already exist!", alerttype="alert-danger")
        db.add_user(username, password, email)
        return render_template("registration.html", message="User registerd! You can log in now.",
                               alerttype="alert-success")
    return render_template("registration.html")


@app.route('/books', methods=['GET', 'POST'])
def books():
    if 'username' in session:
        if request.method == "POST":
            whattosearch = request.form.get('searched')
            result = db.search_books(whattosearch)
            if not result:
                return render_template("index.html", message="No records in our database!", alerttype="alert-danger")
            return render_template("searchresult.html", result=result)
    return render_template("login.html")


@app.route('/books/<int:idbook>')
def books_info(idbook):
    if 'username' in session:
        bookdetails = db.book_details(idbook)
        isbn = ""
        for detail in bookdetails:
            isbn = detail[1]
        apires = requests.get("https://www.goodreads.com/book/review_counts.json",
                              params={"key": "KEY", "isbns": isbn})
        if apires.status_code == 200:
            result = apires.json()
            averagerating = result["books"][0]["average_rating"]
            ratingscount = result["books"][0]['work_ratings_count']
            return render_template("bookinfo.html", bookdetails=bookdetails,
                                   averagerating=averagerating,
                                   ratingscount=ratingscount)
        return render_template("error.html", message="Can't connect to the server try again later!")
    return render_template("index.html")


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
