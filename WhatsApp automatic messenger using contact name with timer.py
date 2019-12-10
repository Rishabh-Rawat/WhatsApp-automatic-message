from selenium import webdriver
import time
import pyautogui as py

def time_check():
    while True:
        hour_now=time.localtime()[3]
        minute_now=time.localtime()[4]
        second_now=time.localtime()[5]
        if hour_now==hour and minute_now==minute and second_now==second:
            return True
        
name=input("Enter the name of receiver as per your contacts")
message=input("Enter the message")
hour=int(input("Enter the hour in 24-hour format to send message"))
minute=int(input("Enter the minute to send message"))
second=int(input("Enter the second to send message"))

driver=webdriver.Chrome("D:/chromedriver")
driver.get("https://web.whatsapp.com")
time.sleep(10)
chat_position=driver.find_element_by_css_selector("[title^="+name+"]")
chat_position.click()

message_box_position=py.locateOnScreen('D:\Thonny\MessageBox.png')
py.click(message_box_position)
time.sleep(1)

py.typewrite(message,interval=0.05)
if time_check():
    py.press('enter')