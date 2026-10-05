import time
import os

GREEN  = '\u001b[42m'
YELLOW = '\u001b[43m'
RED    = '\u001b[41m'
BLUE = '\u001b[44m'
RESET  = '\u001b[0m'
ERASE = '\x1B[2K'
BEGIN = '\x1B[1G'


def flag():
    height = 20
    length = 30
    for i in range(height):
        if i<10:
            print(GREEN +'  ' * 10 + YELLOW +'  ' * 20 + RESET)
        else:
            print(GREEN + '  ' * 10 + RED +'  ' * 20 + RESET)
flag()
print('')
def sequence():
    file = open('sequence.txt', 'r')
    less_zero = []
    more_zero = []
    for line in file:
        if 0 <= int(float(line)) <= 5:
            more_zero.append(float(line))
        elif -5 <= int(float(line)) <= 0:
            less_zero.append(float(line))
    print(f'{BLUE}{' ' * int(len(more_zero) / 5)}{RESET} {round(len(more_zero)/(len(more_zero) + len(less_zero)) * 100, 1)}%')
    print(f'{RED}{' ' * int(len(less_zero) / 5)}{RESET} {round(len(less_zero)/(len(less_zero) + len(more_zero)) * 100, 1)}%')
sequence()
print()

def double_sqr(n,k):
    print('')
    BASE_HEIGHT = 15
    HEIGHT = BASE_HEIGHT * k
    BASE_WIDTH = 40
    WIDTH = BASE_WIDTH * n
    R = 4
    cy1, cx1 = BASE_HEIGHT // 2, 12
    cy2, cx2 = BASE_HEIGHT // 2, 26
    for y in range(HEIGHT):
        for x in range(WIDTH):
            x_local = x % BASE_WIDTH
            y_local = y % BASE_HEIGHT
            dx1 = abs((x_local - cx1) // 2)
            dy1 = abs(y_local - cy1)
            dx2 = abs((x_local - cx2) // 2)
            dy2 = abs(y_local - cy2)
            if (dx1 + dy1 <= R) or (dx2 + dy2 <= R):
                print(BLUE + ' ' + RESET, end='')
            else:
                print(YELLOW + ' ' + RESET, end='')
        print('')
double_sqr(3,3)

def running():
    for i in range(0,101,20):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Running... Stamina:{100-i}%', end=' ', flush=True)
        time.sleep(1)
    print(" TIRED! Need to rest.")
running()

