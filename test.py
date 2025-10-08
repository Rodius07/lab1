import os
import time

ESC = '\033['
YELLOW = f'{ESC}43m'
RED = f'{ESC}41m'
GREEN = f'{ESC}42m'
BLACK = f'{ESC}47m'
RESET = f'{ESC}0m'

print(f"{ESC}?25l", end="")  # Скрыть курсор

while True:
    for color in [RED, GREEN, YELLOW]:
        for _ in range(8):
            print(f"{color}{' ' * 8}{RESET}")
        time.sleep(0.1)
        os.system("clear")
