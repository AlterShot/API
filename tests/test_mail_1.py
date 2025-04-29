# Создаем первый метод с фикстурой по функции
def test_sender(initial_step, function_scope_1) -> None:
    sender = initial_step[0]
    print(f"Письмо отправил {sender}")

# Создаем второй метод с фикстурой по функции
def test_receiver(initial_step, function_scope_2) -> None:
    receiver = initial_step[1]
    print(f"Письмо получил {receiver}")