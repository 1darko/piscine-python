from typing import Any

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]
    
def calculate_quartiles(data):
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
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / (len(data))
    std = variance ** 0.5
    return std

def calculate_var(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    # for arg in args:
    #     print(f"Arg: {arg}")

    for key, value in kwargs.items():
        if(len(args) == 0):
            print("ERROR")
        elif value in ["mean", "median", "quartile", "std", "var"]:
            data = [float(i) for i in args]
            if value == "mean":
                print(f"The mean is: {calculate_mean(data)}")
            elif value=="median":
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

ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5,5,5,5,5,5,5, ejfhhe="ewqqw", ejdjdejn="median")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")