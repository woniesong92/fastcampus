#!/usr/bin/python
# -*- coding: utf-8 -*-

# CH. 부동산 정보 모으기

import requests
from bs4 import BeautifulSoup

url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev"
ServiceKey = "" # ServiceKey 설정
pageNo = 1
numOfRows = 1000
LAWD_CD = '11110'
DEAL_YMD = '202012'

def get_apt_info():
  raw_resp = requests.get(url, params={
    'ServiceKey': ServiceKey,
    'pageNo': pageNo,
    'numOfRows': numOfRows,
    'LAWD_CD': LAWD_CD,
    'DEAL_YMD': DEAL_YMD,
  })
  return raw_resp.text

def parse_apt_info(raw_apt_info):
  keys = ['거래금액', '아파트', '도로명코드', '년', '월', '일', '건축년도']
  soup = BeautifulSoup(raw_apt_info, 'lxml-xml')
  results = []
  
  items = soup.findAll('item') # 아이템 엘레먼트만 뽑기
  for item in items: # 아이템 엘레먼트를 하나씩 반복하면서 돌아가기 (루프)
    result = {}
    for key in keys:
      result[key] = item.find(key).text

    result['거래금액'] = result['거래금액'].strip()
    result['건축년도'] = int(result['건축년도'])
    results.append(result)
  return results

raw_apt_info = get_apt_info()
parsed_apt_info = parse_apt_info(raw_apt_info)
print(parsed_apt_info)
