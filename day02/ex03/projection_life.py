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


def main():
    """
    Main function to load GDP and life expectancy data for 1900
    and plot a scatter plot comparing the two.
    """
    path_gdp = "/home/dakojic/Documents/gdp.csv"
    path_life = "/home/dakojic/Documents/life_expectancy_years.csv"
    try:
        data_gpd = load(path_gdp)
        if data_gpd is None:
            return
        data_life = load(path_life)
        if data_life is None:
            return
        data_gpd.set_index("country", inplace=True)
        data_life.set_index("country", inplace=True)
        gdp_1900 = data_gpd["1900"]
        life_1900 = data_life["1900"]

        data_1900 = pd.DataFrame({"gdp": gdp_1900, "life": life_1900})
        if data_1900 is None:
            return
        data_1900 = data_1900.dropna()

        plt.scatter(data_1900["gdp"], data_1900[["life"]])
        plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(human_format))
        plt.title("Life Expectancy vs GDP per Capita (1900)")
        plt.xlabel("GDP per Capita (1900)")
        plt.ylabel("Life Expectancy (1900)")
        plt.grid()
        plt.show()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        return


if __name__ == "__main__":
    main()
