import os
from time import time

def time_spent(start) -> float:
    formated_time = time() - start
    if(formated_time < 10):
        return f"00:0{formated_time:.0f}"
    elif(formated_time < 60):
        return f"00:{formated_time:.0f}"
    elif(formated_time < 3600):
        minutes = int(formated_time // 60)
        seconds = formated_time % 60
        return f"{minutes}:{seconds:.2f}"
    else:
        hours = int(formated_time // 3600)
        minutes = int((formated_time % 3600) // 60)
        seconds = formated_time % 60
        return f"{hours}:{minutes}:{seconds:.2f}s"


def time_estimated(start, percentage) -> float:
    if(percentage > 0 and percentage < 100):
        estimated_time = (time() - start) * (100 / percentage)
        remaining_time = estimated_time - (time() - start)
        if(remaining_time < 10):
            return f"00:0{remaining_time:.0f}"
        elif(remaining_time < 60):
            return f"00:{remaining_time:.0f}"
        elif(remaining_time < 3600):
            minutes = int(remaining_time // 60)
            seconds = remaining_time % 60
            return f"{minutes}:{seconds:.2f}"
        else:
            hours = int(remaining_time // 3600)
            minutes = int((remaining_time % 3600) // 60)
            seconds = remaining_time % 60
            return f"{hours}:{minutes}:{seconds:.2f}s"
    return "00:00"


def iter_per_sec(start, iteration) -> float:
    time_spent = time() - start
    if time_spent > 0:
        return f"{iteration / time_spent:.2f}"

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_length = os.get_terminal_size().columns - 50
    starting_time = time()
    if bar_length < 2:
        bar_length = 2
    for i, elem in enumerate(lst):
        percent = ((i + 1) / total * 100)
        filled_length = int(bar_length * (i + 1) / total)
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)
        time_done = time_spent(starting_time)
        time_remain = time_estimated(starting_time, percent)
        its = iter_per_sec(starting_time, i + 1)
        print(f'\r{percent:.0f}%|{bar}| {i+1}/{total} [{time_done}<{time_remain}, {its}it/s]', end='')
        yield elem
    print()