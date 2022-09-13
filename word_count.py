import csv

all_words = []

with open('all_messages.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        # print(row['message'])
        all_words.extend(list(row['message'].lower().strip('?!:;"-=+_,.()[]0123456789').split()))

print(all_words)
for word in all_words:
    print(f" - '{word}' = {all_words.count(word)}")
