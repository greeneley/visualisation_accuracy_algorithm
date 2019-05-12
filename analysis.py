import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns
import plotly.graph_objs as go
import plotly.plotly as py
import plotly 
plotly.tools.set_credentials_file(username='thanhdinh', api_key='fNARQhT2RXa4ZZspntSk')
data = pd.read_csv('./accuracy_full.csv')

data_algo = data.drop(columns='Unnamed: 0').copy()

x = np.random.randn(500)
data = [go.Histogram(x=x,
                     histnorm='probability')]

py.iplot(data, filename='normalized histogram')