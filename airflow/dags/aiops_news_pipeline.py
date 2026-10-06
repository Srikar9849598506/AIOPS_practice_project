import sys

from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


sys.path.insert(0, "/opt/airflow/src")

URL = "https://news.ycombinator.com/"


def scrape_task():
    from scraper import scraper

    text = scraper(URL)

    print("Website scraped successfully!")
    print(f"Scraped characters: {len(text)}")

    return text


def summarize_task(**context):
    from summarizer import summarize

    text = context["ti"].xcom_pull(task_ids="scrape_task")

    summary = summarize(text)

    print("Summary generated:")
    print(summary)

    return summary


def firebase_task(**context):
    from firebase import save_summary

    summary = context["ti"].xcom_pull(task_ids="summarize_task")

    save_summary(summary)

    print("Summary saved to Firebase!")


with DAG(
    dag_id="aiops_news_pipeline",
    start_date=datetime(2026, 9, 27),
    schedule="*/15 * * * *",
    catchup=False,
    max_active_runs=1,
    tags=["aiops", "news", "ollama", "firebase"],
) as dag:

    scrape = PythonOperator(
        task_id="scrape_task",
        python_callable=scrape_task,
    )

    summarize = PythonOperator(
        task_id="summarize_task",
        python_callable=summarize_task,
    )

    save = PythonOperator(
        task_id="firebase_task",
        python_callable=firebase_task,
    )

    scrape >> summarize >> save
