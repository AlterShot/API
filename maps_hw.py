# Импортируем библиотеку
import requests


# Создаем общий класс
class MapsPostNGet():
    # Создаем переменные класса
    base_url = 'https://rahulshettyacademy.com'
    key = '?key=qaclick123'
    post_path = '/maps/api/place/add/json'
    get_path = '/maps/api/place/get/json'

    location_description = {"location": {
        "latitude": "-38.383494",
        "longitude": "33.427362"},
        "accuracy": "50",
        "name": "Frontline house",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": "shoe park,shop",
        "website": "http://google.com",
        "language": "French-IN"}

    # Создаем метод для POST и записи
    def post_and_write(self) -> None:
        # Собираем url и печатаем его
        post_url = self.base_url + self.post_path + self.key
        print(post_url)

        # Переменная, где будут храниться place_id
        place_ids = []

        # Проходим 5 раз метод POST
        for i in range(5):
            post_result = requests.post(post_url, json=self.location_description)
            post_result_json = post_result.json()
            print(post_result_json)

            # Проверяем статус-код запросов
            status_code = post_result.status_code
            print(status_code)
            assert status_code == 200, "wrong POST status code"
            print("status code POST correct")

            # Добавляем id в ранее созданный список
            place_ids.append(post_result_json.get('place_id'))

        # Создаем файл и записывает туда значения из списка
        with open('places.txt', 'w') as places_to_write:
            for place_id in place_ids:
                places_to_write.write(place_id + "\n")

        # Печатаем, что файлы сохранены
        print("ids are saved")

    # Создаем метод для чтения и метода GET
    def get_and_read(self) -> None:
        get_url = self.base_url + self.get_path + self.key + "&place_id="

        # Достаем id из файла
        with open('places.txt', 'r') as places_to_read:
            place_id = [line.strip() for line in places_to_read]

        # Подставляем id из файла в GET запрос
        for places in place_id:
            full_get_url = get_url + f"{places}"
            process_of_get = requests.get(full_get_url)

            # Проверяем, не пустой ли id
            names = process_of_get.json()
            check_name = names.get('name')
            assert check_name is not None, "no data found in this place_id"
            print("data exists")

            # Проверяем и печатаем статус-код
            print(process_of_get.status_code)
            assert process_of_get.status_code == 200, "status code in GET is wrong"
            print("status code GET correct")


# Создаем экземпляр класса и вызывает методы
start = MapsPostNGet()
start.post_and_write()
start.get_and_read()
