import math


class Figure:
    sides_count = 0

    def __init__(self, colors: list, *sides: int, filled=False):
        if sides is None or len(sides) != self.sides_count:
            sides = [1] * self.sides_count
        trust_colors = []
        for color in colors:
            if 0 <= color <= 255:
                trust_colors.append(color)
            else:
                trust_colors.append(0)
        self.__color = trust_colors
        self.__sides = sides
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        colors = [r, g, b]
        for color in colors:
            if not 0 <= color <= 255:
                return False
        return True

    def set_color(self, r, g, b):
        check = self.__is_valid_color(r, g, b)
        if check:
            self.__color = [r, g, b]


    def __is_valid_sides(self, *sides):
        count = 0
        for side in sides:
            if isinstance(side, int) and side > 0:
                count += 1
        if count == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        p = 0
        for side in self.__sides:
            p += side
        return p

    def set_sides(self, *new_sides):
        check = []
        for side in new_sides:
            if isinstance(side, int):
                check.append(side)
            else:
                break
        if len(check) == self.sides_count:
            self.__sides = check


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius() ** 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        p = 0.5 * (a + b + c)  # or p = 1/2 * sum(self.__sides)
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, colors, *sides, filled=False):
        sides *= self.sides_count
        super().__init__(colors, *sides, filled=filled)

    def get_volume(self):
        return self.get_sides()[0] ** 3


if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, радиус)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
