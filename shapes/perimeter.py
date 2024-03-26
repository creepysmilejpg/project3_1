def calculate_perimeter(shape):
    import math
    pi = math.pi
    perimeter = 0.00
    if shape == 1:
        radius = float(input('Circle radius: '))
        perimeter = (radius * pi) * 2
        print("Circle perimeter = {:0.2f}".format(perimeter))
    elif shape == 2:
        base = float(input('Rectangle side 1: '))
        height = float(input('Rectangle side 2: '))
        perimeter = (base * 2) + (height * 2)
        print("Rectangle perimeter = {:0.2f}".format(perimeter))
    elif shape == 3:
        side = float(input('Square length: '))
        perimeter = side * 4
        print("Square perimeter = {:0.2f}".format(perimeter))
    elif shape == 4:
        side1 = float(input('Triangle side 1: '))
        side2 = float(input('Triangle side 2: '))
        side3 = float(input('Triangle side 3: '))
        perimeter = (side1 + side2 + side3)
        print("Triangle perimeter = {:0.2f}".format(perimeter))

