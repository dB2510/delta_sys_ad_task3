import mysql.connector, os
import re
from werkzeug.security import generate_password_hash,check_password_hash
from flask import Flask, render_template, url_for, request, session, redirect, make_response
app = Flask(__name__)
cnx = mysql.connector.connect(user='cheevu_rs',password="dummy123",database="lp")
cursor = cnx.cursor()
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

@app.route('/temp')
def temp():
    return render_template('temp.html')
@app.route('/')
def base():
    if session:
        user = session['username']
        queryt = "SELECT count FROM USER WHERE userName='%s'"
        queryt1 = "UPDATE USER SET count=count+1 WHERE userName='%s'"
        cursor.execute(queryt1%user)
        cursor.execute(queryt%user)
        count = cursor.fetchall()
        cnx.commit()
        return render_template('index.html',user=user,count = count,f=0)
    else:
        return render_template('base.html')


@app.route('/index')
def index():
    if session:
        user = session['username']
        queryt = "SELECT count FROM USER WHERE userName='%s'"
        queryt1 = "UPDATE USER SET count=count+1 WHERE userName='%s'"
        cursor.execute(queryt1%user)
        cursor.execute(queryt%user)
        count = cursor.fetchall()
        cnx.commit()
        return render_template('index.html',user=user,count = count,f=0)
    else:
        return render_template('index.html',f=0)
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register',methods=['POST'])
def register_po():
    cnx = mysql.connector.connect(user='cheevu_rs',password="dummy123",database="lp")
    cursor = cnx.cursor()
    result = request.form
    if len(result['username']) <4 or len(result['username']) >11 :
        return render_template('error.html',ret=1)
    if result['fullname']=="":
        return render_template('error.html',ret=2)
    if not re.match(r"[^@]+@[^@]+\.[^@]+",result['email']):
        return render_template('error.html',ret=3)
    if len(result['password'])<4 and re.match(r"[a-z]/i", result['password']) and re.match(r"[0-9]", result['password']) and set('[~!@#$%^&*()_+{}":;\']+$').intersection(result['password']) :
        return render_template('error.html',ret=4)
    if result['password'] != result['rpassword']:
        return render_template('error.html',ret=5)
    query = "SELECT * FROM USER WHERE userName='%s'"
    user = result['username']
    cursor.execute(query%user)
    res = cursor.fetchone()
    if res:
        return render_template('login.html')
    else:
        pwd = generate_password_hash(result['password'])
        query1="INSERT INTO USER(userName,fullName,email,password_hash,count) VALUES('%s','%s','%s','%s',0)"
        cursor.execute(query1%(result['username'],result['fullname'],result['email'],pwd))
        cnx.commit()
        return render_template('success.html',result=result)

@app.route('/login')
def login():
    name1 = request.cookies
    if 'userId' in name1:
        name = name1['userId']
        queryt = "SELECT count FROM USER WHERE userName='%s'"
        queryt1 = "UPDATE USER SET count=count+1 WHERE userName='%s'"
        cursor.execute(queryt1%name)
        cursor.execute(queryt%name)
        count = cursor.fetchall()
        cnx.commit()
        session['username']=name
        return render_template('index.html',user=name,count=count,f=1)
    else:
        return render_template('login.html')

@app.route('/login',methods=['POST'])
def login_po():
    result = request.form
    query = "SELECT * FROM USER WHERE userName='%s'"
    user = result['username']
    cursor.execute(query%user)
    pwd = result['password']
    res = cursor.fetchone()
    if res:
        queryp = "SELECT password_hash from USER where userName='%s'"
        cursor.execute(queryp%user)
        rows = cursor.fetchall()
        for r in rows:
            for d in r:
                pwdd = d
        if check_password_hash(pwdd,pwd):
            queryt = "SELECT count FROM USER WHERE userName='%s'"
            queryt1 = "UPDATE USER SET count=count+1 WHERE userName='%s'"
            cursor.execute(queryt1%user)
            cursor.execute(queryt%user)
            count = cursor.fetchall()
            cnx.commit()
            session['username']=user
            return render_template('index.html',user=user,result=result,count=count,f=0)
        else:
            return render_template('errorL.html')
    else:
        return render_template('register.html')

@app.route('/logout')
def logout():
    user = session['username']
    session.pop('username',None)
    return render_template('logout.html',user=user)

if __name__ == '__main__':
   app.run(debug = True)
