<?php
// Параметры подключения к базе данных
$servername = "localhost"; // Хост
$username = "vankul777g";                     // Имя пользователя
$password = "TOTnot0671M";          // Пароль
$database = "vankul777g";           // Имя базы данных

// Создаем соединение
$conn = new mysqli($servername, $username, $password, $database);

// Проверяем соединение
if ($conn->connect_error) {
    die("Ошибка подключения: " . $conn->connect_error);
}

// Получаем данные из POST-запроса
$name = isset($_POST['Имя']) ? $_POST['Имя'] : 'Не указано';
$email = isset($_POST['Email']) ? $_POST['Email'] : 'Не указано';
$phone = isset($_POST['Телефон']) ? $_POST['Телефон'] : 'Не указано';

// Вставляем данные в таблицу
$stmt = $conn->prepare("INSERT INTO contact (name, email, phone) VALUES (?, ?, ?)");
$stmt->bind_param("sss", $name, $email, $phone);

if ($stmt->execute()) {
    echo json_encode(["message" => "Данные успешно записаны!"]);
} else {
    echo json_encode(["error" => "Ошибка при добавлении данных: " . $stmt->error]);
}

// Закрываем соединение
$stmt->close();
$conn->close();
?>
