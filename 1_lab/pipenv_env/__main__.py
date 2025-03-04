from bank import BankAccount
from animals import *

if __name__ == "__main__":
    # Демонстрація роботи
    account = BankAccount("Богдан", 1000)
    print(account.owner)  # Публічний атрибут доступний
    # print(account.__balance)  # Викличе помилку, бо атрибут приватний

    account.deposit(500)
    account.withdraw(300)
    print("Поточний баланс:", account.get_balance)

    # Примусове звернення до приватного атрибута (небажано)
    print("Прямий доступ:", account._BankAccount__balance)  # Можливий, але не рекомендований підхід
    # Демонстрація наслідування
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    print(f"{dog.name} каже: {dog.make_sound()}")  # Виведе: Buddy каже: Woof! Woof!
    print(f"{cat.name} каже: {cat.make_sound()}")  # Виведе: Whiskers каже: Meow!