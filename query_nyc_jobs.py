#! /usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata
import dotenv
import os

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

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("kpav-sd4t", limit = 2000, select = "*")

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
print(results_df)

select_clause = "job_id, agency, posting_date, salary_range_from, salary_range_to"
where_clause = "job_category='Technology, Data & Innovation' AND career_level='Entry-Level'"
order_by_clause = "posting_date DESC"
results = client.get("kpav-sd4t", limit = 10, select = select_clause, where = where_clause, order = order_by_clause)
results_df = pd.DataFrame.from_records(results)
print(results_df)

select_clause = "job_category, COUNT(job_id)"
group_by_clause = "job_category"
order_by_clause = "COUNT(job_id) DESC"
results = client.get("kpav-sd4t", limit = 10, select = select_clause, group = group_by_clause, order = order_by_clause)
results_df = pd.DataFrame.from_records(results)
print(results_df)

# if __name__ == '__main__':