import pandas as pd
import os
import json
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def load_runs(output_dir):
    runs = []
    for f in os.listdir(output_dir):
        
        with open(f"{output_dir}/{f}", 'r') as run:
            runs.append(json.loads(next(run)))
    return runs


def greedy_vs_exhaustive_time_linear(greedy_runs, exhaustive_runs, random, log=False):
    #plt.plot(greedy_runs['V'], greedy_runs['time'], label="greedy")
    #plt.plot(exhaustive_runs['V'], exhaustive_runs['time'], label="exhaustive")
    plt.plot(random_runs['V'], random_runs['time'], label='random')
    plt.xlabel("Number of Vertexes")
    plt.ylabel("Execution Time (s) (log10)")
    plt.title("Execution time E vs G vs R")
    plt.legend()
    plt.show()    

def data_to_tex_table(data):
	print("\\begin{tabular}{|c c c c|}")
	print("\\hline")
	print(" V & E & time(s) & solution\\\\ [0.5ex] ")
	print("\\hline\\hline")
	for _, row in data.iterrows():
		print(f"{int(row['V'])} & {int(row['E'])} & {row['time']:.5f} & {int(row['mvc'])} \\\\")
		print("\\hline")
	print("\end{tabular}")	

def mvc_results(greedy_runs, exhaustive_runs):
	plt.plot(greedy_runs['V'], greedy_runs['mvc'], label='greedy')
	plt.plot(exhaustive_runs['V'], exhaustive_runs['mvc'], label='exhaustive')

	plt.xlabel('Number of Vertexes')
	plt.ylabel('Minimum Vertex Cover')
	plt.title('Greedy vs Exhaustive Vertex Cover Length')
	plt.legend()
	plt.show()

def greedy_goal(x, a, b, c):
	return a * np.exp(b * x) + c

def g_fit(runs, func, plot=True):
	curve, _ = curve_fit(func, runs['V'], runs['time']) 
	a, b, c = curve
	print(f"t = {a:.5f} * e^({b:.5f}) * V) + {c:.5f}")
	
	limits = range(0, 25)
	if plot:
		plt.plot(runs['V'], runs['time'], 'o', label='runs')
		plt.plot(limits, [greedy_goal(x, a, b, c) for x in limits], label='fit')
		plt.xlabel("Number of Vertexes")
		plt.ylabel("Execution time")
		plt.title("Exhaustive Fit")
		plt.legend()
		plt.show()
	print(greedy_goal(100, a, b, c) / 3600)
def absolute_error(actual, experimental):
	return ((experimental - actual) / actual)

def aprox_error(exh, grd):	
	df = pd.merge(exh, grd, how='inner', on='V')[['V', 'mvc_x', 'mvc_y']]
	
	df['error'] = df.apply(lambda x: absolute_error(x.mvc_y, x.mvc_x) , axis=1)
	print("\\begin{tabular}{|c c c c|}")
	print("\\hline")
	print(" V & exhaustive & greedy & absolute error\\\\ [0.5ex] ")
	print("\\hline\\hline")
	for _, row in df.iterrows():
		print(f"{int(row['V'])} & {int(row['mvc_y'])} & {int(row['mvc_x'])} & {row['error']:.2f} \\\\")
		print("\\hline")
	print("\end{tabular}")
	print(df['error'].mean() * 100)

df = pd.DataFrame(load_runs("./runs"))
df['mvc'] = df['solution'].apply(lambda r: len(r))
greedy_runs = df.loc[df['solver'] == 'g'].sort_values(by='V')
exhaustive_runs = df.loc[df['solver'] == 'e'].sort_values(by='V')
random_runs = df.loc[df['solver'] == 'r'].sort_values(by="V")

#greedy_vs_exhaustive_time_linear(greedy_runs, exhaustive_runs, random_runs)
#print(data_to_tex_table(greedy_runs.drop(['seed', 'solver', 'solution'], axis=1)))
#print(data_to_tex_table(random_runs.drop(['seed', 'solver', 'solution'], axis=1)))
#mvc_results(greedy_runs, exhaustive_runs)

#g_fit(exhaustive_runs, greedy_goal)
#g_fit(random_runs, greedy_goal)

aprox_error(random_runs, exhaustive_runs)
