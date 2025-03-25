import os
import random
import string

def generate_random_text(length=100, words=True):
    """
    Генерує випадковий текст.
    :param length: Довжина тексту або кількість слів
    :param words: Чи використовувати слова (True) або просто символи (False)
    :return: Згенерований рядок
    """
    if words:
        word_list = ["".join(random.choices(string.ascii_letters, k=random.randint(3, 10))) for _ in range(length)]
        return " ".join(word_list)
    else:
        return "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

def write_random_to_file(filename, text_length=100, use_words=True):
    """
    Створює файл, записує в нього випадковий текст.
    :param filename: Назва файлу
    :param text_length: Довжина випадкового тексту
    :param use_words: Використовувати слова або окремі символи
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(generate_random_text(text_length, use_words))
    print(f"Файл '{filename}' успішно створено та заповнено випадковими даними.")

if __name__ == "__main__":
    filename = input("Введіть назву файлу: ")
    text_length = int(input("Введіть довжину тексту (кількість символів або слів): "))
    use_words = input("Використовувати випадкові слова (так/ні)? ").strip().lower() == "так"
    
    write_random_to_file(filename, text_length, use_words)
