from chatGPT import chatGPT
from chatGPT import chatGPTTurbo
import json
from textReading import agePicker

class TextGuess:
    def __init__(self):
         pass
    def jsonOpen(self, directory):
        with open(directory, "r") as f:
            data = json.load(f)
        return data
    def ageGuess(self, data):
        result = []
        for i in data:
            age = chatGPT('해당 유기견 입양 게시글을 읽고 유기견의 나이를 추론해줘 원하는 형식은 주어없이 문장이 아닌 단답형으로 나이를 추론해줘 원하는 결과 형식은 "n살" 이야 ' + i['mainText'])
            agepick = agePicker(age)
            i['age'] = 'chatGPT : ' + agepick
            result.append(i)
        return result
    def allGuess(self, data):
        result = []
        cnt = 0
        for i in data:
            askGPT = chatGPTTurbo("다음 게시 글을 읽고 유기견 분양 글인지 판단해줘. 만약 아니라면 결과는 'False' 라고 짧게 해줘. 만약에 유기견 분양 글이 맞다면 결과를 강아지 나이, 분양 지역, 강아지 성별 3가지를 각각 'age', 'location','gender'를 키 값으로 가지는 JSON형식으로 알려줘. 만약 추론이 불가능하다면 해당 key값의 value를 '추측 불가'로 넣어도 돼. 게시글 : " + i['mainText'])
            result.append(askGPT)
            # askGPT = i['mainText']
            print(askGPT)
            cnt += 1
            if cnt > 5:
                break
        print(result)
        return result
    def trueGuess(self, data):
        result = []
        for i in data:
            try:
                askGPT = chatGPTTurbo("다음 게시 글을 읽고 강아지 분양글인지 판단해줘. 맞으면 True, 틀리면 False 로 True/False 형식으로 해줘. 게시글 : " + i['mainText'])
                # askGPT = i['mainText']
                print(i['mainText'])
                print(askGPT)
                if askGPT == "True":
                    result.append(i)
            except:
                pass
        return result
    def ageLocGenGuess(self, data):
        result = []
        for i in data:
            askGPT = chatGPTTurbo("해당 유기견 입양 게시글을 읽고 강아지 나이, 분양 지역, 강아지 성별을 추론해줘  결과를 강아지 나이, 분양 지역, 강아지 성별 3가지를 각각 'age', 'location','gender'를 키 값으로 가지는 JSON형식으로 알려줘. 만약 추론이 불가능하다면 해당 key값의 value를 '추측 불가'로 넣어도 돼. 게시글 :  " + i['mainText'])
            # askGPT = i['mainText']
            print(askGPT)
            try:
                jsonObject = json.loads(askGPT)
                for j in jsonObject:
                    i[j] = 'chatGPT : ' + jsonObject[j]
                result.append(i)
            except:
                pass
        return result
    def jsonSave(self,directory,result):
        with open(directory, "w") as f:
            json.dump(result, f, ensure_ascii=False,indent=4)
    def dateFrom(self, value):
        result = ''
        for i in value:
            if i.isdigit():
                result += i
            if len(result) == 4:
                result += '-'
            if len(result) == 7:
                result += '-'
            if len(result) == 10:
                break
        return result
def zooseyo():
    zooseyoTextGuess= TextGuess()
    jsonData = zooseyoTextGuess.jsonOpen("resultFromZooseyo.json")
    ageAppend = zooseyoTextGuess.ageGuess(jsonData)
    zooseyoTextGuess.jsonSave('resultFromZooseyoAddInfo.json',ageAppend)
def insta():
    instaTextGuess = TextGuess()
    jsonData = instaTextGuess.jsonOpen("resultFromInstagram.json")
    trueCheck = instaTextGuess.trueGuess(jsonData)
    instaTextGuess.jsonSave('resultFromInstagramFiltering.json',trueCheck)
    infoAppend = instaTextGuess.ageLocGenGuess(trueCheck)
    instaTextGuess.jsonSave('resultFromInstagramAddInfo.json',infoAppend)
def changeDateInstagram():
    change = TextGuess()
    jsonData = change.jsonOpen('resultFromInstagramAddInfo.json')
    for i in jsonData:
        i['date'] = change.dateFrom(i['date'])
    change.jsonSave('resultFromInstagramAddInfo.json', jsonData)
def changeDateZooseyo():
    change = TextGuess()
    jsonData = change.jsonOpen('resultFromZooseyoAddInfo.json')
    for i in jsonData:
        i['date'] = change.dateFrom(i['date'])
    change.jsonSave('resultFromZooseyoAddInfo.json', jsonData)

def changeDateGovernmentAPI():
    change = TextGuess()
    jsonData = change.jsonOpen('resultFromGovernmentAPI.json')
    for i in jsonData:
        i['date'] = change.dateFrom(i['date'])
    change.jsonSave('resultFromGovernmentAPI.json', jsonData)

if __name__ == '__main__':
    insta()
    changeDateInstagram()