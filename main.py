import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import plotly.express as px
import plotly.graph_objects as go
start = dt.datetime(2020, 8, 8)
end = dt.datetime.now()
selected_stock = 'AMZN'
stocks = web.DataReader(selected_stock, 'yahoo', start, end)
stocks_close = pd.DataFrame(web.DataReader(
    selected_stock, 'yahoo', start, end)['Close'])
stocks2 = pd.DataFrame(web.DataReader(selected_stock, 'yahoo', start, end))
print(stocks2['Close'])
#stocks2['Close',selected_stock] = stocks2.rolling(5).mean()
df = web.DataReader(selected_stock, 'yahoo', start, end)
lows=df.Low.rolling(window=2, min_periods=1).mean()
highs = df.High.rolling(window=2, min_periods=1).mean()
mids = df.Close.rolling(window=2, min_periods=1).mean()
trace1 = {
    'x': df.index,
    'y': mids,
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'black'
    },
    'name': 'Moving Average of 30 periods'
}
trace2 = {
    'x': df.index,
    'y': highs,
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'blue'
    },
    'name': 'Moving Average of 30 periods'
}
trace3 = {
    'x': df.index,
    'y': lows,
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'red'
    },
    'name': 'Moving Average of 30 periods'
}

c_candlestick = go.Figure(data=[go.Candlestick(x=stocks.index,
                                               open=stocks[('Open')],
                                               high=stocks[('High')],
                                               low=stocks[('Low')],
                                               close=stocks[('Close')]),
                               trace1, trace2,trace3])

c_candlestick.update_xaxes(
    title_text='Date',
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label='1M', step='month', stepmode='backward'),
            dict(count=6, label='6M', step='month', stepmode='backward'),
            dict(count=1, label='YTD', step='year', stepmode='todate'),
            dict(count=1, label='1Y', step='year', stepmode='backward'),
            dict(step='all')])))

c_candlestick.update_layout(
    title={
        'text': 'AMAZON SHARE PRICE (2013-2020)',
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

c_candlestick.update_yaxes(title_text='AMZN Close Price', tickprefix='$')
c_candlestick.show()
