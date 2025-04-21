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
        print(category_url)

        # Собираем все категории и выводим их
        category_list = requests.get(category_url).json()
        print(f"all categories: {category_list}")

        # Проходимся по списку полученных категорий
        for category in category_list:

            # Подставляем значения в url для запроса get
            many_jokes_path = f"/jokes/random?category={category}"
            many_jokes_url = self.url + many_jokes_path

            # Печатаем полученные url
            print(many_jokes_url)

            # Выводим на печать то, что получилось
            show_jokes = requests.get(many_jokes_url)
            result = show_jokes.json()
            print(result)

            # Проверяем статус-код для каждой шутки
            print(f"status code: {show_jokes.status_code}")
            assert show_jokes.status_code == 200, "status code wrong"
            print("status code correct")

            # Выводим каждую шутку отдельно
            joke_only = result.get("value")
            print(joke_only)


# Создаем экземпляр класса и вызываем метод
norris_joke = ChuckNorrisJoke()
norris_joke.specific_joke()