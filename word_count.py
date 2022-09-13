import csv

stop_words = ['не', 'в', 'и', 'на', 'это', 'я', 'с', 'а', 'что', 'ты', 'у', 'как', 'по', 'там', 'за', 'да', 'он', 'ну',
              'все', 'надо', 'уже', 'есть', 'от', 'вот', 'но', 'так', '-', 'вы', 'ещё', 'для', 'тоже', 'или', 'то',
              'если', 'к', 'только', 'мы', 'его', 'может', 'будет', 'мне', 'меня', 'же', 'еще', 'нас', 'пока', 'чтобы',
              'можно', 'тут', 'тебе', 'до', 'вроде', 'теперь', 'где', 'очень', 'что-то', 'бы', 'из', 'было', 'она',
              'да', 'ее', 'её', 'нет', 'вообще', 'чего', 'не', 'во', '—']


def sort_words(word_count_list):
    sorted_list = word_count_list[:]  # copy

    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            a = sorted_list[j]
            b = sorted_list[i]
            if sorted_list[j][1] > sorted_list[i][1]:
                sorted_list[j], sorted_list[i] = sorted_list[i], sorted_list[j]

    return sorted_list


all_words = []
word_count = []

# TODO: count messages
# TODO: count words
# TODO: count same by user?

# Get all words into list
with open('all_messages.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        # print(row['message'])
        all_words.extend(list(row['message'].lower().strip('?!:;"-=+_,.()[]0123456789…').split()))

# Count words / remove dupes
# TODO: better stripping needed!
print(all_words)
for word in all_words:
    print(f" - '{word}' = {all_words.count(word)}")

    if not word in stop_words:
        word_count.append([word, all_words.count(word)])

    for _ in range(all_words.count(word)):  # remove dupes
        all_words.remove(word)

# TODO: save stats in CSV or Excel
print(sort_words(word_count))
