from math import sqrt


def quadratic_equation(a, b, c):
    determinant = ((b ** 2) - (4 * a * c))
    if determinant < 0:
        answer = "No real roots exist"
    elif determinant == 0:
        root = (-b / (2 * a))
        answer = f"The equation has one root: x =  {root}"
    else:
        root1 = round(((-b + sqrt(determinant)) / (2 * a)), 2)
        root2 = round(((-b - sqrt(determinant)) / (2 * a)), 2)
        answer = f"The equation has two roots: x1 =  {root1}   and x2 =  {root2}"
    return answer


a = int(input("Input value of a: "))
b = int(input("Input value of b: "))
c = int(input("Input value of c: "))
print(quadratic_equation(a, b, c))
