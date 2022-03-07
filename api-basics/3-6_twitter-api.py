#!/usr/bin/python
# -*- coding: utf-8 -*-

# CH. Twitter API 사용해보기

import requests

# Bearer Token 설정
bearer_token = ''
search_url = "https://api.twitter.com/2/tweets/search/recent"

COIN_NAMES = {
    'bitcoin',
    'ether',
    'litecoin',
    'ltc',
}

class TwitterClient:
    def __init__(self):
        self.headers = {
            'Authorization': f'Bearer {bearer_token}'
        }

    def get_user(self, username):
        raw_resp = requests.get(f"https://api.twitter.com/2/users/by/username/{username}", headers=self.headers)
        return raw_resp.json()

    def get_tweets_by_user(self, user_id):
        params = {
            'max_results': 20,
        }
        url = f'https://api.twitter.com/2/users/{user_id}/tweets'
        raw_resp = requests.get(url, params=params, headers=self.headers)
        resp = raw_resp.json()
        return resp['data']

    def find_coins_from_tweet(self, tweet_text):
        words = tweet_text.split()
        mentioned_coins = []
        for word in words:
            if word.lowercase() in COIN_NAMES:
                mentioned_coins.append(word)
        return mentioned_coins
