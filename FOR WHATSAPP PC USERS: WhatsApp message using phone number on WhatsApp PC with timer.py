import time
import pyautogui as py
from selenium import webdriver

def time_check(hour,minute,second):
    while True:
        hour_now=time.localtime()[3]
        minute_now=time.localtime()[4]
        second_now=time.localtime()[5]
        if hour_now==hour and minute_now==minute and second_now==second:
            return True


phno=input("Enter the receiver's WhatsApp number with country code ")
message=input("Enter the message ")
hour=int(input("Enter the hour in 24-hour format to send message "))
minute=int(input("Enter the minute to send message "))
second=int(input("Enter the second to send message "))
number_of_bombings=int(input("Enter the number of times you want to send the message "))

driver=webdriver.Chrome("chromedriver")
driver.get("https://wa.me/"+phno)
time.sleep(1)
driver.maximize_window()
time.sleep(2)

open_whatsapp_position=(1064,250)
py.click(open_whatsapp_position)

if time_check(hour,minute,second):
    for i in range(number_of_bombings):
        py.typewrite(message)
        py.press('enter')
