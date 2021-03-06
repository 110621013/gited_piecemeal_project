from selenium import webdriver
from time import sleep
from PIL import Image
#from simshow import simshow  #以 pip install simple-imshow 安裝模組
import cv2

delay = 0.3
url = 'https://irs.thsrc.com.tw/IMINT/'  #高鐵訂票網頁
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=option)
driver.get(url)
sleep(delay)  #加入等待
driver.find_element_by_id("btn-confirm").click()
sleep(delay)
driver.save_screenshot('tem.png')  #擷取螢幕後存檔
captchaid = driver.find_element_by_id('BookingS1Form_homeCaptcha_passCode')  #驗證碼圖形id
#取得圖形位置
x1 = captchaid.location['x']
y1 = captchaid.location['y']
x2 = x1 + captchaid.size['width']
y2 = y1 + captchaid.size['height']
image1 = Image.open('tem.png')  #讀取螢幕圖形
image2 = image1.crop((x1, y1, x2, y2))  #擷取驗證碼圖形
image2.save('captcha.png')  #圖形存檔
#simshow(image2)  #顯示圖形
###
img = cv2.imread('tem.png')
cv2.imshow('img:', img)
###
captchatext = input('輸入驗證碼：')

driver.find_element_by_name("selectStartStation").click()
sleep(delay)
driver.find_element_by_xpath("(//option[@value='2'])[1]").click()
sleep(delay)
driver.find_element_by_name("selectDestinationStation").click()
sleep(delay)
driver.find_element_by_xpath("(//option[@value='7'])[2]").click()
sleep(delay)
driver.find_element_by_id("seatRadio1").click()
sleep(delay)
driver.find_element_by_id("ToTimePicker").click()
sleep(delay)
driver.find_element_by_xpath("//tbody/tr[3]/td[3]").click()
sleep(delay)
driver.find_element_by_name("toTimeTable").send_keys("\n")
sleep(delay)
driver.find_element_by_xpath("(//option[@value='800A'])[1]").click()
sleep(delay)
driver.find_element_by_name("homeCaptcha:securityCode").send_keys("\n")
sleep(delay)
driver.find_element_by_name("homeCaptcha:securityCode").clear()
sleep(delay)
driver.find_element_by_name("homeCaptcha:securityCode").send_keys(captchatext)
sleep(delay)
driver.find_element_by_id("SubmitButton").click()
sleep(delay)
driver.find_element_by_xpath("(//input[@name='TrainQueryDataViewPanel:TrainGroup'])[3]").click()
sleep(delay)
driver.find_element_by_name("SubmitButton").click()
sleep(delay)
driver.find_element_by_id("idNumber").click()
sleep(delay)
driver.find_element_by_id("idNumber").clear()
sleep(delay)
driver.find_element_by_id("idNumber").send_keys("A117290980")
sleep(delay)
driver.find_element_by_id("mobileInputRadio").click()
sleep(delay)
driver.find_element_by_id("mobilePhone").click()
sleep(delay)
driver.find_element_by_id("mobilePhone").clear()
sleep(delay)
driver.find_element_by_id("mobilePhone").send_keys("0922735901")
sleep(delay)
driver.find_element_by_name("agree").click()
sleep(delay)
#driver.find_element_by_id("isSubmit").click()
print('完成訂票！')
