import pandas as pd
import numpy as np
import math
from google.colab.data_table import DataTable

DAYS = {
  'sun': 1,
  'mon': 2,
  'tue': 3,
  'wed': 4,
  'thu': 5,
  'fri': 6,
  'sat': 7,
}

MONTHS = {
  'jan': 1,
  'feb': 2,
  'mar': 3,
  'apr': 4,
  'may': 5,
  'jun': 6,
  'jul': 7,
  'aug': 8,
  'sep': 9,
  'oct': 10,
  'nov': 11,
  'dec': 12,
}

cols = ['X', 'Y', 'month', 'day', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain', 'area'] 

data = pd.read_csv('forestfires.csv', header=0, names=cols, sep= ',')

month_cos_all = []
month_sin_all = []
day_cos_all = []
day_sin_all = []

for i, row in data.iterrows():

  month = MONTHS[row['month']]

  month_cos = round(math.cos(2 * math.pi * month / 12), 2)
  month_cos_all = np.append(month_cos_all, month_cos)

  month_sin = round(math.sin(2 * math.pi * month / 12), 2)
  month_sin_all = np.append(month_sin_all, month_sin)

  day = DAYS[row['day']]

  day_cos = round(math.cos(2 * math.pi * day / 7), 2)
  day_cos_all = np.append(day_cos_all, day_cos)

  day_sin = round(math.sin(2 * math.pi * day / 7), 2)
  day_sin_all =  np.append(day_sin_all, day_sin)

data['month_cos'] = month_cos_all
data['month_sin'] = month_sin_all
data['day_cos'] = day_cos_all
data['day_sin'] = day_sin_all

data.drop(['month', 'day'], inplace=True, axis=1)

data.head()