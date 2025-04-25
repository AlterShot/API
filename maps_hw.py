# Импортируем библиотеку
import requests


# Создаем общий класс
class MapsPostNGet():
    # Создаем переменные класса
    base_url = 'https://rahulshettyacademy.com'
    key = '?key=qaclick123'
    post_path = '/maps/api/place/add/json'
    get_path = '/maps/api/place/get/json'
    delete_path = '/maps/api/place/delete/json'

    location_description = {"location": {
        "lat": "-38.383494",
        "lng": "33.427362"},
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
            place_ids = [line.strip() for line in places_to_read]

        # Подставляем id из файла в GET запрос
        for place_id in place_ids:
            full_get_url = get_url + f"{place_id}"
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

    # Создаем метод для удаления
    def delete_stuff(self) -> None:
        # Перебираем id
        with open('places.txt', 'r') as places_to_delete:
            place_ids = [line.strip() for line in places_to_delete.readlines()]

        # Создаем переменную для удаления
        delete_ids = [place_ids[1], place_ids[3]]

        # Удаляем 2 и 4 id из списка
        for place_id in delete_ids:
            delete_url = self.base_url + self.delete_path + self.key
            deletion = {"place_id": place_id}
            delete_process = requests.delete(delete_url, json=deletion)

            # Проверяем статус-код запроса и печатаем его
            print(f"DELETE status code: {delete_process.status_code}")
            assert delete_process.status_code == 200, f"DELETE status code {place_id} is wrong"
            print(f"DELETE status code {place_id} correct")

    # Создаем метод для получения нового списка
    def get_new(self) -> None:
        # Собираем url
        get_url = self.base_url + self.get_path + self.key + "&place_id="

        # Перебираем список id
        with open('places.txt', 'r') as places_to_read:
            place_ids = [line.strip() for line in places_to_read.readlines()]

        # Создаем переменную для хранения существующих id
        places_exist = []

        # Перебираем id и делаем запросы
        for place_id in place_ids:
            getting_ids = requests.get(get_url + place_id)

            # Проверяем статус-коды запросов
            if getting_ids.status_code == 200 and getting_ids.json().get('name'):
                places_exist.append(place_id)
                print(f"{place_id} correct")
            else:
                print(f"{place_id} wrong")

        # Записываем id в новый файл
        with open('existing_places.txt', 'w') as file:
            for place_id in places_exist:
                file.write(place_id + "\n")
        print("IDs added")


# Создаем экземпляр класса и вызывает методы
start = MapsPostNGet()
print("test start")
start.post_and_write()
start.get_and_read()
start.delete_stuff()
start.get_new()
print("test finish")
