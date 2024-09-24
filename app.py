from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='./templates/static')

# Настройки для подключения к MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'nero'
app.config['MYSQL_PASSWORD'] = '1212'
app.config['MYSQL_DB'] = 'umbrella'

mysql = MySQL(app)
app.secret_key = 'Umbrella'

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/doctor', methods=['GET', 'POST'])
def doctor_page():
    if 'regname' in session:
        regname = session['regname']
        return render_template('doctor.html', RegisName=regname)
    else:
        flash('Пожалуйста, войдите в систему.')
        return redirect(url_for('login'))

@app.route("/docGr")
def doctorGr():
    return render_template("doctorGraphics.html")

@app.route("/spCard")
def SpCart():
    return render_template("SpisocCart.html")

@app.route("/ZapPac")
def ZapPac():
    return render_template("ZapisPacientov.html")


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM reg WHERE email = %s AND password = %s", (email, password))
    user = cur.fetchone()
    cur.close()

    if user:
        role = user[6]
        session['regname'] = user[1]
        if role == "Доктор":
            return redirect(url_for('doctor_page'))
        elif role == "Пациент":
            return redirect(url_for('patient_page'))
        else:
            flash('Неверная роль пользователя')
            return redirect(url_for('main'))
    else:
        flash('Неверный email или пароль')
        return redirect(url_for('main'))



@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    building_code = request.form['buildingCode']
    role_code = request.form['roleCode']
    role = request.form['role']
    password = request.form['password']
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM reg WHERE email = %s", (email,))
    existing_user = cur.fetchone()

    if existing_user:
        cur.close()
        return redirect(url_for('main'))
    cur.execute("""
        INSERT INTO reg (regname, email, building_code, role_code, role, password) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (name, email, building_code, role_code, role, password))
    mysql.connection.commit()
    cur.close()

    if role == "Доктор":
         return redirect(url_for('doctor_page'))
    elif role == "Пациент":
        return redirect(url_for('patient_page'))
    else:
        flash('Неверная роль пользователя')
        return redirect(url_for('main'))


@app.route('/patient')
def patient_page():
    return render_template("patient.html")






if __name__ == "__main__":
    app.run(debug=True)
