import requests  # 정보를 긁어오는데 필요한 requests 라이브러리를 가져옵니다.

# 입력한 주소로 가서 정보를 가져옵니다.
r = requests.get('https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json?address=서울특별시 용산구')
# 가져온 정보를 파이썬이 사용할 수 있도록 변경합니다. 
rjson = r.json()

# 상점 정보를 꺼냅니다.
store_list = rjson['stores']

# 상점 목록을 돌면서 하나하나 작업을 진행합니다.
for store in store_list:
		# 만약에 충분한 양의 마스크가 남아있는 약국이면
    if store['remain_stat'] == 'plenty':
				# 약국의 주소와 이름을 출력합니다.
        print(store['addr'],store['name'])