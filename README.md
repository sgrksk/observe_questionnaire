# アンケートの感情分析をやってみた

``` bash
$ python3 observe_questionaire.py 

    User                            Text
0  user1            GitHub Actions はとっても便利です。
1  user2             GitHub Actions は使いやすくない。
2  user3  GitHub Actions よりも Jenkins の方が便利です。
3  user4          過去のログ同士を比較できる機能がほしいです。
4  user5                実行時間をもっと短くして欲しい。

user1 : GitHub Actions はとっても便利です。
  → 便利
{'p': 1, 'n': 0, 'e': 0}
Positive 1.0
Negative 0.0
Neutral 0.0


user2 : GitHub Actions は使いやすくない。
{'p': 0, 'n': 0, 'e': 0}


user3 : GitHub Actions よりも Jenkins の方が便利です。
  → 便利
{'p': 1, 'n': 0, 'e': 0}
Positive 1.0
Negative 0.0
Neutral 0.0


user4 : 過去のログ同士を比較できる機能がほしいです。
  → 過去
  → 機能
{'p': 1, 'n': 1, 'e': 0}
Positive 0.5
Negative 0.5
Neutral 0.0


user5 : 実行時間をもっと短くして欲しい。
  → 実行
  → 時間
{'p': 0, 'n': 0, 'e': 2}
Positive 0.0
Negative 0.0
```

辞書をリッチにしないと精度が出ない？？？
- user1 : ○
- user2 : × (ネガティブな意見を評価できていない)
- user3 : × (「便利」をひろってポジティブに評価されている)
- user4 : ○ (要望なのでニュートラルな評価は妥当か？)
- user5 : × (不満からくる要望だがニュートラルと評価されている)
