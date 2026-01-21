from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def human_format(x, pos):
    """ 
    Formats a number into a human-readable string with suffixes.
    """
    if x >= 1e9:
        return f"{x/1e9:.1f}B"
    elif x >= 1e6:
        return f"{x/1e6:.1f}M"
    elif x >= 1e3:
        return f"{x/1e3:.0f}K"
    return str(int(x))


def parse_population(value: str) -> float:
    """
    Parses a population value from a string to a float.
    """
    if isinstance(value, str):
        value = value.strip()
        if value.endswith("B"):
            return float(value[:-1]) * 1e9
        if value.endswith("M"):
            return float(value[:-1]) * 1e6
        return float(value)
    return value


def set_country_data(data: pd.DataFrame, country_n: str) -> None:
    """"
    Sets and plots the population data for a given country.
    """
    country = data.loc[data["country"] == country_n]

    years = country.columns[1:].astype(int)
    population = country.iloc[0, 1:].apply(parse_population)

    mask = (years >= 1800) & (years <= 2050)

    plt.plot(years[mask], population[mask], label=country_n)


def main():
    """
    Main function to load data and plot population for specific countries.
    """
    try:
        path = "/home/dakojic/Documents/population_total.csv"
        data = load(path)
        if data is None:
            return
        set_country_data(data, "China")
        set_country_data(data, "France")
        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(human_format))
        plt.title("Population by country (1800–2050)")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend()
        plt.grid()
        plt.show()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        exit(0)


if __name__ == "__main__":
    main()
