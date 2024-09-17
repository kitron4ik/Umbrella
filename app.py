from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='./templates/static')
app.secret_key = 'your_secret_key'  # Необходимо для использования flash-сообщений

# Настройки для подключения к MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'nero'
app.config['MYSQL_PASSWORD'] = '1212'
app.config['MYSQL_DB'] = 'umbrella'

# Инициализация MySQL
mysql = MySQL(app)

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM reg WHERE email = %s AND password = %s", (email, password))
    user = cur.fetchone()
    cur.close()

    if user:
        # Логика для перенаправления в зависимости от роли
        role = user[6]  # Индекс может изменяться в зависимости от структуры таблицы
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
        flash('Пользователь с таким email уже зарегистрирован.')
        cur.close()
        return redirect(url_for('main'))
    cur.execute("""
        INSERT INTO reg (name, email, building_code, role_code, role, password) 
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

@app.route('/doctor')
def doctor_page():
    return render_template("doctor.html")

if __name__ == "__main__":
    app.run(debug=True)
