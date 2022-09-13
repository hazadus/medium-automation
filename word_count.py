import csv
import re

INPUT_CSV_FILE = 'hazadus_lair_all_messages.csv'
OUTPUT_CSV_FILE = 'word_stats.csv'
INPUT_COLUMN_TITLE = 'message'

stop_words = ['это', 'что', 'как', 'там', 'все', 'надо', 'уже', 'есть', 'вот', 'так', 'ещё', 'для', 'тоже', 'или',
              'если', 'только', 'его', 'может', 'будет', 'мне', 'меня', 'еще', 'нас', 'пока', 'чтобы', 'можно', 'тут',
              'тебе', 'вроде', 'теперь', 'где', 'очень', 'что-то', 'было', 'она', 'нет', 'вообще', 'чего', 'тебя',
              'без', 'http', 'https', 'они', 'сам', 'про', 'при', 'com', 'нам', 'кто', 'этот', 'какая', 'какие', 'ним',
              'них', 'чем', 'ему', 'эту', 'всё', 'себя', 'либо', 'наш', 'вас', 'эти', 'такой', 'хоть', 'вам', 'оно',
              'эта']


def sort_words_by_count_desc(word_count_list: list) -> list:
    sorted_list = word_count_list[:]  # copy

    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[j][0] > sorted_list[i][0]:
                sorted_list[j], sorted_list[i] = sorted_list[i], sorted_list[j]

    return sorted_list


all_words = []
word_count = []

# Get all words into list
with open(INPUT_CSV_FILE, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    msg_count = 0
    for row in reader:
        message = row[INPUT_COLUMN_TITLE].lower()
        message = re.sub(r'[\W\d]', r' ', message)
        all_words.extend(list(message.split()))
        msg_count += 1
    print('Total messages:', msg_count)

# Count words / remove dupes
print('Word count:', len(all_words))
for word in all_words:
    if word not in stop_words and len(word) > 2:
        word_count.append([all_words.count(word), word])

    for _ in range(all_words.count(word)):  # remove dupes
        all_words.remove(word)

# TODO: save stats in CSV or Excel
print('Unique word count:', len(word_count))
print('Word stats:')

sorted_words = sort_words_by_count_desc(word_count)

for word in sorted_words:
    if word[0] > 3:
        print(f' - {word[0]} \t {word[1]}')

# https://www.wordclouds.com - create fun wordclouds from csv there!
with open(OUTPUT_CSV_FILE, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(sorted_words)
