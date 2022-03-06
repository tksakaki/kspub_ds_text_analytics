# -*- coding: utf-8 -*-
'''
Twitter Search APIのサンプル
'''

import os
import sys
from requests_oauthlib import OAuth1Session
import json
from dotenv import load_dotenv

# 1. .envファイルをロードして環境変数に反映する
load_dotenv()

# 2. 認証情報が環境変数に存在するかをチェックする
if os.getenv('CONSUMER_KEY') is None or os.getenv('CONSUMER_SECRET') is None or os.getenv('ACCESS_TOKEN') is None or os.getenv('ACCESS_TOKEN_SECRET') is None:
    sys.exit('.envのロードに失敗し，認証情報が取得できませんでした')

# 3. 認証情報をもとにOAuthセッションを取得する
twitter = OAuth1Session(os.getenv('CONSUMER_KEY'),
    client_secret=os.getenv('CONSUMER_SECRET'),
    resource_owner_key=os.getenv('ACCESS_TOKEN'),
    resource_owner_secret=os.getenv('ACCESS_TOKEN_SECRET'))

# 4. OAuthセッションを利用し，検索APIにアクセスする
response = twitter.get('https://api.twitter.com/1.1/search/tweets.json', params = { "q" : "外出", "result_type" : "result_type", "count" : 100, "tweet_mode" : "extended" })

# 5. 取得した結果を，idとJSONテキストのタブ区切りで出力する
for status in response.json()['statuses']:
    # idとJSONをタブ区切りで表示
    print('\t'.join([str(status['id']), json.dumps(status)]))
