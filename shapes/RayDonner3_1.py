def selection():
    print('----------------------')
    print('SELECT SHAPE')
    print('----------------------')
    print('1 - Circle')
    print('2 - Rectangle')
    print('3 - Square')
    print('4 - Triangle')
    shape = int(input('Shape number: '))
    while shape < 1 or shape > 4:
        shape = int(input('Shape number (1-4): '))
    return shape


def main():
    while True:
        shape = selection()

        choice = int(input('Computation (Area = 1 or Perimeter = 2) '))
        while choice != 1 and choice != 2:
            choice = int(input('Enter 1 or 2 '))

        if choice == 1:
            from area import calculate_area
            calculate_area(shape)
        elif choice == 2:
            from perimeter import calculate_perimeter
            calculate_perimeter(shape)

        choicecontinue = input('Continue (y/n): ').strip()
        while choicecontinue != 'y' and choicecontinue != 'n':
            choicecontinue = input('Enter y or n: ').strip()
        if choicecontinue == 'n':
            print('PROGRAM DONE')
            return False


if __name__ == '__main__':
    main()
