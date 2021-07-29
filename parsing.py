import requests
from bs4 import BeautifulSoup
from pip.save_csv import save_file
from show_table_inf import show_data
from chart import create_chart
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

URL = 'https://jobs.dev.by/'
HEADERS = {'user-agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/91.0.4472.164 Safari/537.36','accept':'*/*'}
HOST = 'https://jobs.dev.by/'
FILE = 'vacancies.csv'

def get_html(url):
    r = requests.get(url,headers = HEADERS)
    return r



def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'vacancies-list-item__body js-vacancies-list-item--open')
    vacancies = []

    for item in items:
        salary = item.find('div', class_ = 'vacancies-list-item__salary')
        company = item.find('div', class_='vacancies-list-item__company')
        type_of_work = item.find('span', class_='vacancies-list-item__label')

        if salary:
            salary = salary.get_text()
        else:
            salary = 'не указанa'
        if company and type_of_work:
            company = company.get_text().replace('Удалённо',' ')
        elif company:
            company = company.get_text()
        else:
            companies = 'не указанa'
        if type_of_work:
            type_of_work = type_of_work.get_text()
        else:
            type_of_work = 'В офисе'

        vacancies.append({
            'title': item.find('div', class_ = 'vacancies-list-item__position').get_text(strip = True),
            'link': HOST + item.find('a',class_ = 'vacancies-list-item__link_block').get('href'),
            'company': company,
            'salary': salary,
            'type_of_work': type_of_work,
        })


    return vacancies

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        vacancies = []
        vacancies.extend(get_content(html.text))
        print(len(vacancies))

    else:
        print('error')
    save_file(vacancies, FILE)
    data = show_data(FILE)
    create_chart(data)
parse()
