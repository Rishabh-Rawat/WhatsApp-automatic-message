import mysql.connector
import time
import pyautogui as py
from selenium import webdriver

def date_check(date,month):
    '''This function checks if passed date and month are birthday of any friend in database'''
    month_today=time.localtime()[1]
    date_today=time.localtime()[2]
    if date==date_today and month==month_today:
        return True
    else:
        return False

def time_check():
    '''This function checks if time is 12AM for checking the dates'''
    while True:
        hour_now=time.localtime()[3]
        minute_now=time.localtime()[4]
        second_now=time.localtime()[5]
        if hour_now==0 and minute_now==0 and second_now==0:
            return True

def retrieve_from_table():
    '''This function connects the database table storing birthdays of friends to python and retrieve them from the table'''
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="CHUTIYA#1",database="rishabh")
    cur=mycon.cursor()
    cur.execute("select * from birthday_database")
    details=data=cur.fetchall()
    return details

while True:
    if time_check():
        friends_details=retrieve_from_table()
        
        for onefriend_details in friends_details:
            name,date,month,phno=onefriend_details
            
            if date_check(date,month):
                print("Today is ",name,"'s birthday",sep="")
                print("Wishing",name,"happy birthday...")
                
                driver=webdriver.Chrome("chromedriver")
                driver.get("https://wa.me/"+phno)
                time.sleep(1)
                
                driver.maximize_window()
                time.sleep(1)
                
                open_whatsapp_position=(1064,250)
                py.click(open_whatsapp_position)
                time.sleep(7)
                
                py.typewrite("Happy birthday...")
                py.press("enter")
                driver.quit()
                time.sleep(1)
                print(name,"successfully wished happy birthday !","\n")
                
        print("All done for today !")
        print("Waiting for tomorrow...")
        time.sleep(86000)
