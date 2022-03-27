# 크립토 트레이딩 알고리즘

from coin_bot import CoinBot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 가격을 잘 보고 있다가, 어떤 코인이 X 가격이 되면 사라
# 2. 어떤 코인이 Y 가격이 되면 팔아라

bot = CoinBot()
client = bot.client

def buy_coin_at_price(client, symbol, target_price):
  # symbol = BNBUSDT
  ticker_info = client.get_ticker(symbol=symbol)
  last_price = ticker_info['lastPrice']
  last_price = round(float(last_price), 2)
  if last_price <= target_price:
    return client.order_market_buy(
      symbol=symbol,
      quantity=1.0,
    )
  return None

def sell_coin_at_price(client, symbol, target_price):
  # symbol = BNBUSDT
  ticker_info = client.get_ticker(symbol=symbol)
  last_price = ticker_info['lastPrice']
  last_price = round(float(last_price), 2)
  if last_price >= target_price:
    return client.order_market_sell(
      symbol=symbol,
      quantity=1.0,
    )
  return None

# prices = [20, 22, 24, 25, 23, 26, 28, 26, 29, 27, 26, 28, 26, 29, 27]

# 1. 이동평균선 (moving average) 보다 가격이 낮으면 사고
# 2. 이동평균선 보다 가격이 높으면 팔아라

def get_price_history(client):
  klines = client.get_historical_klines('BNBUSDT', '1h', '2 week ago UTC')
  for line in klines:
    del line[5:]

  df = pd.DataFrame(klines, columns=['date', 'open', 'high', 'low', 'close'])
  df.set_index('date', inplace=True)
  df.index = pd.to_datetime(df.index, unit='ms')
  
  return df.astype(float)

def trade_based_on_5_sma(client):
  df = get_price_history(client)

  # 이동 평균선을 구해줘
  df['5_sma'] = df['close'].rolling(5).mean()
  df['buy'] = np.where(df['5_sma'] > df['close'], 1, 0)
  df['sell'] = np.where(df['5_sma'] <= df['close'], 1, 0)

  return df

def trade_based_on_crossover(client):
  df = get_price_history(client)

  # 이동 평균선을 구해줘
  df['5_sma'] = df['close'].rolling(5).mean()
  df['15_sma'] = df['close'].rolling(15).mean()

  df['signal'] = np.where(df['5_sma'] > df['15_sma'], 1, 0)
  df['position'] = df['signal'].diff()

  df['buy_cross'] = np.where(df['position'] == 1, df['5_sma'], np.NaN)
  df['sell_cross'] = np.where(df['position'] == -1, df['5_sma'], np.NaN)
  
  return df

def plot_crossover_graph(client):
  df = trade_based_on_crossover(client)
  df[['5_sma', '15_sma']].plot()

  plt.scatter(df.index, df['buy_cross'], color='blue', label='Buy', marker='^', alpha=1)
  plt.scatter(df.index, df['sell_cross'], color='red', label='Sell', marker='v', alpha=1)
  
  plt.xlabel('Date')
  plt.ylabel('Price')
  plt.show()

plot_crossover_graph(client)