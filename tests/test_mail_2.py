# Импортируем библиотеку
import pytest

# Создаем фикстуру с переменными
@pytest.fixture
def initial_step():
    print("Вход в систему выполнен")
    sender = "example_sender@test.ru"
    receiver = "example_receiver@test.ru"

    # Вводим команду yield для возвращения значений
    yield sender, receiver

    # Создаем принт, который будет выполняться после методов
    print("Выход из системы выполнен")

# Создаем первый метод с фикстурой
def test_sender(initial_step) -> None:
    sender, _ = initial_step
    print(f"Письмо отправил {sender}")

# Создаем второй метод с фикстурой
def test_receiver(initial_step) -> None:
    _, receiver = initial_step
    print(f"Письмо получил {receiver}")

