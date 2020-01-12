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

def give_open_whatsapp_location():
    size_of_screen=py.size()
    if size_of_screen==(1280,960):
        open_whatsapp_position=(711,187)
    elif size_of_screen==(1280,720) or size_of_screen==(1280,600):
        open_whatsapp_position=(703,184)
    elif size_of_screen==(800,600):
        open_whatsapp_position=(475,188)
    else:
        total_x_size=size_of_screen[0]
        total_y_size=size_of_screen[1]
        open_whatsapp_x_coordinate=(55/100)*total_x_size
        open_whatsapp_y_coordinate=(22.75/100)*total_y_size
        open_whatsapp_position=(open_whatsapp_x_coordinate,open_whatsapp_y_coordinate)
    return open_whatsapp_position

#main
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
time.sleep(1)

required_position=give_open_whatsapp_location()
py.click(required_position)

if time_check(hour,minute,second):
    for i in range(number_of_bombings):
        py.typewrite(message)
        py.press('enter')
    py.typewrite("Message sent using Bomber Made by Rishabh ;_;")
    py.press('enter')