# Импортируем библиотеку
import pytest

# Не используем созданную фикстуру
@pytest.fixture
def initial_step():
    print("Вход в систему выполнен")
    yield
    print("Выход из системы выполнен")

# Создаем первый метод с переменной без фикстуры
def test_sender() -> None:
    sender = "example_sender@test.ru"
    print(f"Письмо отправил {sender}")

# Создаем второй метод с переменной без фикстуры
def test_receiver() -> None:
    receiver = "example_receiver@test.ru"
    print(f"Письмо получил {receiver}")