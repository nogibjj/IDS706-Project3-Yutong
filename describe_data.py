#! /usr/bin/env python

import pandas

def describe_csv_data(file_name):
    df = pandas.read_csv(file_name, index_col=0)
    print(df.describe(include='all'))

if __name__ == '__main__':
    print("--------------- train data set description ---------------")
    describe_csv_data("data/train.csv")
    print("--------------- test data set description ---------------")
    describe_csv_data("data/test.csv")
