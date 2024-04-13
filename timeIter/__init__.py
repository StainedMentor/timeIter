import time
import tkinter as tk
from pandastable import Table
import pandas as pd

measurements = {}

iter_start = 0
show_in_window = False


def measure(name):
    global iter_start
    now = time.time()
    diff = now - iter_start
    if measurements.keys().__contains__(name):
        measurements[name].append(diff)

    else:
        measurements[name] = [diff]
    iter_start = time.time()

def start():
    global iter_start
    if show_in_window:
        df = get_measurement_stats()
        # show(df)
    iter_start = time.time()



def get_measurement_stats():
    df = pd.DataFrame(measurements)

    min_values = df.min()
    max_values = df.max()
    average_values = df.mean()

    result_df = pd.DataFrame({
        'Measure': df.columns,
        'Minimum': min_values.values,
        'Maximum': max_values.values,
        'Average': average_values.values
    })

    return result_df

def print_all():
    df = get_measurement_stats()
    print(df)


def window():

    df = get_measurement_stats()

    df = df.astype('string')

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack(fill='both', expand=True)
    table = Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True)
    table.show()

    root.mainloop()

