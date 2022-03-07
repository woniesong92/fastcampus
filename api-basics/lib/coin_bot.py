from binance.client import Client

class CoinBot:
  # API_KEY 와 API_SECRET 설정
  API_KEY = ''
  API_SECRET = ''

  def __init__(self):
    self.client = Client(self.API_KEY, self.API_SECRET, testnet=True)

  def buy_coin_at_discount(self, symbol, quantity):
    # 1. 코인의 지금 가격을 불러와
    ticker_info = self.client.get_ticker(symbol=symbol)
    last_price = ticker_info['lastPrice']
    
    # 2. 코인의 지금 가격에서 10% 디스카운트 된 가격을 계산해
    discounted_price = round(float(last_price) * 0.9, 2)
    
    # 3. 그 가격에 주문을 넣어놔
    return self.client.order_limit_buy(
      symbol=symbol,
      quantity=quantity,
      price=str(discounted_price)
    )

  def sell_coin_at_premium(self, symbol, quantity):
    # 1. 코인의 지금 가격을 불러와
    ticker_info = self.client.get_ticker(symbol=symbol)
    last_price = ticker_info['lastPrice']
    
    # 2. 코인의 지금 가격에서 10% 프리미엄 된 가격을 계산해
    premium_price = round(float(last_price) * 1.1, 2)
    
    # 3. 그 가격에 주문을 넣어놔
    return self.client.order_limit_sell(
      symbol=symbol,
      quantity=quantity,
      price=str(premium_price)
    )

  def cancel_all_open_orders(self):
    open_orders = self.client.get_open_orders()
    for order in open_orders:
      result = self.client.cancel_order(
        symbol=order['symbol'],
        orderId=order['orderId']
      )
