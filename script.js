const hamburger = document.getElementById('hamburger');
const menu = document.querySelector('.menu');

hamburger.addEventListener('click', function () {
    const hamIcon = this.querySelector('.hamburger-icon');
    const crossIcon = this.querySelector('.cross-icon');
    if (hamIcon.style.display === "none") {
        hamIcon.style.display = "inline-block"
        menu.style.display = "none"
        crossIcon.style.display = "none"
    }
    else {
        crossIcon.style.display = "inline-block"
        hamIcon.style.display = "none"
        menu.style.display = "block"
    }
});



document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".contact-form");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Предотвращаем стандартное действие формы

        const formData = new FormData(form); // Получаем данные формы

        const xhr = new XMLHttpRequest();
        xhr.open("POST", "submit.php", true); // Указываем адрес сервера PHP

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                // Обработка ответа сервера
                if (xhr.status === 200) {
                    alert("Данные успешно отправлены: " + xhr.responseText); // Сообщение об успешной отправке
                    form.reset(); // Очищаем поля формы
                } else {
                    alert("Ошибка: " + xhr.statusText); // Сообщение об ошибке
                }
            }
        };

        xhr.send(formData); // Отправляем данные формы
    });
});

