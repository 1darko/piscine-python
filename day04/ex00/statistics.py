from typing import Any


def calculate_mean(data):
    """Calculate the mean of a list of numbers."""
    return sum(data) / len(data)


def calculate_median(data):
    """Calculate the median of a list of numbers."""
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]


def calculate_quartiles(data):
    """Calculate the first and third quartiles of a list of numbers."""
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        lower_half = sorted_data[:mid]
        upper_half = sorted_data[mid:]
    else:
        lower_half = sorted_data[:mid]
        upper_half = sorted_data[mid + 1:]
    Q1 = calculate_median(lower_half)
    Q3 = calculate_median(upper_half)
    ret = []
    ret.append(Q1)
    ret.append(Q3)
    return ret


def calculate_std(data):
    """Calculate the standard deviation of a list of numbers."""
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / (len(data))
    std = variance ** 0.5
    return std


def calculate_var(data):
    """Calculate the variance of a list of numbers."""
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculate and print various
    statistics based on the provided arguments."""
    for key, value in kwargs.items():
        if (len(args) == 0):
            print("ERROR")
        elif value in ["mean", "median", "quartile", "std", "var"]:
            data = [float(i) for i in args]
            if value == "mean":
                print(f"The mean is: {calculate_mean(data)}")
            elif value == "median":
                print(f"The median is: {calculate_median(data)}")
            elif value == "quartile":
                print(f"quartiles: {calculate_quartiles(data)}")
            elif value == "var":
                print(f"var: {calculate_var(data)}")
            elif value == "std":
                print(f"std: {calculate_std(data)}")
            else:
                print(f"asking for {value}")
        else:
            continue
