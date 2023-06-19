from bs4 import BeautifulSoup
import requests
import json

class CheckDataLink():
    def __init__(self):
        pass
    def get_news_data(self,search):
        # 로그인할 때 저장한 아이디를 세션으로 사용
        # url의 파라미터로 관심종목을 받음
        resultArray = []
        pageArray = ['1','11','21','31','41','51','61','71','81','91']
        for page in pageArray:
            url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={search}&start={page}'
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            # ? 기사 제목
            titles = soup.find_all('a', attrs={'class': 'news_tit'}, limit=100)
            for a_tag in titles:
                resultArray.append(a_tag['title'])
            # ? 기사 간략내용
            details = soup.select(
                'div.news_wrap.api_ani_send > div > div.news_dsc > div > a', limit=100)
            i = 0
            while True:
                try:
                    resultArray.append(details[i].get_text())
                    i += 1
                    print(i)
                except Exception as inst:
                    print(type(inst))
                    break
        return resultArray

    def includeCheck(self, targetText, keyWord):
        if keyWord in targetText:
            return True
        elif targetText in keyWord:
            return True
        else:
            return False
    def checkWords(self, targetList, keyWord):
        beforeOne = ''
        nextList = []
        result = []
        nextFlag = False
        for i in targetList:
            words = i.split(' ')
            for j in words:
                if nextFlag == True:
                    nextList.append(j)
                    nextFlag = False
                if self.includeCheck(j,keyWord):
                    result.append(j)
                    nextFlag = True
                    if beforeOne != '':
                        nextList.append(beforeOne)
                else:
                    beforeOne = j
        return {'result':result, 'nextList':nextList}
    def countWords(self, targetList):
        result = {}
        for i in targetList:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
        return result
    def allWordCheck(self, targetlist):
        result = []
        for i in targetlist:
            for j in i.split(" "):
                result.append(j)
        return result

def getTopTen(searchWord):
    checkDataLink = CheckDataLink()
    wordsFromNews = checkDataLink.get_news_data(searchWord)
    allcheck = checkDataLink.allWordCheck(wordsFromNews)
    return sorted(checkDataLink.countWords(allcheck).items(),key=lambda x:x[1])[-10:]

# wordsFromNews = checkDataLink.get_news_data(searchWord)
# wordsFromChecker = checkDataLink.checkWords(wordsFromNews,searchWord)
# print('------------------------------------------')
# print(checkDataLink.countWords(wordsFromChecker['result']))
# print('------------------------------------------')

# print(checkDataLink.countWords(wordsFromChecker['nextList']))
# print('------------------------------------------')

# allcheck = checkDataLink.allWordCheck(wordsFromNews)
# print(sorted(checkDataLink.countWords(allcheck).items(),key=lambda x:x[1])[-10:])
# print('------------------------------------------')
