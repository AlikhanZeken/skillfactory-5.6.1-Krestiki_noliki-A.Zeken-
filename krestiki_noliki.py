def hello(): print("ИГРА КРЕСТИКИ-НОЛИКИ")
hello()
field = [[" "] * 3 for i in range(3)]
def game():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  ............... ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  ............... ")
    print()
game()
def number():
    while True:
        cords = input(" Ваш ход: ").split()
        if len(cords) != 2:
            print(" ВВОДИТЬ ТОЛЬКО ДВА ЧИСЛА ")
            continue
        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" ВВОДИТЬ ТОЛЬКО ЧИСЛА! ")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" ВВОДИТЬ ТОЛЬКО (0 1 2)!!! ")
            continue
        if field[x][y] != " ":
            print(" ЗАНЯТО! ")
            continue
        return x, y
number()
def win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("ПОЗДРАВЛЯЮ, ВЫЙГРАЛ КРЕСТИК!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("ПОЗДРАВЛЯЮ, ВЫЙГРАЛ НОЛИК!!!")
            return True
    return False

field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    game()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")
    x, y = number()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if win():
        break
    if count == 9:
        print(" Победила дружба ^_^")
        break
