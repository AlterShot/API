# Импортируем библиотеку
import pytest

# Не используем созданную фикстуру
@pytest.fixture
def initial_step() -> tuple[str, str]:
    print("Вход в систему выполнен")
    sender = "example_sender@test.ru"
    receiver = "example_receiver@test.ru"
    return sender, receiver

# Создаем первый метод с переменной без фикстуры
def test_sender() -> None:
    sender = "example_sender@test.ru"
    print(f"Письмо отправил {sender}")

# Создаем второй метод с переменной без фикстуры
def test_receiver() -> None:
    receiver = "example_receiver@test.ru"
    print(f"Письмо получил {receiver}")