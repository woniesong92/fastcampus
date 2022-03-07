#!/usr/bin/python
# -*- coding: utf-8 -*-

# CH. 주식 정보 모으기

import pandas as pd
import requests

# Scope
# 1. 사용자의 관심 종목을 추가 할 수 있어야 함 (현재 가격, PER, EPS, 고가, 저가, 등락)
# 2. 실시간 인기 종목들을 알 수 있어야 함
# 3. 종목의 시세 변동을 알 수 있어야 함

class StockAPIClient:
  # https://finance.naver.com/
  def get_stock_summary(self, itemcode):
    r = requests.get(f'https://api.finance.naver.com/service/itemSummary.naver?itemcode={itemcode}')
    return r.json()

  # https://m.stock.naver.com/myStock/-2
  def get_trending_stocks(self):
    raw_resp = requests.get(f'https://m.stock.naver.com/api/mystock/group/-2')
    return raw_resp.json()['stocks']

def __main__():
  api = StockAPIClient()
  trending_stocks = api.get_trending_stocks()
  trending_stocks_df = pd.DataFrame(trending_stocks)
  trending_stocks_df.to_html("tmp.html")  

__main__()
