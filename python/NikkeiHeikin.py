#coding: UTF-8
import twitter
import urllib.request
from bs4 import BeautifulSoup

#取得したキーとアクセストークンを設定する
auth = twitter.OAuth(consumer_key="",
                     consumer_secret="",
                     token="",
                     token_secret="")

t = twitter.Twitter(auth=auth)

#アクセスするURL
url = "http://www.nikkei.com/markets/kabu/"

#URLにアクセスするhtml
html = urllib.request.urlopen(url)

#htmlをbeautifulsoupで扱う
soup = BeautifulSoup(html, "html.parser")

#span要素をすべて摘出→全てのspan要素が配列に入ってかえされる
span = soup.find_all("span")

#print時のエラーとならないよう最初に宣言
nikkei_heikin = ""

#for文ですべてのspan要素の中からClass="mkc-stock.prices"となっているものを探す
for tag in span:
    #classの設定がされていない要素は、tag.get("class").pop(0)を行うことができないのでエラーとなる。よってtry
    try:
        #tagの中からclass="n"のnの文字列を摘出。複数classが設定されている場合があるので
        #get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する
        #<span class="hoge class"="foo"> → ["hoge", "foo"]
        string_ = tag.get("class").pop(0)

        #摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べる
        if string_ in "mkc-stock_prices":
            #mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶりだす
            nikkei_heikin = tag.string
            #摘出が完了したのでfor文を抜ける
            break

    except:
        #パス→何も処理を行わない
        pass
status = ["日経平均株価は",nikkei_heikin,"円だよ"]
stat = "".join(status)
t.statuses.update(status=stat)
