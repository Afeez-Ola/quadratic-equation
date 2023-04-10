from math import sqrt


def quadratic_equation():
    a = int(input("Input value of a: "))
    b = int(input("Input value of b: "))
    c = int(input("Input value of c: "))

    determinant = (b ^ 2 - 4 * a * c)
    if determinant < 0:
        return "No real roots exist"
    elif determinant == 0:
        root = (-b / 2 * a)
        return "The equation has one root: x = " + root
    else:
        root1 = ((-b + sqrt(determinant)) / 2*a)
        root2 = ((-b - sqrt(determinant)) / 2*a)
        return "The equation has two roots: x1 = " + root1 + " and x2 = " + root2


print(quadratic_equation())