
#coding: UTF-8

import twitter

#取得したキーとアクセストークンを設定する
auth = twitter.OAuth(consumer_key="y3XHgOEoJstHUMIPOn9wsUUES",
                     consumer_secret="4HfZOv9li6RdG5iktWpxVzkcyKuoiAieZEggcNFXp4vLbfYaDj",
                     token="819476346-KESWMspNfBLBPrGQ5gKku0s2Ulua285s41n5LLSo",
                     token_secret="VxnuKpx2zX0MVdoDWjokz5R0X4xYw7J0AoiOKFKbN1wqE")

t = twitter.Twitter(auth=auth)

#twitterへメッセージを投稿する
t.statuses.update(status="pythonからツイート")
