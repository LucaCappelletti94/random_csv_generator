from random_csv_generator import random_csv
from tqdm.auto import tqdm

def test_random_csv():
    for _ in tqdm(range(10)):
        random_csv()