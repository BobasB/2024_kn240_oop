class MyClass:
    def __init__(self, surname:str, name:str, mark:int): # у конструктор передаються аргументи
        print("Викликали конструктор!")
        # а тут визначаємо атрибути обєкта
        self.surname = surname
        self.name = name
        self.mark = mark
        #self.penalty = None # можеми записати динамічний атрибут тут, але він перстане бути динамічним
        print("Завершили присвоєння атрибутів")

    
    def __repr__(self):
        return f"MyClass(Ніяких аргументів не переаємо)"

class MySecondClass:
    pass

