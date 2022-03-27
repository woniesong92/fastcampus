import requests

class StockAPIClient:
  # https://finance.naver.com/
  def get_stock_summary(self, itemcode):
    r = requests.get(f'https://api.finance.naver.com/service/itemSummary.naver?itemcode={itemcode}')
    return r.json()

  # https://m.stock.naver.com/myStock/-2
  def get_trending_stocks(self):
    raw_resp = requests.get(f'https://m.stock.naver.com/api/mystock/group/-2')
    return raw_resp.json()['stocks']

