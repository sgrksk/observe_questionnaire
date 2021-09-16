# アンケートの感情分析をやってみた

``` bash
$ python3 observe_questionaire.py 

[INFO] ########## input ##########
[INFO]                         Text  Expected
0  GitHub Actions はとっても便利です。  positive
1         Eureka Box は役立ってます  positive
2   GitHub Actions は使いやすくない。  negative
3         もっとわかりやすく説明してください。  negative
4            あなたよりも彼の方が好きです。  negative
5             晩御飯にカレーを食べました。   neutral
[INFO]
########## result ##########
[INFO]                         Text  Expected                     mecab                    janome     asari                             oseti
0  GitHub Actions はとっても便利です。  positive  {'p': 1, 'n': 0, 'e': 0}  {'p': 1, 'n': 0, 'e': 0}  positive  [{'positive': 1, 'negative': 0}]
1         Eureka Box は役立ってます  positive  {'p': 0, 'n': 0, 'e': 0}  {'p': 0, 'n': 0, 'e': 0}  positive  [{'positive': 1, 'negative': 0}]
2   GitHub Actions は使いやすくない。  negative  {'p': 0, 'n': 0, 'e': 0}  {'p': 0, 'n': 0, 'e': 0}  negative  [{'positive': 0, 'negative': 0}]
3         もっとわかりやすく説明してください。  negative  {'p': 0, 'n': 0, 'e': 1}  {'p': 0, 'n': 0, 'e': 1}  positive  [{'positive': 0, 'negative': 0}]
4            あなたよりも彼の方が好きです。  negative  {'p': 1, 'n': 0, 'e': 0}  {'p': 1, 'n': 0, 'e': 0}  positive  [{'positive': 1, 'negative': 0}]
5             晩御飯にカレーを食べました。   neutral  {'p': 0, 'n': 0, 'e': 0}  {'p': 0, 'n': 0, 'e': 0}  positive  [{'positive': 0, 'negative': 0}]
```

