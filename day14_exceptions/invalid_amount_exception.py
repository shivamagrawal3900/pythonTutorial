class InvalidAmountException(Exception):
    def __init__(self, money):
        self.money = money

    def __str__(self) -> str:
        return f"Invalid amount {self.money}"
