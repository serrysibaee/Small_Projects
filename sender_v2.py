from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pynput.keyboard import Controller,Key
#pip install openpyxl
#pip install selenium
#pip install pynput

# Replace 'YOUR_CHROMEDRIVER_PATH' with the path to your ChromeDriver executable
driver = webdriver.Chrome('executable_path'=="C:\\Users\\serry\\Desktop\\chromedriver.exe")

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')
input('Scan the QR code and press Enter after WhatsApp Web is fully loaded: ')

# Replace 'YOUR_EXCEL_FILE_PATH' with the path to your Excel file
excel_file = openpyxl.load_workbook('C:\\Users\\serry\\Desktop\\WhatsApp Template.xlsx')
sheet = excel_file.active
keyboard = Controller()
def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

for row in sheet.iter_rows(min_row=2, values_only=True):
    name, phone_number, message = row

    # Formatting the message to include the receiver's name
    message = f"السلام عليكم {name}, {message}"

    # Compose the URL to open the chat with the contact
    url = f'https://web.whatsapp.com/send?phone={phone_number}&text={message}'

    # Open the chat with the contact
    driver.get(url)
    
    # Wait for some time to let the chat load
    sleep(5)
    #driver.find_element(By.XPATH, '//button[text()="Some text"]')

    # Find the input field and send the message
    #input_field = driver.find_element(By.XPATH,'')
    #input_field.send_keys(message)
    #input_field.send_keys(Keys.ENTER)
    sleep(2.5)
    enter()

    
    # Wait for a few seconds before sending the next message (to avoid rate limits)
    sleep(1.5)

# Close the browser window
driver.quit()


