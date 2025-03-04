class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner        # Публічний атрибут
        self.__balance = balance  # Приватний атрибут (інкапсульований)
    
    def deposit(self, amount: float):
        """Додає кошти на рахунок"""
        if amount > 0:
            self.__balance += amount
            print(f"Депозит {amount} успішний. Новий баланс: {self.__balance}")
        else:
            print("Сума повинна бути більше 0!")

    def withdraw(self, amount: float):
        """Знімає кошти з рахунку, якщо баланс дозволяє"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Знято {amount}. Залишок на рахунку: {self.__balance}")
        else:
            print("Недостатньо коштів або некоректна сума!")

    def get_balance(self):
        """Надає доступ до балансу (через метод, а не напряму)"""
        return self.__balance


# Демонстрація роботи
account = BankAccount("Іван", 1000)
print(account.owner)  # Публічний атрибут доступний
# print(account.__balance)  # Викличе помилку, бо атрибут приватний

account.deposit(500)
account.withdraw(300)
print("Поточний баланс:", account.get_balance())

# Примусове звернення до приватного атрибута (небажано)
print("Прямий доступ:", account._BankAccount__balance)  # Можливий, але не рекомендований підхід
