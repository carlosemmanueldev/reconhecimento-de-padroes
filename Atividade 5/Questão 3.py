import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder

cols = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']

buying = ['low', 'med', 'high', 'vhigh']
maint = ['low', 'med', 'high', 'vhigh']
doors = ['2', '3', '4', '5more']
persons = ['2', '4', 'more']     
lug_boot = ['small', 'med', 'big']    
safety = ['low', 'med', 'high']
classification = ['unacc', 'acc', 'good', 'vgood']

data = pd.read_csv('car.data', header=None, names=cols, sep=',')

enc = OrdinalEncoder(categories=[buying, maint, doors, persons, lug_boot, safety, classification])
data = pd.DataFrame(enc.fit_transform(data), columns=cols)

data.head()