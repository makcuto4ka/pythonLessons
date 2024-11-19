#1
print('\n#1')

import pandas as pd
fruits= ["apple", "pear", "orange", "tangerine", "banana", "kiwi", "peach", "plum", "grape", "pineapple"]
fruits_series = pd.Series(fruits)
print(fruits_series)

#2
print('\n#2')

import pandas as pd
df= pd.DataFrame({
    'fruits_1': ["apple", "pear", "orange", "tangerine", "banana"],
    'fruits_2': [ "tangerine", "banana", "kiwi", "peach", "plum"]})
print(df)
print( df[df != df.loc[df['fruits_1'].isin(df['fruits_2']), 'fruits_1'].values])

#3
print('\n#3')
