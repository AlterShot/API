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

# Создаем фикстуру с методом по модулю
@pytest.fixture(scope='module')
def module_scope():
    print('Начало всех тестов')
    yield
    print('Конец всех тестов')

# Создаем фикстуру с методом по функции
@pytest.fixture(scope='function')
def function_scope_1():
    print('Первый тест начат')
    yield
    print('Первый тест закончен')

# Создаем фикстуру с методом по функции
@pytest.fixture(scope='function')
def function_scope_2():
    print('Второй тест начат')
    yield
    print('Второй тест закончен')