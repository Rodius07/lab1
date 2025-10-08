# Вариант 5

# Константы
ESC = '\033['
YELLOW = '\033[43m'
RED = '\033[41m'
GREEN = '\033[42m'
BLACK = '\033[47m'
RESET = '\033[0m'


# 1. Флаг Литвы
print('Флаг Литвы:')

height = 4
width = 50

for color in [YELLOW, GREEN, RED]:
    for _ in range(height):
        print(f"{color}{' ' * width}")

print(f"{RESET}{'-' * 100}")


# 2. Узор "e"
print('Узор e:')

count = 10
p1 = 0
fill = 2
p2 = 5
p4 = 3
g = 3

for d in range(g):
    print(
        f"{RESET}{' ' * p1}{BLACK}{' ' * fill}"
        f"{RESET}{' ' * p2}{BLACK}{' ' * fill}"
        f"{RESET}{' ' * (p4 + d)}" * count
    )
    p1 += 1
    p2 -= 2

print(f"{RESET}{' ' * 4}{BLACK}{' ' * 1}{RESET}{' '*(p4+g+1)}"*count) 
print(f"{RESET}{' ' * 4}{BLACK}{' ' * 1}{RESET}{' '*(p4+g+1)}"*count)
print(f"{RESET}{'-' * 100}")


# 3. y = |x| — первая четверть
print('y = |x| — 1 четверть')

for x in range(9, 0, -1):
    y = abs(x)
    print(f"{RESET}|{' ' * (y - 1)}{BLACK} ")

print(f"|{BLACK} {RESET}{'-' * 15}")
print(f"{RESET}{'-' * 100}")


# 4. Диаграмма
with open('sequence.txt') as file:
    values = [abs(float(line.strip())) for line in file]

sum1 = sum(values[::2])
sum2 = sum(values) - sum1

part1 = sum1 / 125
part2 = sum2 / 125


def draw_vertical_chart(value1, value2):
    total = value1 + value2
    max_height = 18

    height1 = int((value1 / total) * max_height)
    height2 = int((value2 / total) * max_height)

    # Очистка экрана и скрытие курсора
    print(f"{ESC}2J{ESC}H", end="")
    print(f"{ESC}?25l", end="")

    print(f"{ESC}1;15H\033[36m\033[1mВЕРТИКАЛЬНАЯ ДИАГРАММА{RESET}")

    base_row = 18

    # Первый столбец (зелёный)
    for i in range(height1):
        row = base_row - i
        print(f"{ESC}{row};10H{GREEN}  {RESET}", end="")

    # Второй столбец (красный)
    for i in range(height2):
        row = base_row - i
        print(f"{ESC}{row};15H{RED}  {RESET}", end="")

    # Ось Y с метками
    for i in range(0, max_height + 1, 3):
        row = base_row - i
        percent = (i / max_height) * 100
        print(f"{ESC}{row};5H{percent:3.0f}%─", end="")

    # Возврат курсора
    print(f"{ESC}22;1H{ESC}?25h", end="")


draw_vertical_chart(part1, part2)
