from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        path = "/home/dakojic/Documents/life_expectancy_years.csv"
        data = load(path)
        if data is None:
            return
        france = data.loc[data["country"] == "France"]
        years = france.columns[1:].astype(int)
        life_expect = france.iloc[0, 1:].astype(float)
        plt.plot(years, life_expect, marker='o')
        plt.title("Life Expectancy in France Over Years")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy (years)")
        plt.grid()
        plt.show()
        # france = data.loc[data["country"] == "France"]
        # years = france.columns[2:].astype(int)
        # life_expect = france.iloc[0, 2:].astype(float)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        exit(0)


if __name__ == "__main__":
    main()
