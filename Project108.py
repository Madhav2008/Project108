import csv
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("Project108.csv")

graph = ff.create_displot([df["Avg Rating"].tolist()], ["Amazon Mobile Rating"], show_hist = False)
graph.show()
