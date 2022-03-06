# -*- coding: utf-8 -*-
'''
Twitter Streaming APIのサンプル
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

# 4. OAuthセッションを利用し，Streaming APIにアクセスする
response = twitter.get('https://stream.twitter.com/1.1/statuses/sample.json', params = { "lang" : "ja"}, stream=True)

# 5. 取得した結果を，idとJSONテキストのタブ区切りで出力する
for line in response.iter_lines():
    # JSONのパース
    status = json.loads(line.decode('utf-8'))
    # ツイート以外のデータの場合は処理しない
    if status.get('id', None) is None:
        continue
    # idとJSONをタブ区切りで表示
    print('\t'.join([str(status['id']), json.dumps(status)]))
