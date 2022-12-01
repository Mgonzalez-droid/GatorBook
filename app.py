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

#constants for clean code
NOT_LOGGED_IN = "Not Logged in"

INDEX_PAGE = "index.html"
LOGIN_PAGE = "login.html"
CREATE_USER_PAGE = "create_user.html"
MESSENGER_PAGE = "messenger.html"
NOTIFICATION_PAGE = "notifications.html"
SEARCH_PAGE = "search.html"
GROUPS_PAGE = "groups.html"

# ____ W E B P A G E S ____
app = Flask(__name__)

@app.route('/')
def Index():
    
    username = NOT_LOGGED_IN
    resp = make_response(render_template(INDEX_PAGE, username = username))
    resp.set_cookie('username', username)

    return resp

@app.route('/Messenger')
def Messenger():
    return render_template(MESSENGER_PAGE)

@app.route('/Notifications')
def Notifications():
    return render_template(NOTIFICATION_PAGE)

@app.route('/Search')
def Search():
    return render_template(SEARCH_PAGE)

@app.route('/Groups')
def Groups():
    return render_template(GROUPS_PAGE)

@app.route('/CreateUser')
def CreateUser():
    username = request.cookies.get('username')
    createMsg = 'Enter unique user credentials'

    return render_template(CREATE_USER_PAGE, username = username, createMsg = createMsg)

@app.route('/CreateUserAuth', methods= ['POST', 'GET'])
def CreateUserAuth():
    if request.method == 'POST':
      
      username = request.form['username']
      password = request.form['password']

      query = 'SELECT * FROM user WHERE username = \'' + username +'\' AND password = \'' + password + '\''

      cur, conn = ConnectMySql()

      #get cursor to render query
      cur.execute(query)

      result = cur.fetchall()

      #important close connection, after recieving data!
      cur.close()
      conn.close()

      if len(result) > 0:
        username = request.cookies.get('username')
        
        if username:
            return make_response(render_template(CREATE_USER_PAGE, username = username, createMsg = 'User already exists, try again'))
        else:
            username = NOT_LOGGED_IN
            return make_response(render_template(CREATE_USER_PAGE, username = username, createMsg = 'User already exists, try again'))

      else:
        #user was not found in database, insert into users table, set user in cookie, render custom page
        username = request.form['username']
        password = request.form['password']

        query = 'INSERT INTO user (username, password) VALUES (\'' + username + '\', \'' + password + '\')'

        cur, conn = ConnectMySql()

        #get cursor to render query
        cur.execute(query)

        #commit changes to the database
        conn.commit()

        resp = make_response(render_template(INDEX_PAGE, username = username))
        resp.set_cookie('username', username)

        #important close connection, after recieving data!
        cur.close()
        conn.close()

        return resp

@app.route('/Login')
def Login():
    username = request.cookies.get('username')
    loginMsg = 'Enter Login Credentials'
    return  render_template(LOGIN_PAGE, username = username, loginMsg = loginMsg)

@app.route('/LoginAuth', methods= ['POST', 'GET'])
def LoginAuth():
    if request.method == 'POST':
      
      username = request.form['username']
      password = request.form['password']

      query = 'SELECT * FROM user WHERE username = \'' + username +'\' AND password = \'' + password + '\''

      cur, conn = ConnectMySql()

      #get cursor to render query
      cur.execute(query)

      result = cur.fetchall()

      if len(result) > 0:
        #user was found in database, set user in cookie and render custom page
        username = request.form['username']
        resp = make_response(render_template(INDEX_PAGE, username = username))
        resp.set_cookie('username', username)

        #important close connection, after recieving data!
        cur.close()
        conn.close()

        return resp
      else:
        
        username = request.cookies.get('username')

        if username:
            return make_response(render_template(LOGIN_PAGE, username = username, loginMsg = 'Invalid Login Credentials'))
        else:
            username = NOT_LOGGED_IN
            return make_response(render_template(LOGIN_PAGE, username = username, loginMsg = 'Invalid Login Credentials'))


#____ M Y S Q L  C O N N E C T I O N _____
def ConnectMySql():

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
    ConnectMySql()
    app.run(debug=True)