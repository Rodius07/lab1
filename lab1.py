#Вариант 5

# константы
Yellow = '\033[43m'
Red = '\033[41m'
Green = '\033[42m'
Black = '\033[47m'
Reset = '\033[0m'

# 1. Флаг Литвы
print('Флаг Литвы:')
for color in [Yellow,Green,Red]:
    for row in range(4): print(f'{color}{' '*50}')
print(f'{Reset}{'-'*100}')

# 2. узор "e"
print('узор е:')
p1, fill,p2 = 0,2,5
for row in range(3):
    print(f'{Reset}{' '*p1}{Black}{' '*fill}{Reset}{' '*p2}{Black}{' '*fill}')
    p1+=1
    p2-=2
print(f'{Reset}{' '*4}{Black}{' '*1}')
print(f'{Reset}{' '*4}{Black}{' '*1}')

print(f'{Reset}{'-'*100}')

# y = |x| - первая четверть
print('y = |x| - 1 четверть')
for x in range (9,0,-1):
    y = abs(x)
    print(f'{Reset}|{' '*(y-1)}{Black}{' '}')
print(f'|{Black}{''}{Reset}{'-'*15}')

print(f'{Reset}{'-'*100}')
# диаграмма

a = [abs(float(i.strip())) for i in open('sequence.txt')]
sum1 = sum(a[::2])
sum2 = sum(a) - sum1

p1 = sum1/125
p2 = sum2/125

def draw_vertical_chart(p1, p2):
    value1, value2 = p1, p2
    total = value1 + value2
    
    max_height = 18
    
    height1 = int((value1 / total) * max_height)
    height2 = int((value2 / total) * max_height)
    
    print("\033[2J\033[H", end="")
    print("\033[?25l", end="")
    
    print("\033[1;15H\033[36m\033[1mВЕРТИКАЛЬНАЯ ДИАГРАММА\033[0m")
    
    base_row = 18
    
    #Первый столбец (зеленый)
    for i in range(height1):
        row = base_row - i
        print(f"\033[{row};10H{Green}  {Reset}", end="")
    
    #Второй столбец (красный)
    for i in range(height2):
        row = base_row - i
        print(f"\033[{row};15H{Red}  {Reset}", end="")
    
    #Ось Y с метками
    for i in range(0, max_height + 1, 3):
        row = base_row - i
        percent = (i / max_height) * 100
        print(f"\033[{row};5H{percent:3.0f}%─", end="")
    
    print("\033[22;1H\033[?25h")  

draw_vertical_chart(p1,p2)