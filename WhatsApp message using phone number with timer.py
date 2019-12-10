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
        
        
phno=input("Enter the receiver's WhatsApp number")
message=input("Enter the message")
hour=int(input("Enter the hour in 24-hour format to send message"))
minute=int(input("Enter the minute to send message"))
second=int(input("Enter the second to send message"))
number_of_bombings=int(input("Enter the number of times you want to bomb"))

driver=webdriver.Chrome("D:/chromedriver")
driver.get("https://wa.me/91"+phno)
time.sleep(5)

open_whatsapp_position=py.locateOnScreen('D:\Thonny\OpenWhatsApp.png')
py.click(open_whatsapp_position)
time.sleep(10)

message_box_position=py.locateOnScreen('D:\Thonny\MessageBox.png')
py.click(message_box_position)
time.sleep(1)

if time_check():
    for i in range(number_of_bombings):
        py.typewrite(message,interval=0.05)
        py.press('enter')