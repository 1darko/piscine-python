from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt

def main():
    path = "/home/dakojic/goinfre/life_expectancy_years.csv"
    data = load(path)
    if data is None:
        return
    france = data.loc[data["country"] == "France"]
    years = france.columns[2:].astype(int)
    life_expect = france.iloc[0, 2:].astype(float)

    

if __name__ == "__main__":
    main()