# Импортируем библиотеку
import pytest

# Создаем фикстуру с переменными
@pytest.fixture
def initial_step() -> tuple[str, str]:
    print("Вход в систему выполнен")
    sender = "example_sender@test.ru"
    receiver = "example_receiver@test.ru"
    return sender, receiver

# Создаем первый метод с фикстурой
def test_sender(initial_step) -> None:
    sender, _ = initial_step
    print(f"Письмо отправил {sender}")

# Создаем второй метод с фикстурой
def test_receiver(initial_step) -> None:
    _, receiver = initial_step
    print(f"Письмо получил {receiver}")

