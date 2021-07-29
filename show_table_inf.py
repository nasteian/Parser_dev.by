import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show_data(file):
    data = pd.read_csv(file, sep=';', comment='#')
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option('display.width', 200)
    pd.set_option('display.max_colwidth', 200)
    data.style.set_properties(**{'text-align': 'left'})
    # header = ['Вакансия', 'Ссылка', 'Компания', 'З/П', 'Тип работы']
    # data.columns = header + [''] * (len(data.columns) - len(header))
    data_section = data['Вакансия'].value_counts()

    data_section_max = data_section[:1]
    data_section_min = data_section[-1:]
    data_type = data['Тип работы'].value_counts()
    data_section_max = data_type[:1]
    print(data_section_max)
    data_type1 = data['Тип работы'].value_counts().count()
    print(data_type1)
    print(data.head())

    return data_type
