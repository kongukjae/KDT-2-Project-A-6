import requests
import json
import datetime


class GovernmentCrawler:
    def __init__(self):
        pass
    def noslash(self, value):
        result = ''
        for i in value:
            if i != '-':
                result += i
        return result  
    def count(self, fromDatewithNoslach, toDatewithNoslash):
        response = requests.get(f"https://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?pageNo=1&numOfRows=1&bgnde={fromDatewithNoslach}&endde={toDatewithNoslash}&_type=json&serviceKey=a71YfWfLciBMXYG2e5zc9D1hNlQM29N7TICbhuOzOXtUnxJIGZjs0FWWuENqX%2FGdMEvpH%2B7eH1AZ2mhnfQmmiA%3D%3D")
        response = json.loads(response.text)
        count = response['response']['body']['totalCount']//1000
        return count
    def appendData(self, count,resultList):
        for k in range(1,count+2):
            response = requests.get(f"https://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?pageNo={k}&numOfRows=1000&bgnde=20230518&endde=20230531&_type=json&serviceKey=a71YfWfLciBMXYG2e5zc9D1hNlQM29N7TICbhuOzOXtUnxJIGZjs0FWWuENqX%2FGdMEvpH%2B7eH1AZ2mhnfQmmiA%3D%3D")
            response = json.loads(response.text)
            result = response['response']['body']['items']['item']
            for i in result:
                if i['kindCd'][:3]=='[개]' and i['processState']=='보호중':
                    gender = '남아' if i['sexCd'] == 'M' else '여아' if i['sexCd'] == 'F' else '알 수 없음'
                    thisDate = {'date':i['noticeSdt'], "location":i['careAddr'], "age":i['age'], "gender":gender, "breed":i['kindCd'][4:], "imageLink":i['popfile'], "careName":i['careNm'], "webLink":f'https://www.animal.go.kr/front/awtis/protection/protectionDtl.do?desertionNo=' + i['desertionNo']}
                    resultList.append(thisDate)
    def saveJson(self, resultList):
        with open('./resultFromGovernmentAPI.json','w') as f:
            json.dump(resultList, f, ensure_ascii=False, indent=4)
def main():
    governmentCrawler = GovernmentCrawler()
    resultList = []
    now = datetime.datetime.now()
    toDate = str(datetime.datetime.now())[:10]
    fromDate = str(now - datetime.timedelta(days=10))[:10]  
    toDatewithNoslash = governmentCrawler.noslash(toDate)   
    fromDatewithNoslach = governmentCrawler.noslash(fromDate)  
    # pip install requests  
    count = governmentCrawler.count(fromDatewithNoslach,toDatewithNoslash)
    governmentCrawler.appendData(count,resultList)
    governmentCrawler.saveJson(resultList)


if __name__ == '__main__':
  main()

