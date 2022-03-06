# -*- coding: utf-8 -*-
'''
集計中間ファイルを読み込みワードクラウドを生成する（出現割合の条件付き）
'''

import sys
import codecs
import re
from collections import defaultdict
from wordcloud import WordCloud
import matplotlib.pyplot as plt

total = defaultdict(int)
counter = defaultdict(lambda: defaultdict(int))

# 標準入力からのデータ入力
sys.stdin = codecs.getreader(sys.stdin.encoding)(sys.stdin.detach(), errors='ignore')
for line in sys.stdin:
    # 中間データのパース
    obj = line.split("\t")
    # 単語の修正
    obj[1] = re.sub('^「', '', obj[1])
    obj[1] = re.sub('^【', '', obj[1])
    # 出現回数をカウントアップ
    total[obj[1]] += int(obj[2])
    counter[obj[0]][obj[1]] += int(obj[2])

for date in sorted(counter):
    # 年月ごとに出現割合が0.5以上の単語を取り出す
    frequencies = dict(filter(lambda x: x[1] / total[x[0]] > 0.5, counter[date].items()))
    # ワードクラウドの準備
    wordcloud = WordCloud(background_color='white', font_path='ipaexg.ttf', max_font_size=100).fit_words(frequencies)
    # ファイルを出力
    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(f'{date}.png')
