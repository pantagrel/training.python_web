from flask import Flask, render_template
import bookdb

app = Flask(__name__)

db = bookdb.BookDB()

@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)


@app.route('/')
def books(): 
	books = db.titles()
	return render_template('book_list.html', books=books )


@app.route('/book/<book_id>/')
def book(book_id):
	book = db.title_info(book_id)
	return render_template('book_detail.html', book=book)


if __name__ == '__main__':
    app.run(debug=True)
