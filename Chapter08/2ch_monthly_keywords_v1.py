# -*- coding: utf-8 -*-
'''
2ちゃんねるデータ（open.ceek.jp）を読み込みスレッドタイトルに出現する単語を集計する
'''

import sys
import codecs
import spacy
from collections import defaultdict
from datetime import datetime, timedelta, timezone

# GiNZAの準備
nlp = spacy.load("ja_ginza")
# タイムゾーンの定義
JST = timezone(timedelta(hours=+9), 'JST')
# カウンターの準備
counter = defaultdict(lambda: defaultdict(int))

# 1. 標準入力でデータを読み込む
sys.stdin = codecs.getreader(sys.stdin.encoding)(sys.stdin.detach(), errors='ignore')
for line in sys.stdin:
    # 2. データからスレッドタイトルを取り出す
    obj = line.split("\t")
    text = obj[2]
    # 3. データから投稿日時を取り出し，年月の情報に変換する
    # UNIX時間をPythonの日付形式に変換（タイムゾーンはJSTを指定）
    created_at = datetime.fromtimestamp(int(obj[1]), JST)
    # Pythonの日付形式を年月（YYYY-MM）に変換
    date = created_at.strftime("%Y-%m")
    # 4. (2)のスレッドタイトルから名詞句を抽出し，キーワードリストを生成する
    for np in nlp(text).noun_chunks:
        # 5. (3)と(4)の情報をもとに，キーワードの月別出現数をカウントアップする
        counter[date][np.text] += 1

# 6. (5)のカウント情報をもとに，月別に上位のキーワードを指定件数だけ出力する
for date in sorted(counter):
    # 年月ごとに出現頻度上位100件を取り出してループ
    for item in sorted(counter[date].items(), key=lambda x: x[1], reverse=True)[:100]:
        print(f'{date}\t{item[0]}\t{item[1]}')
