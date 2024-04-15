from builtins import print as base_print
class Circle:
    all_circles = []
    pi = 3.1415

    def __init__(self, radius = 1):
        self.radius = radius
        Circle.all_circles.append(self)

    def area(self):
        return Circle.pi * self.radius**2

    @staticmethod
    def total_area():
        return sum(circle.area() for circle in Circle.all_circles)

    def __repr__(self):
        return f'{self.radius}'

'''def print(n):
    if n.__class__.__name__ == 'Circle':
        base_print(n.radius)
    elif hasattr(n, '__iter__'):
        array = []
        for i in n:
            array.append(i.radius)
        base_print(array)
    else:
        base_print(n)
'''

c1 = Circle()
c2 = Circle(7)
c3 = Circle(5)
print(c2.area())
print(c3)
print(Circle.pi)
print(Circle.all_circles)
print(Circle.total_area())
print(len(c3.__class__.all_circles))
