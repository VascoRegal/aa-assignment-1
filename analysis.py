import pandas as pd
import os
import json
import matplotlib.pyplot as plt

def load_runs(output_dir):
    runs = []
    for f in os.listdir(output_dir):
        
        with open(f"{output_dir}/{f}", 'r') as run:
            runs.append(json.loads(next(run)))
    return runs


def greedy_vs_exhaustive_time_linear(greedy_runs, exhaustive_runs, log=False):
    plt.plot(greedy_runs['V'], greedy_runs['time'], label="greedy")
    plt.plot(exhaustive_runs['V'], exhaustive_runs['time'], label="exhaustive")

    plt.xlabel("Number of Vertexes")
    plt.ylabel("Execution Time (s)")
    plt.title("Greedy vs Exhaustive execution time")
    plt.legend()
    plt.show()    

df = pd.DataFrame(load_runs("./runs"))
df['solution_len'] = df['solution'].apply(lambda r: len(r))
greedy_runs = df.loc[df['greedy'] == True].sort_values(by='V')
exhaustive_runs = df.loc[df['greedy'] == False].sort_values(by='V')


greedy_vs_exhaustive_time_linear(greedy_runs, exhaustive_runs)