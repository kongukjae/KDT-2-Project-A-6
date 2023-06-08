from chatGPT import chatGPT
import json
from textReading import agePicker

class TextGuess:
    def __init__(self):
         pass
    def jsonOpen(self, directory):
        # print(chatGPT('안녕'))
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
        for i in data:
            askGPT = chatGPT("다음 게시 글을 읽고 유기견 분양 글인지 판단해줘. 만약 아니라면 결과는 'False' 라고 짧게 해줘. 만약에 유기견 분양 글이 맞다면 결과를 강아지 나이, 분양 지역, 강아지 성별 3가지를 각각 'age', 'location','gender'를 키 값으로 가지는 JSON형식으로 알려줘 만약 추론이 불가능하다면 해당 key값의 value를 '추측 불가'로 넣어도 돼 " + i['mainText'])
            result.append(askGPT)
            # askGPT = i['mainText']
            print(askGPT)
        print(result)
        return result
    def jsonSave(self,directory,result):
        with open(directory, "w") as f:
            json.dump(result, f, ensure_ascii=False,indent=4)


def main():
    def zooseyo():
        zooseyoTextGuess= TextGuess()
        jsonData = zooseyoTextGuess.jsonOpen("resultFromZooseyo.json")
        ageAppend = zooseyoTextGuess.ageGuess(jsonData)
        zooseyoTextGuess.jsonSave('resultFromZooseyoAddAgeVer2.json',ageAppend)
    def insta():
        instaTextGuess = TextGuess()
        jsonData = instaTextGuess.jsonOpen("resultFromInstagram.json")
        instaTextGuess.allGuess(jsonData)
    insta()

if __name__ == '__main__':
    main()