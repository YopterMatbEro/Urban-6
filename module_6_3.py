class Horse:
    def __init__(self, x_distance: int = 0, sound: str = 'Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx: int):
        self.x_distance += dx


class Eagle:
    def __init__(self, y_distance: int = 0, sound: str = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy: int):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self, x_distance: int = 0, y_distance: int = 0, sound: str = 'I train, eat, sleep, and repeat'):
        Horse.__init__(self, x_distance, sound)
        Eagle.__init__(self, y_distance, sound)

    def move(self, dx: int, dy: int):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


if __name__ == "__main__":
    p1 = Pegasus()

    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())

    p1.voice()
