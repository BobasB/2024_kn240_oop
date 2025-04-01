from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
from time import sleep
import math

n_cpu = cpu_count()
print(f"Кількість процесорів на даному компютері: {n_cpu}")

def check_thread(v):
    thread = current_thread()
    print(f"{v}: імя потоку={thread.name}")
    a = math.sqrt(64^v)

with ThreadPoolExecutor() as executor:
    executor.map(check_thread, range(n_cpu))

print("Завершення")