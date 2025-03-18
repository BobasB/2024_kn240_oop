#!/Users/bbuhyl/.pyenv/shims/python
from sys import argv
import os 
import argparse

import shutil
from datetime import datetime

def call_help():
    print("Ми викликали Help для нашої програми")

def display_version():
    print("Ми вивели версію")

def move_file_to_date_folder(filename):
    # Перевіряємо, чи існує файл
    if not os.path.exists(filename):
        print(f"Файл '{filename}' не знайдено.")
        return

    # Отримуємо поточну дату у форматі YYYY-MM-DD
    date_folder = datetime.now().strftime("%Y-%m-%d")

    # Створюємо папку, якщо вона не існує
    if not os.path.exists(date_folder):
        os.makedirs(date_folder)

    # Переміщуємо файл у папку
    shutil.move(filename, os.path.join(date_folder, filename))
    print(f"Файл '{filename}' переміщено в папку '{date_folder}'.")

if __name__ == "__main__":
    if False: #argv[0] == "./__main__.py":
        print(f"Запустились, на першій позцї стоїть: {argv[1]}")
        print(f"А на другій {argv[2]}")
    
    #Якщо передали не всі аргументи программа буде падати
    # і нам потрібні винятки 
    # тому придумали бібліотеку argparse

    parser = argparse.ArgumentParser(
        prog="Тестова програма", 
        description="Експерементуємо з аргументами")
    parser.add_argument("-hh", action='store_true', help="Наш тестовий ключ")
    parser.add_argument("-v", "--version", action='store_true', help="Ми додали нашу Версію!")
    args = parser.parse_args()

    #print(parser.print_help())
    if args.hh:
        call_help()
    if args.version:
        display_version()
    
    # Приклад виклику функції
    file_to_move = "example.txt"  # Замініть на реальну назву файлу
    move_file_to_date_folder(file_to_move)
