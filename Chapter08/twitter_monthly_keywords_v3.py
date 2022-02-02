# -*- coding: utf-8 -*-
'''
Tweet JSONを読み込み本文テキストに出現する単語を集計する（全件出力）
'''

import sys
import json
import codecs
import spacy
import re
from collections import defaultdict
from datetime import datetime, timedelta, timezone

nlp = spacy.load("ja_ginza")
counter = defaultdict(lambda: defaultdict(int))
JST = timezone(timedelta(hours=+9), 'JST')

# 標準入力からのデータ入力
sys.stdin = codecs.getreader(sys.stdin.encoding)(sys.stdin.detach(), errors='ignore')
for tweet in sys.stdin:
	# JSONのパース
	try:
		obj = json.loads(tweet)
	except:
		continue
	# 公式リツイートの場合は処理しない
	if obj.get('retweeted_status', None) is not None:
		continue
	# 公式リプライの場合は処理しない
	if obj.get('in_reply_to_user_id', None) is not None:
		continue
	# ツイート本文の代入
	text = obj.get('full_text') or obj.get('text')
	# ツイート本文から不要な部分を削除
	text = re.sub('^RT @[\w_]+:', '', text)
	text = re.sub('^@[\w_]+', '', text)
	text = re.sub('https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', text)
	text = re.sub('\s+', ' ', text)
	# Twitterの日付形式をPythonの日付形式に変換
	created_at = datetime.strptime(obj['created_at'], '%a %b %d %H:%M:%S %z %Y')
	# Pythonの日付形式をJSTの年月（YYYY-MM）に変換
	date = created_at.astimezone(JST).strftime("%Y-%m")
	# ツイート本文の名詞句を抽出して集計する
	for np in nlp(text).noun_chunks:
		counter[date][np.text] += 1

for date in counter:
	# 全件出力する
	for item in counter[date].items():
		print(f'{date}\t{item[0]}\t{item[1]}')
