class BankAccount:
    def __init__(self):
        self.balance = 0
        self.opened = False

    def get_balance(self):
        self.check_availability()
        return self.balance

    def open(self):
        if self.opened:
            raise ValueError("This account is already opened!")
        self.opened = True

    def deposit(self, amount):
        self.check_availability()
        if amount >= 0:
            self.balance += amount
        else:
            raise ValueError("Cannot deposit negative amount!")

    def withdraw(self, amount):
        self.check_availability()
        if 0 <= amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError(
                f"Cannot withdraw {amount}! Your balance is {self.balance}."
            )

    def close(self):
        if not self.opened:
            raise ValueError("This account is already closed!")
        self.opened = False
        self.balance = 0

    def check_availability(self):
        if not self.opened:
            raise ValueError(
                "This account is closed! \
                Cannot proceed with the operation!"
            )
