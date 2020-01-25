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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def telemarketers(call_records, text_records):
    send_calls = []
    receive_calls = []
    send_texts = []
    receive_texts = []
    possible = []
    for call_record in call_records:
        if call_record[0] not in send_calls:
            send_calls.append(call_record[0])
        if call_record[1] not in receive_calls:
            receive_calls.append(call_record[1])
    for text_record in text_records:
        if text_record[0] not in send_texts:
            send_texts.append(text_record[0])
        if text_record[1] not in receive_texts:
            receive_texts.append(text_record[1])
    for number in send_calls:
        if number not in receive_calls and number not in send_texts and number not in receive_texts:
            possible.append(number)
    return possible


print("These numbers could be telemarketers: ")
for telemarketer in telemarketers(calls, texts):
    print(telemarketer)
