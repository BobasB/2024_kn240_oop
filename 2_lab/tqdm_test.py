from tqdm import tqdm
from time import sleep
r = range(5)
for i in tqdm(r):
    sleep(1)

import psutil
import os
import time

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # в MB

if __name__ == "__main__":
    print(f"Початкова памʼять: {get_memory_usage():.2f} MB")

    with open("example.csv", encoding="utf-8") as f:
        for line in f:
            pass  # або обробка

    print(f"Після читання файлу: {get_memory_usage():.2f} MB")

