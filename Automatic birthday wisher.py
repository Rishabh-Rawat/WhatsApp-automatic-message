# automatic birthday wisher
# created by Rishabh-Rawat
import mysql.connector as msq              #importing packages/modules
import time
import pyautogui as py  
from selenium import webdriver

def date_check(date,month):
    '''This function checks if passed date and month are birthday of any friend in database'''
    month_today=time.localtime()[1]      # stores current month from localtime() list
    date_today=time.localtime()[2]       # stores current date from localtime() list
    if date==date_today and month==month_today:# checks if current date-month matches
        return True
    else:
        return False

def time_check():
    '''This function checks if time is 12AM for checking the dates'''
    while True:
        hour_now=time.localtime()[3]    # stores current hour from localtime() list
        minute_now=time.localtime()[4]  # stores current minute from localtime() list
        second_now=time.localtime()[5]  # stores current second from localtime() list
        if hour_now==0 and minute_now==0 and second_now==0: #checks if current time is 12AM
            return True

def give_open_whatsapp_position():
    '''This function returns the position of the OpenWhatsApp button on the screen
        as per the current monitor resolution'''
    size_of_screen=py.size()           # stores the current resolution of the monitor
    if size_of_screen==(1280,960):                                               
        open_whatsapp_position=(711,187)  # button position for screen with resolution 1280x960
    elif size_of_screen==(1280,720) or size_of_screen==(1280,600):               
        open_whatsapp_position=(703,184) #button position for resolution 1280x720 or 1280x600
    elif size_of_screen==(800,600):                                              
        open_whatsapp_position=(475,188)    # button position for screen with resolution 800x600
    else:                # calculating position for all other valid screen resolutions
        total_x_size=size_of_screen[0]
        total_y_size=size_of_screen[1]
        open_whatsapp_x_coordinate=(55/100)*total_x_size
        open_whatsapp_y_coordinate=(22.75/100)*total_y_size
        open_whatsapp_position=(open_whatsapp_x_coordinate,open_whatsapp_y_coordinate)
    return open_whatsapp_position        # returns the required position of the button


def retrieve_from_table():
    '''This function connects the database table storing birthdays of friends
       to python and retrieve them from the table'''
    mycon=msq.connect(host="localhost",user="root",passwd="CHUTIYA#1",database="rishabh")
    cur=mycon.cursor()       # creates cursor instance
    cur.execute("select * from birthday_database")    # retriveve friends details from table
    details=data=cur.fetchall()     # extract all friends' details in form of a tuple 
    return details

while True:            # this makes the program keep on running continuosly 
    if time_check():       # checks time and returns the control only when time is 12AM
        friends_details=retrieve_from_table()   # stores data of all friends 
        
        for onefriend_details in friends_details:    #checking one friend details at a time
            name,date,month,phno=onefriend_details     # unpacking tuple to get details
             
            if date_check(date,month):       # checks if today is the birthday of that friend
                print("Today is ",name,"'s birthday",sep="")  
                print("Wishing",name,"happy birthday...")
                
                driver=webdriver.Chrome("chromedriver") # accessing chromedriver for selenium 
                driver.get("https://wa.me/"+phno)      # loads the chat link using phone number
                time.sleep(1)             # sleeps for 1 second for complete loading of page
                
                driver.maximize_window() # maximizes browser window to click on 'OpenWhatsApp'
                time.sleep(1)       # sleeps for 1 second for completion of maximizng
                
                open_whatsapp_position=give_open_whatsapp_position() #'OpenWhatsApp' position
                py.click(open_whatsapp_position)    # clicks on button and opens whatsapp
                time.sleep(10)          # sleeps for 10 seconds for complete opening of the chat
                
                py.typewrite("Happy birthday...")   # types 'Happy Birthday' in the message box
                py.press("enter")     # presses enter for sending the message
                driver.quit()      # closes the web browser
                time.sleep(1)  # sleeps for 1 second for complete closing of browser
                print(name,"successfully wished happy birthday !","\n") 
                
        print("All done for today !")      # displaying for completion of all tasks that day
        print("Waiting for tomorrow...")
        time.sleep(86000)           # sleeps for 86000 seconds & start checking tomorrow