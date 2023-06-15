from urllib import request
from io import BytesIO
from PIL import Image
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def saveImage(url,savelocation):
    request.urlretrieve(url, savelocation) #해당 url에서 이미지를 다운로드 메소드
def jsonOpen(directory):
    with open(directory, "r") as f:
        data = json.load(f)
    return data
def jsonSave(directory,result):
    with open(directory, "w") as f:
        json.dump(result, f, ensure_ascii=False,indent=4)
def instaImageSave():
    imageFromInstagram = jsonOpen('./resultFromInstagramAddInfo.json')
    result = []
    count = 0
    for i in imageFromInstagram:
        imageLink = i['imageLink']
        newImageLink = str(count)  + '.jpg'
        saveImage(imageLink, '../apiServer/images/instagram/' + newImageLink)
        i['imageLink'] = 'http://localhost:2080/image/' + newImageLink
        result.append(i)
        count += 1
    jsonSave('./resultFromInstagramAddInfoTest.json',result)

instaImageSave()

# 다운받을 이미지 url
# url = "https://www.zooseyo.or.kr/dog_sale/photo_free/202306/1686176309_31241700.jpeg"

# # # request.urlopen()
# # res = request.urlopen(url).read()

# # # Image open
# # img = Image.open(BytesIO(res))
# # print(img)

# savelocation = "./test.jpg" #내컴퓨터의 저장 위치

# saveImage(url,savelocation)