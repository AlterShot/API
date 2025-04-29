# Импортируем библиотеку
import pytest


# Создаем первый метод
@pytest.mark.run(order=6)
def test_sender(initial_step, module_scope) -> None:
    sender = initial_step[0]
    print(f"первое письмо отправил {sender}")

# Создаем второй метод
@pytest.mark.run(order=5)
def test_receiver(initial_step, module_scope) -> None:
    receiver = initial_step[1]
    print(f"первое письмо получил {receiver}")

# Создаем третий метод
@pytest.mark.run(order=1)
def test_sender_1(initial_step, module_scope) -> None:
    sender = initial_step[0]
    print(f"второе письмо отправил {sender}")

# Создаем четвертый метод
@pytest.mark.run(order=3)
def test_receiver_1(initial_step, module_scope) -> None:
    receiver = initial_step[1]
    print(f"второе письмо получил {receiver}")

# Создаем пятый метод
@pytest.mark.run(order=2)
def test_sender_2(initial_step, module_scope) -> None:
    sender = initial_step[0]
    print(f"третье письмо отправил {sender}")

# Создаем шестой метод
@pytest.mark.run(order=4)
def test_receiver_2(initial_step, module_scope) -> None:
    receiver = initial_step[1]
    print(f"третье письмо получил {receiver}")