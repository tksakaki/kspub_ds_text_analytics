# -*- coding: utf-8 -*-
'''
集計中間ファイルを読み込み出現する単語を集計する（出現割合の条件付き）
'''

import sys
import codecs
from collections import defaultdict

counter = defaultdict(lambda: defaultdict(int))
total = defaultdict(int)

# 標準入力からのデータ入力
sys.stdin = codecs.getreader(sys.stdin.encoding)(sys.stdin.detach(), errors='ignore')
for line in sys.stdin:
    # 中間データのパース
    obj = line.split("\t")
    # 出現回数をカウントアップ
    counter[obj[0]][obj[1]] += int(obj[2])
    total[obj[1]] += int(obj[2])

for date in sorted(counter):
    # 年月ごとに出現割合が0.5以上かつ出現頻度上位100件を取り出してループ
    for item in sorted(filter(lambda x: x[1] / total[x[0]] > 0.5, counter[date].items()), key=lambda x: (x[1], x[1] / total[x[0]]), reverse=True)[:100]:
        print(f'{date}\t{item[0]}\t{item[1]}\t{item[1]/total[item[0]]}')
