# Проект FitLife - MVP версия 1.0
import sys

# Гарантируем UTF-8 для стандартных потоков, чтобы вывод
# корректно читался тестами и не падал с UnicodeDecodeError.
# Получил при помощи ИИ так как не смог сам разобраться
# в чем была ошибка в 6 тесте.
for _stream in (sys.stdin, sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        try:
            _stream.reconfigure(encoding="utf-8", errors="replace")
        except (ValueError, OSError):
            pass


# Константы программы
WATER_PER_KG = 30          # мл воды на 1 кг веса
MIN_AGE = 1
MAX_AGE = 99
MIN_WEIGHT = 20
MAX_WEIGHT = 300
MIN_HEIGHT = 1.0
MAX_HEIGHT = 3.0
LITER = 1000


def input_name():
    """Запрашивает имя пользователя и проверяет, что оно не пустое."""
    while True:
        name = input(
            "Здравствуйте, пожалуйста, введите ваше имя: "
        ).strip()
        if name:
            return name
        print("Ошибка. Имя не может быть пустым.")


def input_age():
    """Запрашивает возраст (целое число) в допустимом диапазоне."""
    while True:
        try:
            value = int(input("Введите ваш возраст: "))
        except ValueError:
            print("Ошибка. Пожалуйста, введите целое число.")
            continue
        if MIN_AGE <= value <= MAX_AGE:
            return value
        print(
            f"Ошибка. Возраст должен быть от {MIN_AGE}",
            f"до {MAX_AGE}.",
        )


def input_weight():
    """Запрашивает вес в кг (число с плавающей точкой)."""
    while True:
        raw = input("Введите ваш вес (кг): ").replace(",", ".")
        try:
            value = float(raw)
        except ValueError:
            print("Ошибка. Пожалуйста, введите число.")
            continue
        if MIN_WEIGHT <= value <= MAX_WEIGHT:
            return round(value, 2)
        print(
            f"Ошибка. Вес должен быть от {MIN_WEIGHT}",
            f"до {MAX_WEIGHT}.",
        )


def input_height():
    """Запрашивает рост в метрах (число с плавающей точкой)."""
    while True:
        raw = input("Введите ваш рост (м): ").replace(",", ".")
        try:
            value = float(raw)
        except ValueError:
            print("Ошибка. Пожалуйста, введите число.")
            continue
        if MIN_HEIGHT <= value <= MAX_HEIGHT:
            return round(value, 2)
        print(
            f"Ошибка. Рост должен быть от {MIN_HEIGHT}",
            f"до {MAX_HEIGHT}.",
        )


def calculate_bmi(weight, height):
    """Возвращает индекс массы тела (ИМТ)."""
    return weight / (height ** 2)


def calculate_water(weight):
    """Возвращает рекомендуемую норму воды в мл."""
    return int(weight * WATER_PER_KG)


# 1. Знакомство
user_name = input_name()
user_age = input_age()

# 2. Сбор данных
user_weight = input_weight()
user_height = input_height()

# 3. Расчеты
user_bmi = round(calculate_bmi(user_weight, user_height), 1)
water_needed_ml = round(calculate_water(user_weight))
water_needed_l = water_needed_ml / LITER


# 4. Вывод результата
print(f"Привет, {user_name}!")
print(f"Ваш возраст: {user_age}")
print(f"Ваш ИМТ: {user_bmi}.")
print(f"Рекомендуемая норма воды: {water_needed_l} л.")
print("Расчет окончен. Будьте здоровы!")
