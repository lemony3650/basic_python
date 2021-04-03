import pandas as pd

s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
d = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns= ['a', 'b', 'c'])

d.head()
d.describe()
