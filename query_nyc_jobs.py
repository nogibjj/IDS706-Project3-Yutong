#! /usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata
import dotenv
import os

def get_job_category(client):
    select_clause = "job_category, COUNT(job_id)"
    group_by_clause = "job_category"
    order_by_clause = "COUNT(job_id) DESC"
    
    results = client.get("kpav-sd4t", limit = 30, select = select_clause, group = group_by_clause, order = order_by_clause)
    results_df = pd.DataFrame.from_records(results)
    print("------------------ JOB CATEGORIES ------------------")
    print(results_df)
    print("\n")

def get_career_level(client):
    select_clause = "career_level, COUNT(job_id)"
    group_by_clause = "career_level"
    order_by_clause = "COUNT(job_id) DESC"
    
    results = client.get("kpav-sd4t", select = select_clause, group = group_by_clause, order = order_by_clause)
    results_df = pd.DataFrame.from_records(results)
    print("------------------ JOB CAREER LEVELS ------------------")
    print(results_df)
    print("\n")

def filter_jobs(client, job_category = "", career_level = ""):
    select_clause = "job_id, agency, posting_date, salary_range_to, salary_frequency"
    where_clause = "posting_date > '2022-01-01T00:00:00.000'"
    if job_category != "":
        where_clause += " AND job_category='" + job_category + "'"
    if career_level != "":
        where_clause += " AND career_level='" + career_level + "'"
    order_by_clause = "posting_date DESC"

    # First 2000 results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get("kpav-sd4t", limit = 50, select = select_clause, where = where_clause, order = order_by_clause)
    results_df = pd.DataFrame.from_records(results)
    print("------------------ FILTERED JOBS ------------------")
    print(results_df)
    print("\n")

def query_nyc_jobs():
    dotenv.load_dotenv()
    TOKEN = os.getenv('TOKEN')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')

    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    # client = Socrata("data.cityofnewyork.us", None)

    # Example authenticated client (needed for non-public datasets):
    client = Socrata("data.cityofnewyork.us",
                    TOKEN,
                    username = USERNAME,
                    password = PASSWORD)
    
    get_job_category(client)
    get_career_level(client)

    job_category = input("Enter job_category you want to query: ")
    career_level = input("Enter career_level you want to query: ")
    print("\n")
    # filter_jobs("Technology, Data & Innovation", "Entry-Level")
    filter_jobs(client, job_category, career_level)


if __name__ == '__main__':
    query_nyc_jobs()
