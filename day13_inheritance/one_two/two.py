from day13_inheritance.one_two.one import One


class Two(One):
    def set_xy(self, x, y):
        super().set_x(x)
        # above and below line will do the same thing
        # One.set_x(self, x)
        self.y = y

    def show_xy(self):
        super().show_x()
        # above and below line will do the same thing
        # One.show_x(self)
        print("y =", self.y)
