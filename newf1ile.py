import random
from math import sqrt, pi
import pandas as pd
from datetime import datetime

random_numeber = random.randint(1, 100)
print(random_numeber)
randomfruit = random.choice(['apple', 'banana', 'cherry'])
print(randomfruit)

def area_of_square(side):
    area = side ** 2
    return area

def areofthecircle(radius):
    area = pi * radius ** 2
    return area
square_area = area_of_square(4)
circle_area = areofthecircle(3)
print(square_area)
print(circle_area)

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Occupation': ['Engineer', 'Doctor', 'Artist']
}
df = pd.DataFrame(data)
print(df)


timenow = datetime.now()
print(timenow)