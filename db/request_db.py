import sqlite3





# Запрос к таблице
def request_database(user_request):
    
    # Подключение к базе данных
    conn = sqlite3.connect('database.sqlite')
    c = conn.cursor()
    
    try:
        
        #user_input = input("Введите вопрос: ")
        c.execute(f"SELECT answer FROM questions WHERE request = '{user_request.lower()}'", ())
        result = c.fetchone()

        # Возвращение ответа
        if result is not None:
            conn.close()
            return "Причина и решение проблемы(если оно есть):\n" + result[0].capitalize()

        else:
            conn.close()
            return("Переформулируйте проблемы, я не совсем понимаю вас")
    except:
            return("Переформулируйте проблемы, я не совсем понимаю вас")
    