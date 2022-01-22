import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from flask import send_file

df_lbj = pd.read_pickle("/Users/jeanphilippepetit-frere/Python_projects/nba/nba_big_project/Lebron James")
df_embiid = pd.read_pickle("/Users/jeanphilippepetit-frere/Python_projects/nba/nba_big_project/Joel Embiid")
df_kd = pd.read_pickle("/Users/jeanphilippepetit-frere/Python_projects/nba/nba_big_project/Kevin Durant")
df_kawhi = pd.read_pickle("/Users/jeanphilippepetit-frere/Python_projects/nba/nba_big_project/Kawhi Leonard")
df_kyrie = pd.read_pickle("/Users/jeanphilippepetit-frere/Python_projects/nba/nba_big_project/Kyrie Irving")
df_jokic = pd.read_pickle("/Users/jeanphilippepetit-frere/Python_projects/nba/nba_big_project/Nikola Jokic")
df_giannis = pd.read_pickle("/Users/jeanphilippepetit-frere/Python_projects/nba/nba_big_project/Giannis Antetokounmpo")

lst = [df_lbj, df_kd, df_giannis, df_jokic, df_kyrie, df_embiid, df_kawhi]
athlete = ['Lebron James','Kevin Durant','Giannis Antetokounmpo','Nikola Jokic','Kyrie Irving'
,'Joel Embiid','Kawhi Leonard']

app = Flask(__name__)
@app.route('/')
def get_all_graph(stats):
    num = 0
    def get_graph(df,name):
        from plotly.subplots import make_subplots
        import plotly.graph_objects as go

        fig = make_subplots(rows=3, cols=2,subplot_titles=('Points',  'Assists', 'Rebounds', 'Steals', 'Blocks', 'Turnovers'))

        fig.add_trace(
            go.Histogram(x=df['points']),
            row=1, col=1
        )

        fig.add_trace(
            go.Histogram(x=df['assists']),
            row=1, col=2
        )
        fig.add_trace(
            go.Histogram(x=df['totReb']),
            row=2, col=1
        )

        fig.add_trace(
            go.Histogram(x=df['steals']),
            row=2, col=2
        )

        fig.add_trace(
            go.Histogram(x=df['blocks']),
            row=3, col=1
        )

        fig.add_trace(
            go.Histogram(x=df['turnovers']),
            row=3, col=2
        )
        fig.update_layout(height=800, width=1000, title_text="Distibution plots of "+name+" stats",title_x=0.5)
        fig.write_image("images/fig"+name[:3]+".jpeg")
        fig.show()
 
    for x in stats:
        get_graph(x,athlete[num])
        num+=1