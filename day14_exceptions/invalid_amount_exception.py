class InvalidAmountException(Exception):
    def __init__(self, rupee, paisa):
        self.rupee = rupee
        self.paisa = paisa

    def __str__(self) -> str:
        return f"Invalid amount ₹{self.rupee}.{self.paisa}"
