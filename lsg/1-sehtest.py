'''
Probe EF 2022
Programm 1-SEHTEST.PY
'''

def full_line(size):
    sz = size + 4
    print('* ' * sz)
    print('* ' * sz)

def boardered_right(size):
    for i in range(size):
        print('    ' + '  ' * size + '* * ')

def boardered_left(size):
    for i in range(size):
        print('* * ' + '  ' * size + '    ')

def boardered_line(size):
    for i in range(size + 2):
        print('* * ' + '  ' * size + '* * ')

def c(size, side):
    if side == 'R':
        full_line(size)
        boardered_left(size)
        full_line(size)
    elif side == 'L':
        full_line(size)
        boardered_right(size)
        full_line(size)
    elif side == 'D':
        full_line(size)
        boardered_line(size)
    elif side == 'U':
        boardered_line(size)
        full_line(size)

def question():
    size = input('Welches C? (Format: [Grösse][Richtung], bspw. 2r) ')
    if len(size) < 2:
        return [-1, '']
    side = size[-1].upper()
    grösse = size[:-1]
    try:
        grösse = int(grösse)
    except:
        grösse = -1
    return [grösse, side]

def user_input():
    [size, side] = question()
    while size < 0 or side not in ['R', 'L', 'U', 'D']:
        [size, side] = question()
    return [size, side]


[size, side] = user_input()

c(size, side)