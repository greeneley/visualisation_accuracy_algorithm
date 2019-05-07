import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

data = pd.read_csv('./accuracy_full.csv')

data_history= data.iloc[:, 2:].copy()

data_history.hist(bins=100, color='steelblue', edgecolor='black', linewidth=1.0, xlabelsize=8, ylabelsize=8, grid=False)
plt.tight_layout()