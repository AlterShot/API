# Импортируем библиотеку
import requests


# Создаем класс
class ChuckNorrisJoke():
    url = "https://api.chucknorris.io"

    # Создаем метод
    def specific_joke(self):
        # Создаем переменные с категорией и url, печатаем общий url
        joke_category = "travel"
        type_path = f"/jokes/random?category={joke_category}"
        joke_path = self.url + type_path
        print(joke_path)

        # Обращаемся к API и выводим данные
        joke_show = requests.get(joke_path)
        joke_show_result = joke_show.json()
        print(joke_show_result)

        # Проверяем статус-код ответа
        print(f"status code: {joke_show.status_code}")
        assert joke_show.status_code == 200, "status code wrong"
        print("status code correct")

        # Проверяем корректность категории
        check_joke_category = joke_show_result.get('categories')
        assert joke_category in check_joke_category, "category wrong"
        print("category correct")

        # Печатаем только саму шутку
        joke_only = joke_show_result.get('value')
        print(joke_only)

        # Проверяем наличие слова в шутке
        name = "Chuck"
        if name in joke_only:
            print("joke correct")
        else:
            print("joke wrong")


# Создаем экземпляр класса и вызываем метод
norris_joke = ChuckNorrisJoke()
norris_joke.specific_joke()