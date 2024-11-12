from datetime import datetime

class MyClass:
    """Це буде клас для експериментів.
    Його використовуємо для лаб роботи №3

    ---
    Attributes:
    surname: Прізвище
    name: Імя

    """
    GROUP = "Група, бажано лише читати" # зверніть увагу що все з великої букви
    _data = "Це буде протектек змінна"
    __private_one = 1
    total_students = 0

    def __init__(self, surname:str, name:str, mark:int): # у конструктор передаються аргументи
        print("Викликали конструктор!")
        # а тут визначаємо атрибути обєкта
        self.surname = surname
        self.name = name
        self.mark = mark
        #self.penalty = None # можеми записати динамічний атрибут тут, але він перстане бути динамічним
        print("Завершили присвоєння атрибутів")
        self._test_protected = True

        self.__do_not_touch = "Це змінювати не можна"
        self._created = datetime.now()

        # Зробили приватні атрибути які будуть використовуватись у протектед Властивості
        self.__name = name
        self.__surname = surname

        MyClass.total_students += 1

    def __del__(self):
        print("Видалення обєкта")
        MyClass.total_students -= 1

    @property
    def full_name(self):
        """Виводимо Повне імя, але цей варіант залежить від атрибутів
        """
        return f"{self.name} {self.surname}"
    
    @property
    def full_name_protected(self):
        """Повне імя, але цей варіант незмінний після створення обєкта
        """
        return f"{self.__name} {self.__surname}"
    
    @property
    def name_uppercase(self):
        """Можемо задавати буль-які властивості!
        """
        return self.name.upper()
    
    @property
    def count_name(self):
        """Рахуємо кількість букв в імені
        """
        return len(self.name)
    
    def print_private_attributes(self):
        return self.__do_not_touch
    
    def __repr__(self):
        return f"MyClass(Ніяких аргументів не переаємо)"
    
    def __len__(self):
        return len(self.surname)
    
    def __eq__(self, value):
        if getattr(self, "mark") and getattr(value, "mark", None):
            return True if self.mark == value.mark else False
        return None
        
class MySecondClass:
    pass

