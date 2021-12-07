class Point():
    
    def __init__(self, x, x2, y, y2):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
    
    def info(self):
        p1 = (self.x, self.y)
        p2 = (self.x2, self.y2)
        print("Перед нами следующие координаты: ", (p1), (p2))

    def addition(self):
        add = self.x + self.x2, self.y + self.y2
        print("Сложение двух точек: ", (add))

    def subtraction(self):
        sub = self.x - self.x2, self.y - self.y2
        print("Разница двух точек: ", (sub))

    def multiplication(self):
        mul = self.x * self.x2, self.y * self.y2
        print("Умножение двух точек: ", (mul))
    
    def division(self):
        div = self.x / self.x2, self.y / self.y2
        print("Деление двух точек: ", (div))
    
    def exponentiation(self, c):
        exp = ((self.x + self.x2)**c, (self.y + self.y2)**c)
        print(f"При возведении координат в степень {c}, получим:  {exp}")
    
    def distance(self):
        dis = ((self.x - self.x2)**2) + ((self.y + self.y2)**2)**0.5
        print("Расстояние между двумя точками: ", (dis))
    
    

AB = Point(1, 2, 1, 2)
AB.info()
AB.addition()
AB.subtraction()
AB.multiplication()
AB.division()
AB.distance()
AB.exponentiation(2)
print("")
BC = Point(1, 2, 3, 4)
BC.info()
BC.addition()
BC.subtraction()
BC.multiplication()
BC.division()
BC.distance()
BC.exponentiation(2)


