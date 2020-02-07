from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rootroot'
app.config['MYSQL_DB'] = 'todo'

mysql = MySQL(app)



@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM list")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', list=data )




@app.route('/Notstarted')
def Notstarted():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM list where status_flag=0")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', list=data )

@app.route('/started')
def started():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM list where status_flag=1")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', list=data )

@app.route('/finished')
def finished():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM list where status_flag=2")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', list=data )


@app.route('/overdue')
def overdue():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM list where date < curdate() && status_flag <>2")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', list=data )

@app.route('/due')
def due():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM list where date >=curdate() && status_flag < 2")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', list=data )


@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        todo = request.form['TODO']
        status = request.form['status']
        if status=="Finished":
            status_flag = 2
        if status=="Started":
            status_flag = 1
        if status=="Notstarted":
            status_flag = 0
        date = request.form['date']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO list (TODO, status, status_flag,date) VALUES (%s, %s, %s, %s)", (todo, status, status_flag,date))
        mysql.connection.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM list WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        todo = request.form['TODO']
        status = request.form['status']
        if status=="Finished":
            status_flag = 2
        if status=="Started":
            status_flag = 1
        if status=="Notstarted":
            status_flag = 0
        date = request.form['date']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE list
               SET TODO=%s, status=%s, status_flag=%s,
               date=%s
               WHERE id=%s
            """, (todo, status, status_flag,date, id_data))
        mysql.connection.commit()
        return redirect(url_for('Index'))









if __name__ == "__main__":
    app.run(debug=True)
