#FOR WEBPAGE SUPPORT
from flask import Flask, render_template, url_for

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
    return render_template('index.html')

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
    )

    #Create cursor

    cur = conn.cursor()

    #return cursor
    return cur, conn


# Main entry point for application
if __name__ == "__main__":
    connectMySql()
    app.run(debug=True)