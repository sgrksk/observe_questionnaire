import pandas as pd
import csv
from janome.tokenizer import Tokenizer

"""
アンケートデータ作成
"""
ans1 = 'DevOps CI はとっても便利です。'
ans2 = 'DevOps CI は使いやすくない。'
ans3 = 'DevOps CI よりも Jenkins の方が便利です。'
ans4 = '過去のログ同士を比較できる機能がほしいです。'
ans5 = '実行時間をもっと短くして欲しい。'

user_list = ['user1', 'user2', 'user3', 'user4','user5']
text_list = [ans1, ans2, ans3, ans4, ans5]

df = pd.DataFrame(list(zip(user_list, text_list)), columns=['User', 'Text'])
print(df)

"""
日本語評価極性辞書ダウンロード
"""
# curl http://www.cl.ecei.tohoku.ac.jp/resources/sent_lex/pn.csv.m3.120408.trim > pn.csv

np_dic = {}
fp = open("pn.csv", "rt", encoding="utf-8")
reader = csv.reader(fp, delimiter='\t')
for i, row in enumerate(reader):
  name = row[0]
  result = row[1]
  np_dic[name] = result


"""

"""
tok = Tokenizer()

for row in df.itertuples():
    print(row.User + ' : ' + row.Text)

    res = {"p":0, "n":0, "e":0}
    for t in tok.tokenize(row.Text):
        #print(t)
        bf = t.base_form
        if bf in np_dic:
            print('  → ' + bf)
            r = np_dic[bf]
            if r in res:
                res[r] += 1
                
    print(res)
    cnt = res["p"] + res["n"] + res["e"]
    if cnt:    
        print("Positive", res["p"] / cnt)
        print("Negative", res["n"] / cnt)
        print("Neutral" , res["e"] / cnt)
    print('\n')