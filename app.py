from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Параметры подключения к базе данных
db_config = {
    'host': 'bedrocks.tplinkdns.com',
    'database': 'ivan_portfolio',
    'user': 'ivan',
    'password': 'ivankulikov2005'
}

def create_table():
    connection = None  # Инициализация переменной
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS contact (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    email VARCHAR(100),
                    phone VARCHAR(15)
                )
            ''')
            print("Таблица 'contact' успешно создана или уже существует.")
    except Error as e:
        print(f"Ошибка соединения: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('Имя', 'Не указано')
    email = request.form.get('Email', 'Не указано')
    phone = request.form.get('Телефон', 'Не указано')

    print(f"Полученные данные: Имя={name}, Email={email}, Телефон={phone}")

    connection = None  # Инициализация переменной
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO contact (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
            connection.commit()
            print("Данные успешно записаны в таблицу.")
            return jsonify({"message": "Данные успешно записаны!"}), 200
        
    except Error as e:
        print(f"Ошибка: {e}")
        return jsonify({"error": str(e)}), 500
    
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == '__main__':
    create_table()  # Создаем таблицу при старте приложения
    app.run(host='0.0.0.0', port=5000)  # Обеспечиваем, что приложение доступно на всех интерфейсах
