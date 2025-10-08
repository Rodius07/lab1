import os
import time

Yellow = '\033[43m'
Red = '\033[41m'
Green = '\033[42m'
Black = '\033[47m'
Reset = '\033[0m'

print("\033[?25l", end="")

while True:
    for color in [Red,Green,Yellow]:
        for i in range(8): print(f'{color}{' '*8}{Reset}')
        time.sleep(0.1)
        os.system("clear")

    

