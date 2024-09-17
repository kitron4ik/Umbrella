from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='./templates/static')

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
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        building_code = request.form['buildingCode']
        role_code = request.form['roleCode']
        role = request.form['role']
        password = request.form['password']

        # МайЭСКЮЭЛЬ
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO reg (name, email, building_code, role_code, role, password) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, email, building_code, role_code, role, password))
        
        mysql.connection.commit()
        cur.close()

        # Роли
        if role == "Доктор":
            return redirect(url_for('doctor_page'))
        elif role == "Пациент":
            return redirect(url_for('patient_page'))
        else:
            return redirect(url_for('main'))

# Страница пациента
@app.route('/patient')
def patient_page():
    return render_template("patient.html")

# Страница доктора
@app.route('/doctor')
def doctor_page():
    return render_template("doctor.html")

if __name__ == "__main__":
    app.run(debug=True)
