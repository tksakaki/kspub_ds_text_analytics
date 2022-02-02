# -*- coding: utf-8 -*-
'''
2ちゃんねるデータ（open.ceek.jp）を読み込みスレッドタイトルに出現する単語を集計する（出現割合の条件付き）
'''

import sys
import codecs
import spacy
from collections import defaultdict
from datetime import datetime, timedelta, timezone

nlp = spacy.load("ja_ginza")
total = defaultdict(int)
counter = defaultdict(lambda: defaultdict(int))
JST = timezone(timedelta(hours=+9), 'JST')

# 標準入力からのデータ入力
sys.stdin = codecs.getreader(sys.stdin.encoding)(sys.stdin.detach(), errors='ignore')
for line in sys.stdin:
	# データのパース
	obj = line.split("\t")
	# スレッドタイトルの代入
	text = obj[2]
	# UNIX時間をPythonの日付形式に変換（タイムゾーンはJSTを指定）
	created_at = datetime.fromtimestamp(int(obj[1]), JST)
	# Pythonの日付形式を年月（YYYY-MM）に変換
	date = created_at.strftime("%Y-%m")
	# スレッドタイトルの名詞句を抽出して集計する
	for np in nlp(text).noun_chunks:
		total[np.text] += 1
		counter[date][np.text] += 1

for date in counter:
	# 年月ごとに出現割合が0.5以上かつ出現頻度上位100件を取り出してループ
	for item in sorted(filter(lambda x: x[1] / total[x[0]] > 0.5, counter[date].items()), key=lambda x: (x[1], x[1] / total[x[0]]), reverse=True)[:100]:
		print(f'{date}\t{item[0]}\t{item[1]}\t{item[1]/total[item[0]]}')
