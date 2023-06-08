from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

class ZooseyoCrawler:
  def __init__(self):
    self.driver = webdriver.Chrome()
    self.result = {}
  def goUrl(self, url):
    self.driver.get(url)
    time.sleep(3)
  def searchTargetList(self,date):
    result = []
    pageNo = 1
    loopFlag = False
    while True:
      self.driver.get(f'https://www.zooseyo.or.kr/Yu_board/freesale.html?animal=강아지&area=&ty=1&page={pageNo}')
      time.sleep(4)
      targets = self.driver.find_elements(By.TAG_NAME,'tr')
      for i in targets:
        if i.get_attribute('height') == '50' and i.get_attribute('onclick') != None:
          result.append(i.get_attribute('onclick').split(',')[0].split('(')[1][1:-1])
          try:
            if i.find_element(By.TAG_NAME,'p').text == date:
              loopFlag = True
              break
          except:
            continue
      if loopFlag:
        break
      else:
        pageNo += 1
    return result
  def getImageInfo(self):
    mainImage = self.driver.find_element(By.XPATH,'//*[@id="imgg1"]/img')
    mainImageLink = mainImage.get_attribute('src')
    return mainImageLink
  def getDateInfo(self):
    date = self.driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div').text
    return date
  def getBreedInfo(self):
    breed = self.driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[5]/td/table/tbody/tr/td[2]/b').text
    return breed
  def getGenderInfo(self):
    gender = self.driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[9]/td/table/tbody/tr/td[4]').text
    return gender
  def getLocationInfo(self):
    location = self.driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[7]/td/table/tbody/tr/td[2]').text
    return location
  def getMainTextInfo(self):
    mainText = self.driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[23]/td/table/tbody/tr/td[2]').text
    return mainText
  def saveJson(self, resultList):
    with open('./resultFromZooseyo.json','w') as f:
      json.dump(resultList, f, ensure_ascii=False, indent=4)

def main():
  resultList = []
  zooseyoCrawler = ZooseyoCrawler()
  targetList = zooseyoCrawler.searchTargetList('05/31')
  for i in targetList:
    try:
      zooseyoCrawler.goUrl(f'https://www.zooseyo.or.kr/Yu_board/{i}')
      time.sleep(4)
      resultList.append({'imageLink':zooseyoCrawler.getImageInfo(),'date':zooseyoCrawler.getDateInfo(),'breed':zooseyoCrawler.getBreedInfo(),'gender':zooseyoCrawler.getGenderInfo(),'location':zooseyoCrawler.getLocationInfo(),'mainText':zooseyoCrawler.getMainTextInfo()})
    except:
      continue
  zooseyoCrawler.saveJson(resultList)


if __name__ == '__main__':
  main()