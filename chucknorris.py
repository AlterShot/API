# Импортируем библиотеку
import requests


# Создаем класс
class ChuckNorrisJoke():
    url = "https://api.chucknorris.io"

    # Создаем метод
    def specific_joke(self) -> None:
        # Создаем переменную с путем для всех категорий
        category_list_path = "/jokes/categories"
        category_url = self.url + category_list_path

        # Печатаем путь
        print("\n----" * 2)
        print(f"\U0001F517path to categories: {category_url}")
        print("\n----" * 2)

        # Собираем все категории и выводим их
        category_list = requests.get(category_url).json()
        print("\n----" * 2)
        print(f"\U0001F4DAall categories: ")
        for category in category_list:
            print(f" - {category}")
        print("\n----" * 2)

        # Проходимся по списку полученных категорий
        for category in category_list:
            print("\n----" * 2)
            # Подставляем значения в url для запроса get
            many_jokes_path = f"/jokes/random?category={category}"
            many_jokes_url = self.url + many_jokes_path

            # Печатаем полученные url
            print(f"\n\U0001F50Dpath to current joke: {many_jokes_url}")

            # Выводим на печать то, что получилось
            show_jokes = requests.get(many_jokes_url)
            result = show_jokes.json()
            print(f"\n\U0001F4E6full json info: {result}")

            # Проверяем статус-код для каждой шутки
            print(f"\n\u26A0current path status code: {show_jokes.status_code}")
            assert show_jokes.status_code == 200, "\u274Cstatus code wrong"
            print("\n\u2705status code check correct")

            # Выводим каждую шутку отдельно
            joke_only = result.get("value")
            print(f"\n\U0001F602and the joke by itself is: {joke_only}")
            print("\n----" * 2)


# Создаем экземпляр класса и вызываем метод
norris_joke = ChuckNorrisJoke()
norris_joke.specific_joke()
