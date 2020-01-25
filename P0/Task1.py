"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
import numpy as np


def number_unique(text, call):
    phone_numbers = []
    for record in text:
        phone_numbers.append(record[0])
        phone_numbers.append(record[1])
    for record in call:
        phone_numbers.append(record[0])
        phone_numbers.append(record[1])
    return len(np.unique(phone_numbers))


print("There are", number_unique(texts, calls), "different telephone numbers in the records.")
