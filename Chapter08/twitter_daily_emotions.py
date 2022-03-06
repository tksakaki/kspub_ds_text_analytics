# -*- coding: utf-8 -*-
'''
Tweet JSONを読み込み本文テキストの感情を集計する
'''

import sys
import json
import codecs
from mlask import MLAsk
import re
from collections import defaultdict
from datetime import datetime, timedelta, timezone

# pymlaskの準備
emotion_analyzer = MLAsk()
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
    # Pythonの日付形式をJSTの年月日（YYYY-MM-DD）に変換
    date = created_at.astimezone(JST).strftime("%Y-%m-%d")
    # 6. (4)の本文をpymlaskに与え，感情成分を生成する
    emotion = emotion_analyzer.analyze(text)
    if emotion['emotion'] is not None:
        # 7. (5)と(6)の情報をもとに，各感情の日別出現数をカウントアップする
        for k, v in emotion['emotion'].items():
            counter[date][k] += 1
    else:
        # ツイート本文に感情を含まない場合はnoneをカウントアップする
        counter[date]['none'] += 1

# 8. (7)のカウント情報をもとに，日別の感情成分を出力する
for date in sorted(counter):
    # 感情成分を頻度順に出力
    for item in sorted(counter[date].items(), key=lambda x: x[1], reverse=True):
        print(f'{date}\t{item[0]}\t{item[1]}')
