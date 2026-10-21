print("Введите стороны треугольника")

a = float(input("Первая сторона: "))
b = float(input("Вторая сторона: "))
c = float(input("Третья сторона: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Это не треугольник!")
elif a == b == c:
    print("Равносторонний треугольник")
elif a == b or b == c or a == c:
    print("Равнобедренный треугольник")
else:
    print("Разносторонний треугольник")
