import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('database.sqlite')
c = conn.cursor()

# Создание таблицы
c.execute("CREATE TABLE IF NOT EXISTS questions (request TEXT, answer TEXT)")

# Вставка данных в таблицу
questions = []
for _ in range(548):
    questions.append((None, None))
c.executemany("INSERT INTO questions (request, answer) VALUES (?, ?)", questions)

# Запрос к таблице
question = input("Введите вопрос: ")
c.execute("SELECT answer FROM questions WHERE request = ?", (question,))
result = c.fetchone()

# Возвращение ответа
if result is not None:
    print("Ответ:", result[0])
else:
    print("Вопрос не найден.")

# Закрытие соединения с базой данных
conn.close()
