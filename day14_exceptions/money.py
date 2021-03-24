from day14_exceptions.invalid_amount_exception import InvalidAmountException


class Money:
    def __init__(self, rupee: int = 0, paisa: int = 0):
        self.rupee = rupee
        self.paisa = paisa
        if self.rupee < 0 or self.paisa < 0:
            raise InvalidAmountException(self)

    def _get_in_paisa(self):
        return self.rupee * 100 + self.paisa

    @staticmethod
    def _get_money(rupee=0, paisa=0):
        if paisa > 100:
            carry = paisa // 100
            rupee += carry
            paisa %= 100
        return Money(rupee, paisa)

    def __str__(self) -> str:
        return f"₹{self.rupee}.{self.paisa}"

    def __lt__(self, other):
        m1 = self._get_in_paisa()
        m2 = other._get_in_paisa()
        return m1 < m2

    def __le__(self, other):
        m1 = self._get_in_paisa()
        m2 = other._get_in_paisa()
        return m1 <= m2

    def __gt__(self, other):
        m1 = self._get_in_paisa()
        m2 = other._get_in_paisa()
        return m1 > m2

    def __ge__(self, other):
        m1 = self._get_in_paisa()
        m2 = other._get_in_paisa()
        return m1 >= m2

    def __eq__(self, other):
        m1 = self._get_in_paisa()
        m2 = other._get_in_paisa()
        return m1 == m2

    def __nq__(self, other):
        m1 = self._get_in_paisa()
        m2 = other._get_in_paisa()
        return m1 != m2

    def _normalise(self):
        if self.paisa >= 100:
            self.rupee += (self.paisa // 100)
            self.paisa = self.paisa % 100

    # def __add__(self, other):
    #     money = Money()
    #     money.rupee = self.rupee + other.rupee
    #     money.paisa = self.paisa + other.paisa
    #     money._normalise()
    #     if money.rupee < 0 or money.paisa < 0:
    #         raise InvalidAmountException(money)
    #     return money

    def __add__(self, other):
        m1 = self._get_in_paisa()
        m2 = other._get_in_paisa()
        return Money._get_money(paisa=m1 + m2)

    def __sub__(self, other):
        m1 = self._get_in_paisa()
        m2 = other._get_in_paisa()
        return Money._get_money(paisa=m1 - m2)

    def __iadd__(self, other):
        m1 = self._get_in_paisa()
        m2 = other._get_in_paisa()
        return Money._get_money(paisa=m1 + m2)

    def __isub__(self, other):
        m1 = self._get_in_paisa()
        m2 = other._get_in_paisa()
        return Money._get_money(paisa=m1 - m2)


m1 = Money(50, 60)
m2 = Money(30, 80)
print(f"m1 = {m1}")
print(f"m2 = {m2}")
print(f"m1 > m2 = {m1 > m2}")
print(f"m1 >= m2 = {m1 >= m2}")
print(f"m1 < m2 = {m1 < m2}")
print(f"m1 <= m2 = {m1 <= m2}")
print(f"m1 == m2 = {m1 == m2}")
print(f"m1 != m2 = {m1 != m2}")
print(f"m1 + m2 = {m1 + m2}")
print(f"m1 - m2 = {m1 - m2}")
m1 += m2
print(f"m1 += m2 = {m1}")
m1 -= m2
print(f"m1 -= m2 = {m1}")
