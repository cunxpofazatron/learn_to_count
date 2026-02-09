import random


LOW = 10
HIGH = 100

play_game = True
count = 0
right = 0
score = 0


def gen_add():
    x = random.randint(LOW, HIGH)
    y = random.randint(LOW, HIGH)
    return x, y, x + y


def gen_sub():
    x = random.randint(LOW, HIGH)
    y = random.randint(LOW, x)
    return x, y, x - y


def gen_mul():
    x = random.randint(2, 10)
    y = random.randint(2, 10)
    return x, y, x * y


def gen_div():
    y = random.randint(2, 10)
    z = random.randint(2, 10)
    x = y * z
    return x, y, z


print("""Компьютер составляет пример.
Введите ответ.
HELP — подсказка
STOP — выход
""")

print("*" * 40)


while play_game:

    print(f"\nОчки: {score} | Задач: {count} | Верных: {right}")
    print("-" * 30)

    sign = random.randint(0, 3)

    if sign == 0:
        x, y, z = gen_add()
        print(f"{x} + {y} = ?")

    elif sign == 1:
        x, y, z = gen_sub()
        print(f"{x} - {y} = ?")

    elif sign == 2:
        x, y, z = gen_mul()
        print(f"{x} * {y} = ?")

    else:
        x, y, z = gen_div()
        print(f"{x} / {y} = ?")

    while True:
        user = input("Ваш ответ: ").strip()

        if user.upper() in ("STOP", "S", "Ы", "ЫЕЩЗ"):
            play_game = False
            break

        if user.upper() in ("HELP", "?", ",", "РУДЗ"):
            print(f"Последняя цифра: {z % 10}")
            score -= 10
            continue

        if not user.isdigit():
            print("Введите число или команду")
            continue

        user = int(user)
        break

    if not play_game:
        break

    count += 1

    if user == z:
        print("Правильно!")
        right += 1
        score += 1
    else:
        print(f"Неправильно. Правильный ответ: {z}")
        score -= 20


print("\n" + "*" * 40)
print("Статистика:")

print(f"Всего задач: {count}")
print(f"Верных: {right}")

if count > 0:
    print(f"Процент: {int(right / count * 100)} %")
else:
    print("Процент: 0 %")

print("До встречи!")
