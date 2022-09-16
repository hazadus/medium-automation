"""
Counts all words in a column of csv file.
https://www.wordclouds.com - create fun wordclouds from csv there!
"""
import csv
import re

INPUT_CSV_FILE = 'hazadus_lair_all_messages.csv'
OUTPUT_CSV_FILE = 'word_stats.csv'
INPUT_COLUMN_TITLE = 'message'

# List of words excluded from counting / stats
stop_words = ['это', 'что', 'как', 'там', 'все', 'надо', 'уже', 'есть', 'вот', 'так', 'ещё', 'для', 'тоже', 'или',
              'если', 'только', 'его', 'может', 'будет', 'мне', 'меня', 'еще', 'нас', 'пока', 'чтобы', 'можно', 'тут',
              'тебе', 'вроде', 'теперь', 'где', 'очень', 'что-то', 'было', 'она', 'нет', 'вообще', 'чего', 'тебя',
              'без', 'http', 'https', 'они', 'сам', 'про', 'при', 'com', 'нам', 'кто', 'этот', 'какая', 'какие', 'ним',
              'них', 'чем', 'ему', 'эту', 'всё', 'себя', 'либо', 'наш', 'вас', 'эти', 'такой', 'хоть', 'вам', 'оно',
              'эта']


def sort_words_by_count_desc(word_count_list: list) -> list:
    """
    Сортируем список, содержащий статистику по количеству слов, по убыванию.

    :param word_count_list: список, например: [[1, "word"], [10, "stats"]], etc.
    :type word_count_list: List[List[int, str]]

    :return: отсортированный по убыванию список, например [[10, "stats"], [1, "word"]]
    :rtype: List[List[int, str]]
    """
    sorted_list = word_count_list[:]  # copy

    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[j][0] > sorted_list[i][0]:
                sorted_list[j], sorted_list[i] = sorted_list[i], sorted_list[j]

    return sorted_list


all_words = list()
unique_words = list()
word_stats = list()  # Format: [[1, "word"], [10, "stats"]], etc.
msg_count = 0

# Get all words into list
with open(INPUT_CSV_FILE, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        message = row[INPUT_COLUMN_TITLE].lower()
        message = re.sub(r'[\W\d]', r' ', message)
        all_words.extend(list(message.split()))
        msg_count += 1

# Remove dupes, then count unique words (which are not in stop list and longer than two symbols)
unique_words = set(all_words)
word_stats = [[all_words.count(word), word] for word in unique_words if word not in stop_words and len(word) > 2]

# Sort, save in CSV
sorted_words = sort_words_by_count_desc(word_stats)
with open(OUTPUT_CSV_FILE, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(sorted_words)

# Print all the stats to console
print('\U0001F4CATotal messages:\t{:,d}'.format(msg_count))
print('\U0001F4CCTotal words:\t\t{:,d}'.format(len(all_words)))
print('\U0001F4CCUnique words:\t\t{:,d}'.format(len(word_stats)))
print('\nWord rating:\nCount\tWord')
print('\n'.join([f'{word[0]}\t\t{word[1]}'
                 for word in sorted_words
                 if word[0] > 3  # filter by number of occurences
                 ]))
