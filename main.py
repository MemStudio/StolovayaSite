
# Импортируем Flask
from flask import Flask

# Создаём экземпляр приложения Flask
app = Flask(__name__)

# Определяем маршрут для главной страницы
@app.route("/")
def home():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1> привет мир<h1>
</body>
</html>"""

# Запускаем сервер
if __name__ == "__main__":
    app.run(debug=True)  # debug=True включает автоматическую перезагрузку