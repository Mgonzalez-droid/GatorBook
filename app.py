#FOR WEBPAGE SUPPORT
from flask import Flask, render_template, url_for, redirect, request, make_response

#FOR MYSQL CONNECTION
#import cx_Oracle
import mysql.connector
import os
import sys

#FOR GENERATING HTML CODE ON THE FLY
import html

# These pertain to the active user of the website
username = ""
password = ""
isAdmin = False
isLoggedIn = False
#cur =
#conn

# ____ W E B P A G E S ____
app = Flask(__name__)

@app.route('/')
def index():
    
    username = 'Not Logged in'
    resp = make_response(render_template('index.html', username = username))
    resp.set_cookie('username', username)

    return resp

@app.route('/Messenger')
def messenger():
    #query = "SELECT TITLE FROM MOVIE"

    #get cursor to render query
    cur, conn = connectMySql()

    #cur.execute(query)

    #result = cur.fetchall()

    #important close connection, after recieving data!
    cur.close()
    conn.close()
    return render_template('messenger.html')

@app.route('/Notifications')
def notifications():
    #query = "SELECT TITLE FROM MOVIE"

    #get cursor to render query
    cur, conn = connectMySql()

    #cur.execute(query)

    #result = cur.fetchall()

    #important close connection, after recieving data!
    cur.close()
    conn.close()
    return render_template('notifications.html')

@app.route('/Search')
def search():
    #query = "SELECT TITLE FROM MOVIE"

    #get cursor to render query
    cur, conn = connectMySql()

    #cur.execute(query)

    #result = cur.fetchall()

    #important close connection, after recieving data!
    cur.close()
    conn.close()
    return render_template('search.html')

@app.route('/Groups')
def groups():
    #query = "SELECT TITLE FROM MOVIE"

    #get cursor to render query
    cur, conn = connectMySql()

    #cur.execute(query)

    #result = cur.fetchall()

    #important close connection, after recieving data!
    cur.close()
    conn.close()
    return render_template('groups.html')

@app.route('/CreateUser')
def createUser():
    username = request.cookies.get('username')
    createMsg = 'Enter unique user credentials'

    return render_template('create_user.html',username = username, createMsg = createMsg)

@app.route('/CreateUserAuth', methods= ['POST', 'GET'])
def createUserAuth():
    if request.method == 'POST':
      
      username = request.form['username']
      password = request.form['password']

      query = 'SELECT * FROM user WHERE username = \'' + username +'\' AND password = \'' + password + '\''

      cur, conn = connectMySql()

      #get cursor to render query
      cur.execute(query)

      result = cur.fetchall()

      #important close connection, after recieving data!
      cur.close()
      conn.close()

      if len(result) > 0:
        username = request.cookies.get('username')
        
        if username:
            return make_response(render_template('create_user.html', username = username, createMsg = 'User already exists, try again'))
        else:
            username = 'Not Logged in'
            return make_response(render_template('create_user.html', username = username, createMsg = 'User already exists, try again'))

      else:
        #user was not found in database, insert into users table, set user in cookie, render custom page
        username = request.form['username']
        password = request.form['password']

        query = 'INSERT INTO user (username, password) VALUES (\'' + username + '\', \'' + password + '\')'

        cur, conn = connectMySql()

        #get cursor to render query
        cur.execute(query)

        #commit changes to the database
        conn.commit()

        resp = make_response(render_template('index.html', username = username))
        resp.set_cookie('username', username)

        #important close connection, after recieving data!
        cur.close()
        conn.close()

        return resp
        
    
    
    
    #query = "SELECT TITLE FROM MOVIE"

    #get cursor to render query
    cur, conn = connectMySql()

    #cur.execute(query)

    #result = cur.fetchall()

    #important close connection, after recieving data!
    cur.close()
    conn.close()
    return render_template('create_user.html')

@app.route('/Login')
def login():

    username = request.cookies.get('username')
    loginMsg = 'Enter Login Credentials'
    return  render_template('login.html', username = username, loginMsg = loginMsg)

@app.route('/LoginAuth', methods= ['POST', 'GET'])
def loginAuth():
    if request.method == 'POST':
      
      username = request.form['username']
      password = request.form['password']

      query = 'SELECT * FROM user WHERE username = \'' + username +'\' AND password = \'' + password + '\''

      cur, conn = connectMySql()

      #get cursor to render query
      cur.execute(query)

      result = cur.fetchall()

      if len(result) > 0:
        #user was found in database, set user in cookie and render custom page
        username = request.form['username']
        resp = make_response(render_template('index.html', username = username))
        resp.set_cookie('username', username)

        #important close connection, after recieving data!
        cur.close()
        conn.close()

        return resp
      else:
        
        username = request.cookies.get('username')

        if username:
            return make_response(render_template('login.html', username = username, loginMsg = 'Invalid Login Credentials'))
        else:
            username = 'Not Logged in'
            return make_response(render_template('login.html', username = username, loginMsg = 'Invalid Login Credentials'))


#____ O R A C L E  C O N N E C T I O N _____
def connectMySql():
    
    #Pull user name and password from text files
    #oracleUsername = ""
    #oraclePassword = ""
    #with open("Credentials/username.txt") as f:
    #    oracleUsername = f.readline()
    #with open("Credentials/password.txt") as f:
    #    oraclePassword = f.readline()

    #Create a connection

    conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database='gatorbookdb'
    )

    #Create cursor

    cur = conn.cursor()

    #return cursor
    return cur, conn


# Main entry point for application
if __name__ == "__main__":
    connectMySql()
    app.run(debug=True)