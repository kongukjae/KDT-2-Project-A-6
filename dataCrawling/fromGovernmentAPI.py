import requests
import json
import pymysql
import datetime

now = datetime.datetime.now()
toDate = str(datetime.datetime.now())[:10]
fromDate = str(now - datetime.timedelta(days=10))[:10]
def noslash(value):
    result = ''
    for i in value:
        if i != '-':
            result += i
    return result

toDatewithNoslash = noslash(toDate)
fromDatewithNoslach = noslash(fromDate)

# pip install requests
# pip install PyMySQL
con = pymysql.connect(host='localhost', user='root', password='00000000',db='dogListApi', charset='utf8') # 한글처리 (charset = 'utf8')
# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor()

response = requests.get(f"https://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?pageNo=1&numOfRows=1&bgnde={fromDatewithNoslach}&endde={toDatewithNoslash}&_type=json&serviceKey=a71YfWfLciBMXYG2e5zc9D1hNlQM29N7TICbhuOzOXtUnxJIGZjs0FWWuENqX%2FGdMEvpH%2B7eH1AZ2mhnfQmmiA%3D%3D")
response = json.loads(response.text)
count = response['response']['body']['totalCount']//1000
print(count)
for k in range(1,count+2):
    print(k)
    response = requests.get(f"https://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?pageNo={k}&numOfRows=1000&bgnde=20230518&endde=20230531&_type=json&serviceKey=a71YfWfLciBMXYG2e5zc9D1hNlQM29N7TICbhuOzOXtUnxJIGZjs0FWWuENqX%2FGdMEvpH%2B7eH1AZ2mhnfQmmiA%3D%3D")
    response = json.loads(response.text)
    result = response['response']['body']['items']['item']
    for i in result:
        if i['kindCd'][:3]=='[개]' and i['processState']=='보호중':
  
            # STEP 4: SQL문 실행 및 Fetch
            sql = f"INSERT INTO dogList(date, location, age, gender, breed, imageLink, careName, webLink) VALUES('{i['noticeSdt']}','{i['careAddr']}','{i['age']}','{i['sexCd']}','{i['kindCd'][4:]}','{i['popfile']}','{i['careNm']}','{'https://www.animal.go.kr/front/awtis/protection/protectionDtl.do?desertionNo=' + i['desertionNo']}');"
            cur.execute(sql)
            con.commit()

# # 데이타 Fetch
# rows = cur.fetchall()
# print(rows)     # 전체 rows
# STEP 5: DB 연결 종료
con.close()

