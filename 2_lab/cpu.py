from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from threading import current_thread
from time import sleep
import math

n_cpu = cpu_count()
print(f"Кількість процесорів на даному компютері: {n_cpu}")

def check_thread(v):
    """Функція для багатопоточночті через треди
    """
    thread = current_thread()
    print(f"{v}: імя потоку={thread.name}")
    a = math.sqrt(64^v)

with ThreadPoolExecutor() as executor:
    executor.map(check_thread, range(n_cpu))


def is_prime(n):
    """Перевірка, чи є число простим."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

print("Завершення")