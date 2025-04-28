import pytest


@pytest.fixture
def initial_step():
    print("Вход в систему выполнен")
    sender = "example1@test.ru"
    receiver = "example2@test.ru"
    return sender, receiver

def test_sender(initial_step):
    sender, _ = initial_step
    print(f"Письмо отправил {sender}")

def test_receiver(initial_step):
    _, receiver = initial_step
    print(f"Письмо получил {receiver}")

