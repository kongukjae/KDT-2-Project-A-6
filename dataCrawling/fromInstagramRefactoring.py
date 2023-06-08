from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

class InstaCrawler:
  def __init__(self):
    self.driver = webdriver.Chrome()
    self.result = {}
  def goUrl(self, url):
    self.driver.get(url)
    time.sleep(3)
  def login(self, instaId,instaPw):
    input = self.driver.find_elements(By.TAG_NAME, 'input');
    input[0].send_keys(instaId)
    input[1].send_keys(instaPw)
    input[1].send_keys(Keys.RETURN)
    time.sleep(5)
  def search(self, keyword):
    self.driver.get(f"https://www.instagram.com/explore/tags/{keyword}")
    time.sleep(10)
  def getFirstPost(self):
    recent = self.driver.find_elements(By.TAG_NAME, 'h2')
    rows = recent[-1].get_property('nextSibling').get_property('firstChild').get_property('firstChild').get_property('children')
    rows[0].click()
    time.sleep(2)
  def getTextInfo(self):
    mainTextTag = self.driver.find_elements(By.TAG_NAME,'h1')
    time.sleep(1)
    try:
      return mainTextTag[0].text
    except:
      return 'none'
  def getDateInfo(self):
    timeTag = self.driver.find_elements(By.TAG_NAME,'time')
    return timeTag[0].get_attribute('datetime')
  
  
  def getImageInfo(self):
    headerTag = self.driver.find_elements(By.TAG_NAME,'header')
    result=headerTag[1].get_property('parentElement').get_property('parentElement').get_property('parentElement').get_property('parentElement').get_property('parentElement').get_property('previousSibling').find_element(By.TAG_NAME,'img').get_attribute('src')
    time.sleep(2)
    return result
  def getCurrentUrl(self):
    url = self.driver.current_url
    return url
  def gotoNext(self):
    svgList = self.driver.find_elements(By.TAG_NAME, 'svg')
    time.sleep(2)
    nextTarget = None
    for i in svgList:
      if i.get_attribute('aria-label') == '다음':
        nextTarget = i.get_property('parentElement').get_property('parentElement').get_property('parentElement')
        break
    nextTarget.click()
    time.sleep(2)
  def saveJson(self, resultList):
    with open('./resultFromInstagram.json','w') as f:
      json.dump(resultList, f, ensure_ascii=False, indent=4)

def main():
  resultList = []
  instaCrawler = InstaCrawler()
  instaCrawler.goUrl('https://www.instagram.com/accounts/login/')
  instaCrawler.login("joyeji1577@rockdian.com","asdasd123")
  instaCrawler.search("유기견입양")
  instaCrawler.getFirstPost()

  for _ in range(100):
    resultDict = {}
    resultDict["mainText"] = instaCrawler.getTextInfo()
    if len(resultDict["mainText"]) < 50:
      instaCrawler.gotoNext()
      continue
    try:
      resultDict["date"] = instaCrawler.getDateInfo()
      resultDict["imageLink"] = instaCrawler.getImageInfo()
      resultDict["webLink"] = instaCrawler.getCurrentUrl()
      resultList.append(resultDict)
      instaCrawler.gotoNext()
    except:
      instaCrawler.gotoNext()
  print(resultList)
  instaCrawler.saveJson(resultList)

if __name__ == '__main__':
  main()
  