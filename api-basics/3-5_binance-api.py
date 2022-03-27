#!/usr/bin/python
# -*- coding: utf-8 -*-

# CH. 바이낸스 API 로 코인 구입/판매 해보기

from binance.client import Client

class CoinBot:
  # API_KEY 와 API_SECRET 설정
  API_KEY = ''
  API_SECRET = ''

  def __init__(self):
    self.client = Client(self.API_KEY, self.API_SECRET, testnet=True)

  def limit_buy_order(self, symbol='BTCUSDT'):
    avg_price_info = self.client.get_avg_price(symbol=symbol)
    avg_price = avg_price_info['price']
    return self.client.order_limit_buy(symbol=symbol, quantity=1, price=avg_price)

  def get_account_info(self):
    return self.client.get_account()

  def get_all_orders(self, symbol='BTCUSDT', limit=10):
    return self.client.get_all_orders(symbol=symbol, limit=limit)

  def cancel_all_orders(self):
    open_orders = self.client.get_open_orders()
    for order in open_orders:
      order_id = order['orderId']
      symbol = order['symbol']
      self.client.cancel_order(symbol=symbol, order_id=order_id)
