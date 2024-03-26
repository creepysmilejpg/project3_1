def calculate_area(shape):
    import math
    pi = math.pi
    area = 0.00
    if shape == 1:
        radius = float(input('Circle radius: '))
        area = (radius * radius) * pi
        print("Circle area = {:0.2f}".format(area))
    elif shape == 2:
        base = float(input('Rectangle side 1: '))
        height = float(input('Rectangle side 2: '))
        area = base * height
        print("Rectangle area = {:0.2f}".format(area))
    elif shape == 3:
        side = float(input('Square length: '))
        area = side * side
        print("Square area = {:0.2f}".format(area))
    elif shape == 4:
        base = float(input('Triangle side 1: '))
        height = float(input('Triangle side 2: '))
        area = (base * height) / 2
        print("Triangle area = {:0.2f}".format(area))

