#! /usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

TOKEN = "AJQvu7Yuf7tc8JSSuBgBlmJvO"
USERNAME = "zhang.bingfen@outlook.com"
PASSWORD = "yutong@IDS706"


# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
# client = Socrata("data.cityofnewyork.us", None)

# Example authenticated client (needed for non-public datasets):
client = Socrata("data.cityofnewyork.us",
                 TOKEN,
                 username=USERNAME,
                 password=PASSWORD)

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("kpav-sd4t", limit=2000, select="job_id, agency")

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
print(results_df)

# if __name__ == '__main__':