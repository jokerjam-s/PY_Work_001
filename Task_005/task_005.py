# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21 
#

from cmath import sqrt
import os

# получить число с консоли
#   message - сообщение для пользователя
#
def get_int(message: str) -> int:
    return int(input(message))

# расчет расстояния между точками на декартовой системе координат
#   ax - коорд х точки A
#   ay - коорд y точки A
#   bx - коорд х точки B
#   by - коорд y точки B
#
def calc_line(ax: int, ay: int, bx: int, by: int) -> float:
    return sqrt((ax - bx)**2 + (ay - by)**2)


## MAIM ##
os.system('cls')
aX = get_int('Координата X точки A: ')
aY = get_int('Координата Y точки A: ')
bX = get_int('Координата X точки B: ')
bY = get_int('Координата Y точки B: ')

# line = calc_line(aX, aY, bX, bY)

print(f'расстояние между точками {calc_line(aX, aY, bX, bY):.3f}')