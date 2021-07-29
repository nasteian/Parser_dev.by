import csv

def save_file(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(['Вакансия', 'Ссылка', 'Компания', 'З/П', 'Тип работы'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['company'], item['salary'], item['type_of_work']])