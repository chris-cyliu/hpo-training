#!/bin/bash
# echo Please manually download folder "train" and file "labels.csv" from https://www.kaggle.com/careyai/inceptionv3-full-pretrained-model-instructions/data
# echo and put them into a folder named inceptionv3_dog
curl 'https://storage.googleapis.com/kaggle-competitions-data/kaggle-v2/7327/861871/upload/train.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1594741137&Signature=JPszopUt%2BPWgtcsifgKTgiwdGkYvM0M1sJXGvIx3%2BW%2ByHaUcv34hzi%2BuXDUl4VMSRhdpTEFRdVbknaYV5FN8h3MyQtvV1hdDJRPo7pdaR6XSqZEP4%2BGObJTEYMRv55U9tgaAmZb7qyliyphHOyS2rVAaf2J1JL595Pqkxt1XtXOy94Uy6I6bq95332msvB%2Fu9nZZ%2FnGznEW74liR6lDmQEE7XVqaMF15rBb2Ieo67L3%2F0CM5ayriApE1w1dwL0AuzD6SR%2Br00m7q%2FELuE2NzYyujhioCCh%2ByU97hYTKTYW6%2BhhElSyrDCO3nZcQ7wqhwWQK46EoABBw7CFYlFzuT3A%3D%3D&response-content-disposition=attachment%3B+filename%3Dtrain.zip' -H 'authority: storage.googleapis.com' -H 'upgrade-insecure-requests: 1' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36' -H 'sec-fetch-dest: document' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H 'sec-fetch-site: cross-site' -H 'sec-fetch-mode: navigate' -H 'sec-fetch-user: ?1' -H 'referer: https://www.kaggle.com/' -H 'accept-language: en-US,en;q=0.9,zh;q=0.8,zh-CN;q=0.7' --compressed -o train.zip
mkdir train && cd train
mv ../train.zip .
unzip train.zip
cd ..
curl 'https://storage.googleapis.com/kagglesdsdata/competitions/7327/861871/labels.csv?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1594741449&Signature=pTMnCjmUD4UkWYAjrzTBlt10uzDI2hNaF9sfakJU2%2FzF5STngtzcApNXcv1eLblXBNIRqpt%2B3agTmPsUnTFmlgsk%2F7%2FLUQIQ1cnHM49BU7L5iskhM11vPj4n6YwCsBYRhJjI8sJu1aN%2FOri1sNofxRrKvOksIdoYRefbNAtsvP4GFiMJfi%2BifzBTxLtjdk4s29U4LdZbfK9ObxqQwJ6L9C6%2FVUH8ADab5WpsWumjbXbP4ERtaD6f%2FxuYmpycaXhJZ3qGCIfGoINxXjwuaWeiD2IR5iUw4Z5XavtDDCwTqOcSZiJLvN20TLhIAOAFrvoC2Lz4juiFmdYE1sWwWSHpSQ%3D%3D&response-content-disposition=attachment%3B+filename%3Dlabels.csv' -H 'authority: storage.googleapis.com' -H 'upgrade-insecure-requests: 1' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36' -H 'sec-fetch-dest: document' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H 'sec-fetch-site: cross-site' -H 'sec-fetch-mode: navigate' -H 'sec-fetch-user: ?1' -H 'referer: https://www.kaggle.com/' -H 'accept-language: en-US,en;q=0.9,zh;q=0.8,zh-CN;q=0.7' --compressed -o labels.csv
mkdir inceptionv3_dog
mv train inceptionv3_dog/
mv labels.csv inceptionv3_dog