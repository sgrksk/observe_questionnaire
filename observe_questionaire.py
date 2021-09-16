import pandas as pd
import csv
import pprint
import logging
import warnings
import MeCab
from janome.tokenizer import Tokenizer
from asari.api import Sonar
import oseti

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
# logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')
warnings.simplefilter('ignore')

def main():
    logging.info('########## input ##########')
    df = get_date()
    logging.info(df)
    
    logging.debug('########## mecab ##########')
    do_mecab(df)
    
    logging.debug('########## janome ##########')
    do_janome(df)
    
    logging.debug('########## asari ##########')
    do_asari(df)
    
    logging.debug('########## oseti ##########')
    do_oseti(df)

    logging.info('########## result ##########')
    logging.info(df)


def get_date():
    """
    アンケートデータ作成
    """
    ans1 = 'GitHub Actions はとっても便利です。'
    ans2 = 'Eureka Box は役立ってます'
    ans3 = 'GitHub Actions は使いやすくない。'
    ans4 = 'もっとわかりやすく説明してください。'
    ans5 = 'あなたよりも彼の方が好きです。'
    ans6 = '晩御飯にカレーを食べました。'

    text_list = [ans1, ans2, ans3, ans4, ans5, ans6]
    expected_list = ['positive', 'positive', 'negative', 'negative', 'negative', 'neutral']

    df = pd.DataFrame(list(zip(text_list, expected_list)), columns=['Text', 'Expected'])    
    return df

    
def get_dict():
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
    return np_dic


def do_mecab(df):
    mecab = MeCab.Tagger('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')
    mecab.parse('')
    np_dic = get_dict()

    judge = []
    for row in df.itertuples():
        logging.debug('text : ' + row.Text)

        nodes = mecab.parseToNode(row.Text)

        res = {"p":0, "n":0, "e":0}
        while nodes:
            logging.debug(nodes.surface)
            logging.debug(nodes.feature)
            if nodes.surface in np_dic:
                logging.debug('match  → ' + nodes.surface)
                r = np_dic[nodes.surface]
                if r in res:
                    res[r] += 1
            nodes = nodes.next

        logging.debug(res)
        judge.append(res)
        cnt = res["p"] + res["n"] + res["e"]
        if cnt:
            logging.debug("Positive" + str(res["p"] / cnt))
            logging.debug("Negative" + str(res["n"] / cnt))
            logging.debug("Neutral" + str(res["e"] / cnt))
        logging.debug('\n')
    
    df['mecab'] = judge


def do_janome(df):
    tok = Tokenizer()
    np_dic = get_dict()

    judge = []
    for row in df.itertuples():
        logging.debug('text : ' + row.Text)

        res = {"p":0, "n":0, "e":0}
        for t in tok.tokenize(row.Text):
            logging.debug(t)
            bf = t.base_form
            if bf in np_dic:
                logging.debug('match  → ' + bf)
                r = np_dic[bf]
                if r in res:
                    res[r] += 1
                
        logging.debug(res)
        judge.append(res)
        cnt = res["p"] + res["n"] + res["e"]
        if cnt:    
            logging.debug("Positive" + str(res["p"] / cnt))
            logging.debug("Negative" + str(res["n"] / cnt))
            logging.debug("Neutral" + str(res["e"] / cnt))
        logging.debug('\n')
    df['janome'] = judge


def do_asari(df):
    """
    https://jupyterbook.hnishi.com/language-models/easy_try_sentiment_analysis.html#asari
    https://teratail.com/questions/316611
    """
    sonar = Sonar()
    
    judge = []
    for row in df.itertuples():
        logging.debug('text : ' + row.Text)
        res = sonar.ping(row.Text)
        judge.append(res['top_class'])
        #pprint.pprint(res)
        logging.debug(res['top_class'])
        logging.debug("Positive" + str(res['classes'][1]['confidence']))
        logging.debug("Negative" + str(res['classes'][0]['confidence']))
        logging.debug('\n')
    df['asari'] = judge


def do_oseti(df):
    """
    janome で指定したのと同じ辞書を使ってるので結果も同じ。
    !pip install mecab-python3==0.996.5
    https://qiita.com/m__k/items/50b018c60f952c28869e
    """
    analyzer = oseti.Analyzer()

    judge = []
    for row in df.itertuples():
        logging.debug('text : ' + row.Text)
        res_count = analyzer.count_polarity(row.Text)
        judge.append(res_count)
        logging.debug(res_count)
        res_detail = analyzer.analyze_detail(row.Text)
        logging.debug(res_detail)
        logging.debug('\n')
    df['oseti'] = judge
    

if __name__ == '__main__':
    main()