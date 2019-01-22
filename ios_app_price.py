#coding: UTF-8

import requests
import os
import lxml.html

# -----
def text_output(xpath):
  print(xpath)
  #list_text = root.findall(xpath)
  list_text = root.xpath(xpath)
  print(list_text)
#  version_str = list_text[0].text
#  path_w = latest_path
#  with open(path_w, mode = 'a') as f:
#    f.write(version_str)
#    f.write('\n')

def file_manipulate():
  # 前々回のファイルがあれば消す
  # 前回のファイルがあればold.logに変更する
  ####関数化する
  ####比較して変更があれば何かしらの方法で通知
  if os.path.exists(old_path):
    os.remove(old_path)
    print('old file removed')
  else:
    print('no old file')
  if os.path.exists(previous_path):
    os.rename(previous_path,old_path)
    print('previous file renamed')
  else:
    print('no previous file')
  if os.path.exists(latest_path):
    os.rename(latest_path,previous_path)
    print('latest file renamed to previous_path')
  else:
    print('no latest file')
# ----

old_path = 'old2.log'
previous_path = 'prev2.log'
latest_path = 'latest2.log'

# HTMLソースを得る
url ='https://itunes.apple.com/jp/app/pythonista-3/id1085978097?mt=8'
r = requests.get(url)
html = r.text
root = lxml.html.fromstring(html)

#file_manipulate()

text_output('//*[@id="ember213"]/div/div[2]/header/ul[2]/li/ul/li')
