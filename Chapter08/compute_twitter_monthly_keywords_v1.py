# -*- coding: utf-8 -*-
'''
集計中間ファイルを読み込み出現する単語を集計する
'''

import sys
import codecs
from collections import defaultdict

counter = defaultdict(lambda: defaultdict(int))

# 標準入力からのデータ入力
sys.stdin = codecs.getreader(sys.stdin.encoding)(sys.stdin.detach(), errors='ignore')
for line in sys.stdin:
    # 中間データのパース
    obj = line.split("\t")
    # 出現回数をカウントアップ
    counter[obj[0]][obj[1]] += int(obj[2])

for date in sorted(counter):
    # 年月ごとに出現頻度上位100件を取り出してループ
    for item in sorted(counter[date].items(), key=lambda x: x[1], reverse=True)[:100]:
        print(f'{date}\t{item[0]}\t{item[1]}')
