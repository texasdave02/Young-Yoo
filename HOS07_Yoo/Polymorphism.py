class Parrot:
    def fly(self):
        print("Parrot can fly")


class Penguin:
    def fly(self):
        print("Penguin cannot fly")


def flying_test(bird):
    bird.fly()


blu = Parrot()
peggy = Penguin()

flying_test(blu)
flying_test(peggy)
