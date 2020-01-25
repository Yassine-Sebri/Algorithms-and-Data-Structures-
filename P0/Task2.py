"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def numbers_list(records):
    numbers = []
    for record in records:
        if record[0] not in numbers:
            numbers.append(record[0])
        if record[1] not in numbers:
            numbers.append(record[1])
    return numbers


def time_spent(numbers, records):
    time = {}
    for number in numbers:
        time[number] = 0
    for record in records:
        time[record[0]] += int(record[3])
        time[record[1]] += int(record[3])
    return time


def most_time(time):
    maximum_time = None
    maximum_number = None
    for number in time:
        if maximum_time is None or time[number] > maximum_time:
            maximum_time = time[number]
            maximum_number = number
    return maximum_number, maximum_time


print(most_time(time_spent(numbers_list(calls), calls))[0], "spent the longest time,", most_time(
    time_spent(numbers_list(calls), calls))[1], "seconds, on the phone during September 2016.")
