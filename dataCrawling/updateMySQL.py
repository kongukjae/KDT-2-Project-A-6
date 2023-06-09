import requests
import json
import pymysql

def jsonOpen(directory):
    with open(directory, "r") as f:
        data = json.load(f)
    return data
def jsonSave(directory,result):
    with open(directory, "w") as f:
        json.dump(result, f, ensure_ascii=False,indent=4)

# pip install PyMySQL
con = pymysql.connect(host='localhost', user='root', password='00000000',db='dogListApi', charset='utf8') # 한글처리 (charset = 'utf8')
# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor()

targetList = ['resultFromGovernmentAPI.json','resultFromInstagramAddInfo.json','resultFromZooseyoAddInfo.json']

for j in range(len(targetList)):
    target = jsonOpen(targetList[j])
    dataFrom = ''
    if j == 0:
        for i in target:
            # STEP 4: SQL문 실행 및 Fetch
            sql = f"INSERT INTO dogList(date, location, age, gender, breed, imageLink, dataFrom, webLink) VALUES('{i['date']}','{i['location']}','{i['age']}','{i['gender']}','{i['breed']}','{i['imageLink']}','{i['careName']}','{i['webLink']}');"
            cur.execute(sql)
            con.commit()
    elif j == 1:
        for i in target:
            # STEP 4: SQL문 실행 및 Fetch
            sql = f"INSERT INTO dogList(date, location, age, gender, breed, imageLink, dataFrom, webLink) VALUES('{i['date']}','{i['location']}','{i['age']}','{i['gender']}','{i['breed']}','{i['imageLink']}','instagram','{i['webLink']}');"
            cur.execute(sql)
            con.commit()
    else:
        for i in target:
            # STEP 4: SQL문 실행 및 Fetch
            sql = f"INSERT INTO dogList(date, location, age, gender, breed, imageLink, dataFrom, webLink) VALUES('{i['date']}','{i['location']}','{i['age']}','{i['gender']}','{i['breed']}','{i['imageLink']}','zooseyo.com','{i['webLink']}');"
            cur.execute(sql)
            con.commit()




# # 데이타 Fetch
# rows = cur.fetchall()
# print(rows)     # 전체 rows
# STEP 5: DB 연결 종료
con.close()

