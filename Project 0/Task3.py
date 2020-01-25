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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def called(records):
    numbers = []
    for record in records:
        if record[0][:5] == "(080)" and record[1] not in numbers:
            numbers.append(record[1])
    return numbers


def codes(numbers):
    list_of_codes = []
    for number in numbers:
        if number[0] == "(":
            if number[1:number.index(")")] not in list_of_codes:
                list_of_codes.append(number[1:number.index(")")])
        elif int(number[0]) in [7, 8, 9]:
            if number[:4] not in list_of_codes:
                list_of_codes.append(number[:4])
    return list_of_codes


def percentage(records):
    from_singapore = 0
    to_singapore = 0
    for record in records:
        if record[0][:5] == "(080)":
            from_singapore += 1
            if record[1][:5] == "(080)":
                to_singapore += 1
    return float(to_singapore)/from_singapore


print("The numbers called by people in Bangalore have codes:")
for code in codes(called(calls)):
    print(code)

print()

print("{:0.2f}".format(percentage(calls)), "percent of calls from fixed lines in Bangalore are calls to other fixed "
                                           "lines in Bangalore.")
