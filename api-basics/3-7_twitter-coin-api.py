#!/usr/bin/python
# -*- coding: utf-8 -*-

# CH. 일론 머스크의 트윗이 올라올때 코인 사기

import requests

from lib.coin_bot import CoinBot

class TwitterClient:
  def __init__(self):
    # Bearer Token 설정
    bearer_token = ''
    self.headers = {
      'Authorization': f'Bearer {bearer_token}'
    }

  def get_user(self, username):
    url = f'https://api.twitter.com/2/users/by/username/{username}'
    raw_resp = requests.get(url, headers=self.headers)
    return raw_resp.json()

  def get_tweets_by_user_id(self, user_id):
    url = f'https://api.twitter.com/2/users/{user_id}/tweets'
    raw_resp = requests.get(url,
      headers=self.headers,
      params={
        'max_results': 20,
      }
    )
    return raw_resp.json()
  
def is_bitcoin_in_tweet(tweet_info):
  text = tweet_info['text']
  return "bitcoin" in text.lower()

def buy_bitcoin_if_elon_says_so():
  twitterClient = TwitterClient()  
  bot = CoinBot()
  
  tweets_by_elon = twitterClient.get_tweets_by_user_id(44196397)
  for tweet in tweets_by_elon:
    is_bitcoin_included = is_bitcoin_in_tweet(tweet)
    if (is_bitcoin_included):
      order = bot.buy_coin_at_discount('BTCUSDT', 1)
      print("주문 완료!", order)
