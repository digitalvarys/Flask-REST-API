import pymysql
from dbconfig importMySql
from app import app
from flask import Flask, jsonify, request

# CRUD Operation - CREATE 
@app.route('/add', methods=['POST'])
def add_book():
	try:
		json = request.json
		Book_name = json['book_name']
		Author_name = json['author_name']
		Publisher_name = json['publisher_name']
		if Book_name and Author_name and Publisher_name and request.method == 'POST':
			SQL_Query = "INSERT INTO books(Book_name, Author_name, Publisher_name) VALUES(%s, %s, %s)"
			data = (Book_name, Author_name, Publisher_name,)
			connection =MySql.connect()
			Pointer = connection.cursor()
			Pointer.execute(SQL_Query, data)
			connection.commit()
			response = jsonify('Book added!')
			response.status_code = 200
			return response
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		Pointer.close() 
		connection.close()
		
#CRUD Operation - READ			
@app.route('/book/<int:id>')
def book(id):
	try:
		connection =MySql.connect()
		Pointer = connection.cursor(pymysql.cursors.DictCursor)
		Pointer.execute("SELECT * FROM books WHERE book_id=%s", id)
		record = Pointer.fetchone()
		response = jsonify(record)
		response.status_code = 200
		return response
	except Exception as e:
		print(e)
	finally:
		Pointer.close() 
		connection.close()

#CRUD Operation - UPDATE	
@app.route('/update', methods=['POST'])
def update_book():
	try:
		json = request.json
		id = json['id']
		Book_name = json['Book_name']
		Author_name = json['Author_name']
		Publisher_name = json['Publisher_name']		
		if Book_name and Author_name and Publisher_name and id and request.method == 'POST':
			SQL_Query = "UPDATE books SET Book_name=%s, Author_name=%s, Publisher_name=%s WHERE book_id=%s"
			data = (Book_name, Author_name, Publisher_name, id,)
			connection =MySql.connect()
			Pointer = connection.cursor()
			Pointer.execute(sql, data)
			connection.commit()
			response = jsonify('Book updated!')
			response.status_code = 200
			return response
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		Pointer.close() 
		connection.close()

#CRUD Operation - DELETE		
@app.route('/delete/<int:id>')
def delete_book(id):
	try:
		connection =MySql.connect()
		Pointer = connection.cursor()
		Pointer.execute("DELETE FROM books WHERE book_id=%s", (id,))
		connection.commit()
		response = jsonify('book deleted!')
		response.status_code = 200
		return response
	except Exception as e:
		print(e)
	finally:
		Pointer.close() 
		connection.close()
		
if __name__ == "__main__":
    app.run()