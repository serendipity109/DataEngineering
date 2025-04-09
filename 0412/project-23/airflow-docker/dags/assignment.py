from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from bs4 import BeautifulSoup
from collections import Counter
import urllib.request
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

    with open('./00_urls.txt', 'r') as f:
        urls = [line.strip() for line in f.readlines() if line.strip()]

    for url in urls:
        index = url.rfind('/') + 1
        file = url[index:]
        data = pull(url)
        store(data, file)
        print('pulled: ' + file)
        print('--- waiting ---')
        time.sleep(15)


def combine():
    # 開啟 combo.txt 檔案以寫入模式
    with open('combo.txt', 'w', encoding='utf-8') as outfile:
        # 遍歷當前目錄下所有的 .html 檔案
        for file in glob.glob("*.html"):
            with open(file, 'r', encoding='utf-8') as infile:
                # 將每個 HTML 檔案的內容寫入 combo.txt
                outfile.write(infile.read())
    print('All HTML files have been combined into combo.txt')


def titles():
    def store_json(data, file):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print('wrote file: ' + file)

    # 讀取 combo.txt 的內容
    with open('combo.txt', 'r', encoding='utf-8') as f:
        html = f.read()

    # 替換換行符號和回車符號
    html = html.replace('\n', ' ').replace('\r', '')

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all('h3')

    titles = [item.text for item in results]

    # 將提取的標題儲存為 titles.json
    store_json(titles, 'titles.json')


def clean():
    def store_json(data, file):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print('wrote file: ' + file)

    # 讀取 titles.json 的內容
    with open('titles.json', 'r', encoding='utf-8') as f:
        titles = json.load(f)

    # 定義要移除的標點符號和數字
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~1234567890'''
    translation_table = str.maketrans("", "", punctuation)

    cleaned_titles = []
    for title in titles:
        # 移除標點符號和數字
        clean = title.translate(translation_table)
        # 移除單個字母的單詞
        clean = ' '.join([word for word in clean.split() if len(word) > 1])
        cleaned_titles.append(clean)

    # 將清理後的標題儲存為 titles_clean.json
    store_json(cleaned_titles, 'titles_clean.json')


def count_words():
    def store_json(data, file):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print('wrote file: ' + file)

    # 讀取 titles_clean.json 的內容
    with open('titles_clean.json', 'r', encoding='utf-8') as f:
        titles = json.load(f)

    words = []
    for title in titles:
        words.extend(title.split())

    # 計算單詞出現次數
    counts = Counter(words)

    # 將結果儲存為 words.json
    store_json(counts, 'words.json')



# 定義 DAG
with DAG(
    "assignment",
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    # 任務 t0：安裝 BeautifulSoup4
    t0 = BashOperator(
        task_id='install_bs4',
        bash_command='pip install beautifulsoup4',
        retries=2
    )

    # 任務 t1：執行 catalog() 函數
    t1 = PythonOperator(
        task_id='pull_course_catalog',
        python_callable=catalog
    )

    # 任務 t2：執行 combine() 函數
    t2 = PythonOperator(
        task_id='combine_html_files',
        python_callable=combine
    )

    # 任務 t3：執行 titles() 函數
    t3 = PythonOperator(
        task_id='extract_titles',
        python_callable=titles
    )

    # 任務 t4：執行 clean() 函數
    t4 = PythonOperator(
        task_id='clean_titles',
        python_callable=clean
    )

    # 任務 t5：執行 count_words() 函數
    t5 = PythonOperator(
        task_id='count_word_frequencies',
        python_callable=count_words
    )

    # 定義任務執行順序
    t0 >> t1 >> t2 >> t3 >> t4 >> t5
