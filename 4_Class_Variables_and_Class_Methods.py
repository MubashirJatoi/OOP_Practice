class Bank:
    bank_name = "Allied Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder} Bank: {Bank.bank_name}")

user1 = Bank("Mubashir")
user2 = Bank("Ali")


user1.display()
user2.display()

Bank.change_bank_name("Habib Bank Limited")

user1.display()
user2.display()