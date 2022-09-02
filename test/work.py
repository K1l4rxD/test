from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__, template_folder='templates', static_folder='templates/')

# Mysql Connection
app.config['MYSQL_HOST'] = '192.168.1.2'
app.config['MYSQL_USER'] = 'omar'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'books_authors'
app.config['MYSQL_PORT'] = 3306
mysql = MySQL(app)

# settings
app.secret_key = 'mykey'

@app.route('/')
def index():

    return redirect(url_for('Reports'))

@app.route('/reports')
def Reports():
   
        
    cur = mysql.connection.cursor()
    sql = 'SELECT * FROM authors'
    cur.execute(sql)
    mysql.connection.commit()
    data = cur.fetchall()
    cur.close()
    
    return render_template('work.html', contacts = data)
    
@app.route('/insert')
def Insert():
   
    return render_template('insert.html') 
 
@app.route('/insert_data', methods=['POST'])
def Insert_data():
    
   if request.method == 'POST':
       AuthorName = request.form['AuthorName']
       AuthorCity = request.form['AuthorCity']
       Gender = request.form['Gender']
       BookTitle = request.form['BookTitle']
       ReleaseYear = request.form['ReleaseYear']
       NumberOfPages = request.form['NumberOfPages']
       PiecesSold = request.form['PiecesSold']
       
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO authors (AuthorName,AuthorCity,Genre,BookTitle,ReleaseYear,NumberOfPages,PiecesSold) VALUES (%s,%s,%s,%s,%s,%s,%s)',(AuthorName,AuthorCity,Gender,BookTitle,ReleaseYear,NumberOfPages,PiecesSold))
       mysql.connection.commit()
       cur.close()
       
       flash('Data registered correctly')
       
       
       return redirect(url_for('Reports')) 

@app.route('/edit/<int:id>')
def Edit(id):
    
    AuthorID = id
   
    return render_template('edit.html', contact = AuthorID)

@app.route('/edit_data', methods=['POST'])
def Edit_data():
    
   if request.method == 'POST':
       AuthorID = request.form['AuthorID']
       AuthorName = request.form['AuthorName']
       AuthorCity = request.form['AuthorCity']
       Gender = request.form['Gender']
       BookTitle = request.form['BookTitle']
       ReleaseYear = request.form['ReleaseYear']
       NumberOfPages = request.form['NumberOfPages']
       PiecesSold = request.form['PiecesSold']
       
       cur = mysql.connection.cursor()
       sql ='UPDATE authors SET AuthorName=%s, AuthorCity=%s, Genre=%s, BookTitle=%s, ReleaseYear=%s, NumberOfPages=%s, PiecesSold=%s WHERE AuthorID=%s'
       values = (AuthorName,AuthorCity,Gender,BookTitle,ReleaseYear,NumberOfPages,PiecesSold,AuthorID)
       cur.execute(sql, values)
       mysql.connection.commit()
       cur.close()

       flash('Data edited correctly')
       
       return redirect(url_for('Reports')) 

@app.route('/delete/<int:id>')
def Delete(id):
    
   
    AuthorID = id
      
    cur = mysql.connection.cursor()
    sql ='DELETE FROM authors WHERE AuthorID="{0}"'.format(AuthorID)
    cur.execute(sql)
    mysql.connection.commit()
    cur.close()

    flash('Data deleted correctly')
       
    return redirect(url_for('Reports'))

   
if __name__ == '__main__':
    app.run(host = "0.0.0.0" , port = 3000, debug = True)
