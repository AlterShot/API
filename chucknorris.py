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
        print("\n----")
        print(f"\U0001F517path to categories: {category_url}")

        # Собираем все категории и выводим их
        category_list = requests.get(category_url).json()
        print("\n----")
        print(f"\U0001F4DAall categories: ")
        for category in category_list:
            print(f" - {category}")

        # Просим пользователя ввести категорию
        user_category = input("enter a category for a joke from a list above: ").strip().lower()

        # Проверяем наличие категории
        if user_category not in category_list:
            print(f"\u274C\'{user_category}\' was not found. Try again.")
            return

        # Если категория есть, печатаем, что выбор успешен
        print(f"\n\u2705\"{user_category}\" category is in a list")

        # Создаем запрос и печатаем полученный адрес
        user_path = self.url + f"/jokes/random?category={user_category}"
        print(f"\n\U0001F50Dyour url: {user_path}")

        # Делаем запрос на шутку и проверяем, нет ли проблем с API
        user_joke = requests.get(user_path)
        if user_joke.status_code != 200:
            print("some error during download")

        # Выводим шутку по запросу пользователя
        user_joke_text = user_joke.json()
        just_joke = user_joke_text.get('value')
        print(f"\n\U0001F602here is your joke: {just_joke}")


# Создаем экземпляр класса и вызываем метод
norris_joke = ChuckNorrisJoke()
norris_joke.specific_joke()
