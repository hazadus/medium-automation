# pip install pandas
# pip install numpy
# pip install textblob
# pip install sklearn
# pip install lxml
# pip install nltk
# pip install matplotlib
# https://pypi.org/project/crazytext/
import pandas as pd
import crazytext as ct

data = pd.read_csv('all_messages.csv')

# TODO: clean source text from symbols and digits (replace them with spaces)
# TODO: make all text lowercase
# TODO: remove all words from predefined list, e.g. prepostions, etc.
dc = ct.Dataframe(df=data, col='message')
count = dc.get_df_words_frequency_count()  # [:10].plot(kind='bar')

for rownum, (indx, val) in enumerate(count.iteritems()):
    print('row number: ', rownum, 'index: ', indx, 'value: ', val)

print('Done')
