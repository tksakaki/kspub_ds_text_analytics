# -*- coding: utf-8 -*-
'''
Twitter Search APIのサンプル
'''

import os
import sys
from requests_oauthlib import OAuth1Session
import json
from dotenv import load_dotenv

# .env ファイルをロードして環境変数へ反映
load_dotenv()

# 認証情報のチェック
if os.getenv('CONSUMER_KEY') is None or os.getenv('CONSUMER_SECRET') is None or os.getenv('ACCESS_TOKEN') is None or os.getenv('ACCESS_TOKEN_SECRET') is None:
	sys.exit('.envのロードに失敗し，認証情報が取得できませんでした')

# OAuthセッションの取得（Twitter APIへのアクセス権の取得）
twitter = OAuth1Session(os.getenv('CONSUMER_KEY'),
	client_secret=os.getenv('CONSUMER_SECRET'),
	resource_owner_key=os.getenv('ACCESS_TOKEN'),
	resource_owner_secret=os.getenv('ACCESS_TOKEN_SECRET'))

# APIの利用
response = twitter.get('https://api.twitter.com/1.1/search/tweets.json', params = { "q" : "外出", "result_type" : "result_type", "count" : 100, "tweet_mode" : "extended" })

# 結果の表示
for status in response.json()['statuses']:
	# idとJSONをタブ区切りで表示
	print('\t'.join([str(status['id']), json.dumps(status)]))
