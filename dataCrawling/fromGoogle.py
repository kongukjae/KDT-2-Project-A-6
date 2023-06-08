from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

driver = webdriver.Chrome()
result = []
def zooseyo():
  result = []
  pageNo = 1
  loopFlag = False
  while True:
    driver.get(f'https://www.zooseyo.or.kr/Yu_board/freesale.html?animal=강아지&area=&ty=1&page={pageNo}')
    time.sleep(4)
    targets = driver.find_elements(By.TAG_NAME,'tr')
    for i in targets:
      if i.get_attribute('height') == '50' and i.get_attribute('onclick') != None:
        result.append(i.get_attribute('onclick').split(',')[0].split('(')[1][1:-1])
        try:
          if i.find_element(By.TAG_NAME,'p').text == '05/29':
            loopFlag = True
            break
        except:
          continue
    if loopFlag:
      break
    else:
      pageNo += 1
  return result

zooseyoList = zooseyo()
def zooseyoTravelPages(targetList):
  for i in targetList:
    try:
      driver.get(f'https://www.zooseyo.or.kr/Yu_board/{i}')
      time.sleep(4)
      mainImage = driver.find_element(By.XPATH,'//*[@id="imgg1"]/img')
      mainImageLink = mainImage.get_attribute('src')
      date = driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div').text
      breed = driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[5]/td/table/tbody/tr/td[2]/b').text
      gender = driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[9]/td/table/tbody/tr/td[4]').text
      location = driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[7]/td/table/tbody/tr/td[2]').text
      mainText = driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[23]/td/table/tbody/tr/td[2]').text

      result.append({'imageLink':mainImageLink,'date':date,'breed':breed,'gender':gender,'location':location,'mainText':mainText})
      print(mainImageLink)
      print(date)
      print(breed)
      print(gender)
      print(location)
      print(mainText)
    except:
      continue


zooseyoTravelPages(zooseyoList)





# input = driver.find_elements(By.TAG_NAME, 'input');

# input[0].send_keys("joyeji1577@rockdian.com")
# input[1].send_keys("asdasd123")
# input[1].send_keys(Keys.RETURN)

# time.sleep(5)
# driver.get("https://www.instagram.com/explore/tags/%EC%9C%A0%EA%B8%B0%EA%B2%AC%EC%9E%85%EC%96%91/")
# time.sleep(10)

# recent = driver.find_elements(By.TAG_NAME, 'h2')

# # print(recent[1].text)
# # print(recent[1].get_attribute('class'))
# rows = recent[1].get_property('nextSibling').get_property('firstChild').get_property('firstChild').get_property('children')
# rows[0].click()
# # recent[1].get_property('nextSibling').get_property('firstChild').get_property('firstChild').get_property('firstChild').get_property('firstChild').click()
# time.sleep(2)

# mainTextTag = driver.find_elements(By.TAG_NAME,'h1')
# # print(len(mainTextTag))
# result['mainText']=mainTextTag[0].text

# # imageTag = driver.find_elements(By.TAG_NAME,'img')
# # for k in imageTag:
# #     print(k.get_attribute('alt'))
# headerTag = driver.find_elements(By.TAG_NAME,'header')
# result['imageLink']=headerTag[1].get_property('parentElement').get_property('parentElement').get_property('parentElement').get_property('parentElement').get_property('parentElement').get_property('previousSibling').find_element(By.TAG_NAME,'img').get_attribute('src')




# exitbuttonList = driver.find_elements(By.TAG_NAME, "svg")
# exitbutton = {}
# nextbutton = []
# for i in exitbuttonList:
#     if i.get_attribute('aria-label') == '닫기':
#         exitbutton = i
#     elif i.get_attribute('aria-label') == '다음':
#         nextbutton.append(i)
#         # i.get_property('parentElement').get_property('parentElement').click()


# # nextbutton[0].click()
# time.sleep(20)
# exitbutton.click()
# time.sleep(100)

with open('./resultFromzooseyo.json','w') as f:
  json.dump(result, f, ensure_ascii=False, indent=4)