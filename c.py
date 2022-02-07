from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from time import sleep
from easygui import *
from datetime import datetime

## Sets up driver
##options = webdriver.ChromeOptions()
##prefs = {"profile.default_content_setting_values.notifications" : 2}
##options.add_experimental_option("prefs",prefs)
###options.add_argument('headless')               USE THESE SETTINGS
###options.add_argument('window-size=1920x1080')  USE THESE SETTINGS
##driver = webdriver.Chrome(options=options)
##driver.set_page_load_timeout(30)
##driver.maximize_window()  TESTING ONLY


#driver.get("https://fc-not-app01:8637/VisionRecipe")
delay = 3

## CSS attributes
block = "block"

## Input fields for GUI
standard_quantity = "10"
code = "WIP04499" # WIP04499 # BRANSTON001
today = datetime.today()
date = today.strftime("%d/%m/%Y")
time = "12:00 PM"
number_of_orders = "1"

def input_details(): ## Build GUI input
    text = "Enter the following details"
    title = "Vision Manufacturing Job Fast Input"
    input_list = ["Prodcut Code", "Standard Quantity", "Date","Time", "Number of Orders","Username","Password"]
    default_list = ["WIP04499", "100",date,time,"1","HOsborn", "Password"]
    output = multpasswordbox(text, title, input_list, default_list)
    username = output[5]
    return username

def input_user_log_in_details(username,password):
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[aria-describedby=Username]"))).send_keys(username)
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Password']"))).send_keys(password)
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,"//button[text()='Login']"))).click()

    
def navigate_to_inputs():
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,"//*[@id='navbarTogglerDemo02']/ul/li[2]"))).click()
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,"//*[@id='navbarTogglerDemo02']/ul/li[2]/ul/li[1]"))).click()
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,"//a[contains(text(),'Manufacturing')]"))).click()
    sleep(0.2) ## Search is slow

def input_prodcut_code(code):
    driver.find_element(By.ID,'PageSearch_Code').send_keys(code)
    sleep(2)   ### Javascript runs slow
    driver.find_element(By.CLASS_NAME,'SelectProduct').click()
    sleep(0.2) ### Lightbox closing has animation
    
def input_standard_quantity(standard_quantity):
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.ID,'StandardQuantity'))).clear()
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.ID,'StandardQuantity'))).send_keys(standard_quantity)
    print (f"(****STANDARD QUANTITY SET TO [{standard_quantity}] ****)")
    
def units_of_measure():
    try:
        temp = Select(driver.find_element(By.ID,'ddlUOMs'))
        grab_uom = temp.first_selected_option
    except:
        print (f"(****UOM NOT SET FOR [{code}]****)")
    else:
        temp = grab_uom.text
        print (f"(****UOM SET TO [{temp}] for [{code}]****)")

def specify_process():
    try:
        temp = Select(driver.find_element(By.ID,'ddlProcesses'))
        grab_sp = temp.first_selected_option
    except:
        print (f"(****PROCESS NOT SPECIFIED FOR [{code}]****)")
    else:
        temp = grab_sp.text
        print (f"(****PROCESS SPECIFIED TO [{temp}] for [{code}]****)")
        
def input_date():
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.ID,'ToBeSampledDate'))).clear()
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.ID,'ToBeSampledDate'))).send_keys(date)
    print (f"(****DATE SET TO [{date}] ****")

def input_number_of_orders():
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.ID,'inputNumberOfOrders'))).clear()
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.ID,'inputNumberOfOrders'))).send_keys(number_of_orders)
    print (f"(****QUANTITY SET TO [{number_of_orders}]****)")

def quantity_by():
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.ID,'inputNumberOfOrders'))).clear()

def push_order():
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.ID,'btnCreateOrder'))).click()

def check_warnings():
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.ID,'Warnings-tab'))).click()
    container1 = driver.find_elements(By.ID,'JobStatusOkWithWarnings')
    
    for items in container1:
        mytext = items.find_element(By.XPATH,"//*[@id='JobStatusOkWithWarnings']")
        print (mytext.text)

def display_output():
    ## message / information to be displayed on the screen
    message = "The following jobs have been successfully processed:"
    title = "Job Completion Summary"
    ok_btn_txt = "Continue"
    output = msgbox(message, title, ok_btn_txt)
    
def wrong_password_username(username):
    message = (f"The username ({username}) or password you supplied is incorrect, please re-enter or press cancel")
    title = "Error"
    output = ccbox(message, title)
    if output:
        input_details()
    else:
        sys.exit()

username = input_details()
wrong_password_username(username)
#navigate_to_inputs()
##input_prodcut_code(code)
##units_of_measure() ### Checks UOM is set
##input_standard_quantity(standard_quantity)
##specify_process()
##input_date()
##input_number_of_orders()
##push_order()
##check_warnings()
display_output()

