import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("backtestResult.csv")

fig = make_subplots(rows=3, cols=1, shared_xaxes=True)

fig.add_trace(go.Scatter(x=df.index,y=df.trade,name='Trade',mode='lines+markers',connectgaps=True, line=dict(color='firebrick', width=1.5, dash='dot')),row=1,col=1)
fig.add_trace(go.Scatter(x=df.index,y=df.enter,name='Enter price',mode='lines',connectgaps=True, line=dict(color='orange', width=1.5)),row=1,col=1)
fig.add_trace(go.Scatter(x=df.index,y=df.price,name='Price',mode='lines',connectgaps=True, line=dict(color='grey', width=2)),row=1,col=1)
fig.add_trace(go.Scatter(x=df.index,y=df.asset,name='Asset',mode='lines',connectgaps=True, line=dict(color='purple', width=2)),row=2,col=1)
fig.add_trace(go.Scatter(x=df.index,y=df.currency,name='Currency',mode='lines',connectgaps=True, line=dict(color='green', width=2)),row=3,col=1)
fig.add_trace(go.Scatter(x=df.index,y=df.equity,name='Equity',mode='lines',connectgaps=True, line=dict(color='grey', width=2)),row=3,col=1)
fig.add_trace(go.Scatter(x=df.index,y=df.budgetextra,name='Budget Extra',mode='lines',connectgaps=True, line=dict(color='darkgreen', width=1.5)),row=3,col=1)

fig.update_traces(hovertemplate='%{y}')
fig.update_layout(title_text="Backtest", hovermode='x unified')

fig.write_html("plottedResults.html")