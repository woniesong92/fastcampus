#!/usr/bin/python
# -*- coding: utf-8 -*-

# CH. 코인 정보 모으기

from requests import Session

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '', # API Key 설정
}

def get_coin_info(symbol):
  session = Session()
  session.headers.update(headers)
  url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  parameters = {'symbol': symbol}
  resp = session.get(url, params=parameters)
  return resp.json()

def get_global_markets_info():
  session = Session()
  session.headers.update(headers)
  url = 'https://sandbox-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
  parameters = {}
  resp = session.get(url, params=parameters)
  return resp.json()

def get_trending_movers():
  session = Session()
  session.headers.update(headers)
  url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/trending/gainers-losers'
  parameters = {}
  resp = session.get(url, params=parameters)
  return resp.json()

class CoinDataAPIClient():
  def __init__(self):
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '', # API Key 설정
    }
    self.session = Session()
    self.session.headers.update(headers)
  
  def get_coin_info(self, symbol):
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {'symbol': symbol}
    resp = self.session.get(url, params=parameters)
    return resp.json()

  def get_trending_movers(self):
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/trending/gainers-losers'
    resp = self.session.get(url)
    return resp.json()

def __main__():
  api_client = CoinDataAPIClient()
  coin_info = api_client.get_trending_movers()
  print(coin_info)

