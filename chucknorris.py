# Импортируем библиотеку
import requests

# Создаем переменную и выводим на печать url
url = "https://api.chucknorris.io/jokes/random"
print(url)

# Отправляем запрос на шутку и выводим
joke = requests.get(url)
joke_itself = joke.json()
print(joke_itself)

# Выводим на печать статус-код и проверяем его
print("status code: " + str(joke.status_code))
assert joke.status_code == 200, "status code wrong"
print("status code correct")

