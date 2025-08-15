import pandas as pd


def classify(df):
    if df['safety'] == 'low' or df['maint'] == 'vhigh':
        return 'unacc'
    else:
        if df['buying'] == 'vhigh' or df['buying'] == 'high':
            if df['safety'] == 'high':
                if df['maint'] == 'high':
                    return 'unacc'
                else:
                    return 'acc'
            else:
                if df['maint'] == 'high' or df['maint'] == 'med':
                    return 'unacc'
                else:
                    return 'acc'
        else:
            if df['buying'] == 'med':
                if df['safety'] == 'high':
                    if df['maint'] == 'high':
                        return 'acc'
                    elif df['maint'] == 'med':
                        return 'good'
                    else:
                        return 'vgood'
                else:
                    if df['maint'] == 'high':
                        return 'unacc'
                    elif df['maint'] == 'med':
                        return 'acc'
                    else:
                        return 'good'
            else:
                if df['safety'] == 'high':
                    if df['maint'] == 'high':
                        return 'good'
                    elif df['maint'] == 'med':
                        return 'vgood'
                    else:
                        return 'vgood'
                else:
                    if df['maint'] == 'high':
                        return 'acc'
                    elif df['maint'] == 'med':
                        return 'vgood'
                    else:
                        return 'vgood'

data = pd.read_csv('car.data.test', header=None,
                   names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class'])

print('Classe Real - Classe Prevista')

cont = 0
for i, value in data.iterrows():
    print(value['class'], '-', classify(value))
    if classify(value) == value['class']:
        cont += 1

print('Resultado: ', cont/len(data))