# -*- coding: utf-8 -*-
'''
Tweet JSONを読み込み本文テキストに出現する単語を集計する
'''

import sys
import json
import codecs
import spacy
import re
from collections import defaultdict
from datetime import datetime, timedelta, timezone

# GiNZAの準備
nlp = spacy.load("ja_ginza")
# タイムゾーンの定義
JST = timezone(timedelta(hours=+9), 'JST')
# カウンターの準備
counter = defaultdict(lambda: defaultdict(int))

# 1. 標準入力でJSONL形式のツイートデータを読み込む
sys.stdin = codecs.getreader(sys.stdin.encoding)(sys.stdin.detach(), errors='ignore')
for tweet in sys.stdin:
    # JSONのパース
    try:
        obj = json.loads(tweet)
    except:
        continue
    # 2. リツイートの場合は処理をせず，次のツイートデータに処理を移す
    if obj.get('retweeted_status', None) is not None:
        continue
    # 3. リプライの場合は処理をせず，次のツイートデータに処理を移す
    if obj.get('in_reply_to_user_id', None) is not None:
        continue
    # 4. ツイートデータから本文を取り出し，リプライやURLなどの不要な部分を削除する
    # ツイート本文の代入
    text = obj.get('full_text') or obj.get('text')
    # ツイート本文から不要な部分を削除
    text = re.sub('^RT @[\w_]+:', '', text)
    text = re.sub('^@[\w_]+', '', text)
    text = re.sub('https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', text)
    text = re.sub('\s+', ' ', text)
    # 5. ツイートデータから投稿日を取り出し，年月の情報に変換する
    # Twitterの日付形式をPythonの日付形式に変換
    created_at = datetime.strptime(obj['created_at'], '%a %b %d %H:%M:%S %z %Y')
    # Pythonの日付形式をJSTの年月（YYYY-MM）に変換
    date = created_at.astimezone(JST).strftime("%Y-%m")
    # 6. (4)の本文から名詞句を抽出し，キーワードリストを生成する
    for np in nlp(text).noun_chunks:
        # 7. (5)と(6)の情報をもとに，キーワードの月別出現数をカウントアップする
        counter[date][np.text] += 1

# 8. (7)のカウント情報をもとに，月別に上位のキーワードを指定件数だけ出力する
for date in sorted(counter):
    # 年月ごとに出現頻度上位100件を取り出してループ
    for item in sorted(counter[date].items(), key=lambda x: x[1], reverse=True)[:100]:
        print(f'{date}\t{item[0]}\t{item[1]}')
