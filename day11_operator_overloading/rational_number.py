class RationalNumber:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def show(self, str=""):
        print(str, self.numerator, "/", self.denominator, sep="")

    def __add__(self, other):
        p1, p2 = self.get_common_numerator(other)
        p = p1 + p2
        q = self.denominator * other.denominator
        return RationalNumber(p, q).normalise()

    def __sub__(self, other):
        p1, p2 = self.get_common_numerator(other)
        p = p1 - p2
        q = self.denominator * other.denominator
        return RationalNumber(p, q).normalise()

    def __mul__(self, other):
        p = self.numerator * other.numerator
        q = self.denominator * other.denominator
        return RationalNumber(p, q).normalise()

    def __truediv__(self, other):
        p = self.numerator * other.denominator
        q = self.denominator * other.numerator
        return RationalNumber(p, q).normalise()

    def __gt__(self, other):
        p1, p2 = self.get_common_numerator(other)
        return p1 > p2

    def __ge__(self, other):
        p1, p2 = self.get_common_numerator(other)
        return p1 >= p2

    def __lt__(self, other):
        p1, p2 = self.get_common_numerator(other)
        return p1 < p2

    def __le__(self, other):
        p1, p2 = self.get_common_numerator(other)
        return p1 <= p2

    def __int__(self):
        return self.numerator // self.denominator

    def __float__(self):
        return self.numerator / self.denominator

    def get_common_numerator(self, other):
        p1 = self.numerator * other.denominator
        p2 = other.numerator * self.denominator
        return p1, p2

    def normalise(self):
        result = RationalNumber(self.numerator, self.denominator)
        for i in range(2, int(min(self.numerator, self.denominator) ** 0.5) + 1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                result.numerator = self.numerator // i
                result.denominator = self.denominator // i
        return result


# Application
r1 = RationalNumber(3, 4)
r2 = RationalNumber(1, 2)

r1.show("Value of r1: ")
r2.show("Value of r2: ")

sum = r1 + r2
sum.show("r1 + r2 = ")

sub = r1 - r2
sub.show("r1 - r2 = ")

mul = r1 * r2
mul.show("r1 * r2 = ")

div = r1 / r2
div.show("r1 / r2 = ")

print("r1 > r2:", r1 > r2)
print("r1 >= r2:", r1 >= r2)
print("r1 < r2:", r1 < r2)
print("r1 <= r2:", r1 <= r2)

print("int(r1):", int(r1))
print("float(r1):", float(r1))
