### Book reviews
A flask application to check for book informations and reviews

### Import books in database
* books.csv - books details
* import.py - python script to import books in database

### Database structure
Database:

* bookreviews

Tables:

* users: id(INT AUTO-INCREMENT),  username(VARCHAR),  password(VARCHAR),  email(VARCHAR) 
* books: id(INT AUTO-INCREMENT),  isbn(VARCHAR),  title(VARCHAR),  author(VARCHAR),  year(INT) 

### API used

```
- https://www.goodreads.com/api
- change 'KEY' in app.py with your developer key
- ex: requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "KEY", "isbns": isbn})
```
