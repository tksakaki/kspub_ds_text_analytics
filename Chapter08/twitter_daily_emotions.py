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

emotion_analyzer = MLAsk()
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
	# Pythonの日付形式をJSTの年月（YYYY-MM-DD）に変換
	date = created_at.astimezone(JST).strftime("%Y-%m-%d")
	# ツイート本文の感情を分析して集計する
	emotion = emotion_analyzer.analyze(text)
	if emotion['emotion'] is not None:
		for k, v in emotion['emotion'].items():
			counter[date][k] += 1
	else:
		# ツイート本文に感情を含まない場合はnoneをカウントアップする
		counter[date]['none'] += 1

for date in counter:
	# 日ごとに感情分布を頻度順に出力
	for item in sorted(counter[date].items(), key=lambda x: x[1], reverse=True):
		print(f'{date}\t{item[0]}\t{item[1]}')
