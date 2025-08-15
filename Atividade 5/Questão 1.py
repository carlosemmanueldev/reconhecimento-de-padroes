import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.model_selection import train_test_split
from google.colab.data_table import DataTable

#Letra B
DataTable.max_columns = 50

cols = [
    'school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup',
    'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2', 'G3'
    ]

binary = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']

data = pd.read_csv('student-mat.csv', header=0, names=cols, sep= ';')

for i in range(len(binary)):
  le = LabelEncoder()
  data[binary[i]] = le.fit_transform(data[binary[i]])

transformer = make_column_transformer((OneHotEncoder(), ['Mjob', 'Fjob', 'reason', 'guardian']), remainder='passthrough')
transformed = transformer.fit_transform(data)
transformed_data = pd.DataFrame(transformed, columns=transformer.get_feature_names_out())

transformed_data.head()

#Letra C
transformed_data['remainder__G3'] = pd.cut(x=transformed_data['remainder__G3'],
                     bins=[-1, 13, 20],
                     labels=['Failed ', 'Approved'])

transformed_data.head()

#Letra D
cols_new = [
    'onehotencoder__Mjob_at_home',	'onehotencoder__Mjob_health',	'onehotencoder__Mjob_other',	'onehotencoder__Mjob_services',	'onehotencoder__Mjob_teacher',	'onehotencoder__Fjob_at_home',	'onehotencoder__Fjob_health',	'onehotencoder__Fjob_other',	'onehotencoder__Fjob_services',	'onehotencoder__Fjob_teacher', 'onehotencoder__reason_course', 'onehotencoder__reason_home', 'onehotencoder__reason_other', 'onehotencoder__reason_reputation', 'onehotencoder__guardian_father', 'onehotencoder__guardian_mother', 'onehotencoder__guardian_other', 'remainder__school', 'remainder__sex', 'remainder__age', 'remainder__address', 'remainder__famsize', 'remainder__Pstatus', 'remainder__Medu', 'remainder__Fedu', 'remainder__traveltime', 'remainder__studytime', 'remainder__failures', 'remainder__schoolsup', 'remainder__famsup', 'remainder__paid', 'remainder__activities', 'remainder__nursery', 'remainder__higher', 'remainder__internet', 'remainder__romantic', 'remainder__famrel', 'remainder__freetime', 'remainder__goout', 'remainder__Dalc', 'remainder__Walc', 'remainder__health', 'remainder__absences', 'remainder__G1', 'remainder__G2', 'remainder__G3'
]
data_x = transformed_data[cols_new[:-1]]
data_y = transformed_data['remainder__G3']
data_scores = []

for i in range(100):
  data_train_x, data_test_x, data_train_y, data_test_y = train_test_split(data_x, data_y, test_size=0.5)

  knn = KNeighborsClassifier(n_neighbors = 1, weights="distance", metric="euclidean")
  knn.fit(data_train_x, data_train_y)

  predict = knn.predict(data_test_x)
  data_score = knn.score(data_test_x, data_test_y)
  data_scores = np.append(data_scores, data_score)

med_1 = np.average(data_scores)
dev_1 = data_scores.std()

confidence_interval_1_n = round(med_1 - (1.96 * dev_1), 5)
confidence_interval_1_p = round(med_1 + (1.96 * dev_1), 5)

print(f'Intervalo de confiança da taxa de acerto: {confidence_interval_1_n}   {confidence_interval_1_p}')