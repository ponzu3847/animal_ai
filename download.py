from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import time,os,sys

key="4e19e5f2fdca6dc11e76029dd37912f3"
secret="612363e6d27cb0fa"
wait_time=1

animalname=sys.argv[1]  # python download.py monkeyで実行した際のmonkey
savedir="./"+animalname

flickr=FlickrAPI(key,secret,format='parsed-json')
result=flickr.photos.search(
    text=animalname,    # 検索文字
    per_page=400,   # 400件の画像を取得する
    media='photos', 
    sort='relevance',    # 関連順にソートする
    safe_search=1,   # 有害コンテンツを表示しない
    extras='url_q, licence'
)

photos=result['photos']
#pprint(photos)

for i,photo in enumerate(photos['photo']):
    url_q=photo['url_q']
    filepath=savedir+'/'+photo['id']+'.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q,filepath)
    time.sleep(wait_time)
