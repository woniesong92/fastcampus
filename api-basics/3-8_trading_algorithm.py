#!/usr/bin/python
# -*- coding: utf-8 -*-

# CH. 크립토 트레이딩 알고리즘

# Section. 무빙 에브리지 계산

from lib.coin_bot import CoinBot
import pandas as pd     # needs pip install
import numpy as np
import matplotlib.pyplot as plt   # needs pip install

# Section. 일정 가격 초과면 팔고 이하면 사기
def buy_above_and_sell_below(client, symbol, price):
  ticker_info = client.get_ticker(symbol=symbol)
  last_price = round(float(ticker_info['lastPrice']), 2)
  if last_price > price:
    client.order_limit_sell(
      symbol=symbol,
      quantity=1.0,
      price=str(last_price)
    )
  else:
    client.order_limit_buy(
      symbol=symbol,
      quantity=1.0,
      price=str(last_price)
    )

# Section. SMA (5-day SMA 를 Signal 로 쓰기)
# Close < 5d-SMA: Buy
# Close >= 5d-SMA: Sell

def get_ohlc_df(client, symbol='BNBUSDT', starttime='2 week ago UTC', interval='1h'):
  bars = client.get_historical_klines(symbol, interval, starttime)

  # Columns: "date" "open" "high" "low" "close"
  for line in bars:
    del line[5:]

  df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])
  df.set_index('date', inplace=True)
  df.index = pd.to_datetime(df.index, unit='ms')
  return df.astype(float)

def trade_based_on_5_sma(client):
  ohlc_df = get_ohlc_df(client)
  ohlc_df['5_sma'] = ohlc_df['close'].rolling(5).mean()

  ohlc_df['position'] = np.where(ohlc_df['5_sma'] < ohlc_df['close'], 1, -1)
  ohlc_df['position'] = np.where(ohlc_df['5_sma'].isnull(), 0, ohlc_df['position'])

  ohlc_df['buy'] = np.where(ohlc_df['position'] == 1, ohlc_df['close'], np.NaN)
  ohlc_df['sell'] = np.where(ohlc_df['position'] == 1, ohlc_df['close'], np.NaN)
  
  print(ohlc_df)

def trade_when_crossover(client):
  ohlc_df = get_ohlc_df(client)
  ohlc_df['5_sma'] = ohlc_df['close'].rolling(5).mean()
  ohlc_df['15_sma'] = ohlc_df['close'].rolling(15).mean()

  ohlc_df['signal'] = np.where(ohlc_df['5_sma'] > ohlc_df['15_sma'], 1, 0)
  ohlc_df['position'] = ohlc_df['signal'].diff()

  ohlc_df['buy'] = np.where(ohlc_df['position'] == 1, ohlc_df['close'], np.NaN)
  ohlc_df['sell'] = np.where(ohlc_df['position'] == -1, ohlc_df['close'], np.NaN)

  ohlc_df['buy_cross'] = np.where(ohlc_df['position'] == 1, ohlc_df['5_sma'], np.NaN)
  ohlc_df['sell_cross'] = np.where(ohlc_df['position'] == -1, ohlc_df['5_sma'], np.NaN)

  return ohlc_df

def plot_graph_5_sma(df):
  df=df.astype(float)
  df[['close', '5_sma']].plot()
  plt.xlabel('Date')
  plt.ylabel('Close price')
  plt.show()

def plot_graph_crossover_sma(df):
  df=df.astype(float)
  df[['5_sma', '15_sma']].plot()

  # plt.scatter(df.index,df['Buy'], color='blue',label='Buy',  marker='^', alpha = 1)
  # plt.scatter(df.index,df['Sell'], color='red',label='Sell',  marker='v', alpha = 1)

  plt.scatter(df.index,df['buy_cross'], color='blue',label='Buy',  marker='^', alpha = 1)
  plt.scatter(df.index,df['sell_cross'], color='red',label='Sell',  marker='v', alpha = 1)

  plt.xlabel('Date')
  plt.ylabel('Moving Average')
  plt.show()

def main():
  

  coin_bot = CoinBot()
  client = coin_bot.client

  buy_above_and_sell_below(client, 'BNBUSDT', 1)

  # df = trade_when_crossover(client)
  # plot_graph_crossover_sma(df)

if __name__ == "__main__":
  main()
