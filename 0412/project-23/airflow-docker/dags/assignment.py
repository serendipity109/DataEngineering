from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from bs4 import BeautifulSoup
from collections import Counter
import urllib.request
import urllib.error
import time
import glob
import json

def catalog():
    def pull(url):
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
        return data

    def store(data, file):
        with open(file, 'w', encoding='utf-8') as f:
            f.write(data)
        print('wrote file: ' + file)

    urls = [
        "http://student.mit.edu/catalog/m1a.html",
        "http://student.mit.edu/catalog/m1b.html",
        "http://student.mit.edu/catalog/m1c.html",
        "http://student.mit.edu/catalog/m2a.html",
        "http://student.mit.edu/catalog/m2b.html",
        "http://student.mit.edu/catalog/m2c.html",
        "http://student.mit.edu/catalog/m3a.html",
        "http://student.mit.edu/catalog/m3b.html",
        "http://student.mit.edu/catalog/m4a.html",
        "http://student.mit.edu/catalog/m4b.html",
        "http://student.mit.edu/catalog/m4c.html",
        "http://student.mit.edu/catalog/m4d.html",
        "http://student.mit.edu/catalog/m4e.html",
        "http://student.mit.edu/catalog/m4f.html",
        "http://student.mit.edu/catalog/m4g.html",
        "http://student.mit.edu/catalog/m5a.html",
        "http://student.mit.edu/catalog/m5b.html",
        "http://student.mit.edu/catalog/m6a.html",
        "http://student.mit.edu/catalog/m6b.html",
        "http://student.mit.edu/catalog/m6c.html",
        "http://student.mit.edu/catalog/m7a.html",
        "http://student.mit.edu/catalog/m8a.html",
        "http://student.mit.edu/catalog/m8b.html",
        "http://student.mit.edu/catalog/m9a.html",
        "http://student.mit.edu/catalog/m9b.html",
        "http://student.mit.edu/catalog/m10a.html",
        "http://student.mit.edu/catalog/m10b.html",
        "http://student.mit.edu/catalog/m10c.html",
        "http://student.mit.edu/catalog/m11a.html",
        "http://student.mit.edu/catalog/m11b.html",
        "http://student.mit.edu/catalog/m11c.html",
        "http://student.mit.edu/catalog/m12a.html",
        "http://student.mit.edu/catalog/m12b.html",
        "http://student.mit.edu/catalog/m12c.html",
        "http://student.mit.edu/catalog/m14a.html",
        "http://student.mit.edu/catalog/m14b.html",
        "http://student.mit.edu/catalog/m15a.html",
        "http://student.mit.edu/catalog/m15b.html",
        "http://student.mit.edu/catalog/m15c.html",
        "http://student.mit.edu/catalog/m16a.html",
        "http://student.mit.edu/catalog/m16b.html",
        "http://student.mit.edu/catalog/m18a.html",
        "http://student.mit.edu/catalog/m18b.html",
        "http://student.mit.edu/catalog/m20a.html",
        "http://student.mit.edu/catalog/m22a.html",
        "http://student.mit.edu/catalog/m22b.html",
        "http://student.mit.edu/catalog/m22c.html"
    ]

    for url in urls:
        index = url.rfind('/') + 1
        file = url[index:]
        try:
            data = pull(url)
            store(data, file)
            print('pulled: ' + file)
        except urllib.error.HTTPError as e:
            print(f'HTTPError for {url}: {e.code}. Skipping.')
        except Exception as e:
            print(f'Error for {url}: {e}. Skipping.')
        print('--- waiting ---')
        time.sleep(15)

def combine():
    with open('combo.txt', 'w', encoding='utf-8') as outfile:
        for file in glob.glob("*.html"):
            with open(file, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
    print('All HTML files have been combined into combo.txt')

def titles():
    def store_json(data, file):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print('wrote file: ' + file)

    with open('combo.txt', 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace('\n', ' ').replace('\r', '')
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all('h3')
    titles = [item.text for item in results]
    store_json(titles, 'titles.json')

def clean():
    def store_json(data, file):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print('wrote file: ' + file)

    with open('titles.json', 'r', encoding='utf-8') as f:
        titles = json.load(f)

    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~1234567890'''
    translation_table = str.maketrans("", "", punctuation)

    cleaned_titles = []
    for title in titles:
        clean_text = title.translate(translation_table)
        clean_text = ' '.join([word for word in clean_text.split() if len(word) > 1])
        cleaned_titles.append(clean_text)
    store_json(cleaned_titles, 'titles_clean.json')

def count_words():
    def store_json(data, file):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print('wrote file: ' + file)

    with open('titles_clean.json', 'r', encoding='utf-8') as f:
        titles = json.load(f)

    words = []
    for title in titles:
        words.extend(title.split())

    counts = Counter(words)
    store_json(counts, 'words.json')

with DAG(
    "assignment",
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    t0 = BashOperator(
        task_id='install_bs4',
        bash_command='pip install beautifulsoup4',
        retries=2
    )

    t1 = PythonOperator(
        task_id='pull_course_catalog',
        python_callable=catalog
    )

    t2 = PythonOperator(
        task_id='combine_html_files',
        python_callable=combine
    )

    t3 = PythonOperator(
        task_id='extract_titles',
        python_callable=titles
    )

    t4 = PythonOperator(
        task_id='clean_titles',
        python_callable=clean
    )

    t5 = PythonOperator(
        task_id='count_word_frequencies',
        python_callable=count_words
    )

    t0 >> t1 >> t2 >> t3 >> t4 >> t5
