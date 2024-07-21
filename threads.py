from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
import requests

start = perf_counter()
urls = range(1, 1000)


def get_data(url):
    r = requests.get(f'http://127.0.0.1:8000/items/{url}')
    print(r.json())


with ThreadPoolExecutor() as executor:
    executor.map(get_data, urls)

stop = perf_counter()
print("Thread time taken:", stop - start)