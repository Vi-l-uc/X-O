# Классическая игра в крестики-нолики на игровом поле 3х3

print("Игра в крестики - нолики. \n"
      "Первым ходят крестики. \n")


def chis(p):
    X = [i for i in range(1, 10)]
    if p.isdigit():
        if int(p) in X:
            return int(p)
        else:
            print('Введите число от 1 до 9')
            return pole()
    else:
        print('Введите число от 1 до 9')
        return pole()


def hod(x):
    global P
    if P[x] == ' ':
        return x
    else:
        print("Ячейка занята, попробуйте снова!")
        return pole()


def pole():
    p = input('Введите номер ячейки: ')
    return hod(chis(p))


def game(pol_gam):
    global P
    print(pol_gam)
    P[pole()] = "X"
    print(pol_gam)
    for i in range(4):
        P[pole()] = "0"
        print(pol_gam)
        print(P)
        P[pole()] = "X"
        print(pol_gam)


P = {i: ' ' for i in range(1, 10)}
pole_game = (f'   +---+---+---+\n'
             f'   | {P[1]}¹| {P[2]}²| {P[3]}³|\n'
             f'   +---+---+---+\n'
             f'   | {P[4]}⁴| {P[5]}⁵| {P[6]}⁶|\n'
             f'   +---+---+---+\n'
             f'   | {P[7]}⁷| {P[8]}⁸| {P[9]}⁹|\n'
             f'   +---+---+---+\n'
             f' ')

game(pole_game)
print(P)
print(pole_game)