from konlpy.tag import Okt
import json
import pymysql

def returnNoun(text):
    okt = Okt()
    result = []
    checked = okt.pos(text)
    for i in checked:
        if i[1] == 'Noun':
            result.append(i[0])
    return result

def jsonSave(directory,result):
    with open(directory, "w") as f:
        json.dump(result, f, ensure_ascii=False,indent=4)

indexDict = {}
keyList=[]

conn = pymysql.connect(host='localhost', user='root', password='00000000',db='dogListApi', charset='utf8') # 한글처리 (charset = 'utf8')

sql = "SELECT * FROM dogList LIMIT 8000"

with conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        result = cur.fetchall()
        for i in result:
            targetString = i[2] +' '+ i[4] +' '+ i[5] +' '+ i[7]
            nounList = set(returnNoun(targetString))
            for j in nounList:
                if j in keyList:
                    indexDict[j].append(i[0])
                else:
                    indexDict[j] = [i[0]]
                    keyList.append(j)
jsonSave('indexResult.json',indexDict)
