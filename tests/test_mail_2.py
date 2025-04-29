# Создаем первый метод с фикстурой по модулю
def test_sender(initial_step, module_scope) -> None:
    sender, _ = initial_step
    print(f"Письмо отправил {sender}")

# Создаем второй метод с фикстурой по модулю
def test_receiver(initial_step, module_scope) -> None:
    _, receiver = initial_step
    print(f"Письмо получил {receiver}")

