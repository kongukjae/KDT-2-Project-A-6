from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

result = {}
driver = webdriver.Chrome()
url = 'https://www.instagram.com/accounts/login/'
driver.get(url)
time.sleep(3)

input = driver.find_elements(By.TAG_NAME, 'input');

input[0].send_keys("joyeji1577@rockdian.com")
input[1].send_keys("asdasd123")
input[1].send_keys(Keys.RETURN)

time.sleep(5)
driver.get("https://www.instagram.com/explore/tags/%EC%9C%A0%EA%B8%B0%EA%B2%AC%EC%9E%85%EC%96%91/")
time.sleep(10)

recent = driver.find_elements(By.TAG_NAME, 'h2')

# print(recent[1].text)
# print(recent[1].get_attribute('class'))
rows = recent[-1].get_property('nextSibling').get_property('firstChild').get_property('firstChild').get_property('children')
rows[0].click()
# recent[1].get_property('nextSibling').get_property('firstChild').get_property('firstChild').get_property('firstChild').get_property('firstChild').click()
time.sleep(2)

mainTextTag = driver.find_elements(By.TAG_NAME,'h1')
# print(len(mainTextTag))
result['mainText']=mainTextTag[0].text

# imageTag = driver.find_elements(By.TAG_NAME,'img')
# for k in imageTag:
#     print(k.get_attribute('alt'))
headerTag = driver.find_elements(By.TAG_NAME,'header')
result['imageLink']=headerTag[1].get_property('parentElement').get_property('parentElement').get_property('parentElement').get_property('parentElement').get_property('parentElement').get_property('previousSibling').find_element(By.TAG_NAME,'img').get_attribute('src')
time.sleep(2)
svgList = driver.find_elements(By.TAG_NAME, 'svg')
time.sleep(2)
nextTarget = None
for i in svgList:
  if i.get_attribute('aria-label') == '다음':
    nextTarget = i.get_property('parentElement').get_property('parentElement').get_property('parentElement')
    break
nextTarget.click()
time.sleep(3)



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

with open('./result.json','w') as f:
  json.dump(result, f, ensure_ascii=False, indent=4)