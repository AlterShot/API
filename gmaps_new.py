# Импортируем библиотеку
import requests


# Создаем общий класс
class MapsPostNGet():
    # Создаем переменные класса
    base_url = 'https://rahulshettyacademy.com'
    key = '?key=qaclick123'
    post_path = '/maps/api/place/add/json'
    get_path = '/maps/api/place/get/json'
    put_path = '/maps/api/place/update/json'
    new_address = '11, Broomside, TR'
    place_id = None

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

    # Создаем метод для POST
    def post(self) -> None:
        # Собираем url и печатаем его
        post_url = self.base_url + self.post_path + self.key
        print(f"POST url: {post_url}")

        # Делаем запрос POST
        post_process = requests.post(post_url, json=self.location_description)
        post_process_json = post_process.json()
        print(post_process_json)

        # Выводим и проверяем статус-код метода
        print(f"POST status code: {post_process.status_code}")
        assert post_process.status_code == 200, "wrong POST status code"
        print("POST status code correct")

        # Проверяем, получили ли place_id и выводим его
        self.place_id = post_process_json.get('place_id')
        assert self.place_id is not None, "place_id not received from POST"
        print(self.place_id)

    # Создаем метод для PUT
    def put(self) -> None:
        # Собираем url и печатаем его
        put_url = self.base_url + self.put_path + self.key
        print(f"PUT url: {put_url}")

        # Добавляем переменную с данными для обновления
        new_location_description = {
            "place_id": self.place_id,
            "address": self.new_address,
            "key": "qaclick123"
        }

        # Делаем запрос PUT
        put_process = requests.put(put_url, json=new_location_description)
        put_process_json = put_process.json()
        print(put_process_json)

        # Проверяем и печатаем статус-код запроса
        print(f"PUT status code: {put_process.status_code}")
        assert put_process.status_code == 200, "wrong PUT status code"
        print("PUT status code correct")

        # Проверяем сообщение, выводимое при запросе
        msg = put_process_json.get('msg')
        assert msg == "Address successfully updated", f"Expected message 'Address successfully updated', but got {msg}"
        print(f"Message correct")

    # Создаем метод для чтения и метода GET
    def get(self) -> None:
        # Собираем url и печатаем его
        get_url = self.base_url + self.get_path + self.key + "&place_id=" + f"{self.place_id}"
        print(f"GET url: {get_url}")

        # Делаем запрос GET
        get_process = requests.get(get_url)
        get_process_json = get_process.json()
        print(get_process_json)

        # Проверяем и печатаем статус-код запроса
        print(f"GET status code: {get_process.status_code}")
        assert get_process.status_code == 200, "wrong GET status code"
        print("GET status code correct")

        # Проверяем корректность обновления данных и печатаем новый адрес
        final_address = get_process_json.get('address')
        assert final_address == self.new_address, f"should've been {self.new_address}, got {final_address}"
        print(f"new address: {final_address}, success")


# Создаем экземпляр класса и вызываем методы
print("test start")
start = MapsPostNGet()
start.post()
start.put()
start.get()
print("test finished")
