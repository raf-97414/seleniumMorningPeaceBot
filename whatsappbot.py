from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#input("Scan QR code then press enter")
def setup_driver(): #helps you create new driver sessions to save you and your friends life if needed
   driver = webdriver.Chrome()
   driver.get("https://web.whatsapp.com")
   return driver

def good_morning(driver, phone_no, message): #the actual action takes place here
   textbox = driver.find_element("xpath","//div[@aria-label='Search']") #searches for the receiver by phone number
   textbox.clear()
   textbox.send_keys(phone_no) #add the phone number in the search bar
   textbox.send_keys(Keys.ENTER) #used to click on enter

   time.sleep(10) #waits for the search to load results

   textbox.find_element("xpath","//div[@class='x10l6tqk xh8yej3 x1g42fcv']") #finds the receiver
   textbox.click() #clicks on the receiver tile

   time.sleep(10) #waits to open the chat

   #Finds the chatbox and sends the message to the receiver
   messagebox = driver.find_element("xpath","//div[@aria-placeholder='Type a message']/p[@class='selectable-text copyable-text x15bjb6t x1n2onr6']")
   messagebox.send_keys(message)
   messagebox.send_keys(Keys.ENTER)
   time.sleep(10) #waits for some time before closing the session
   print("Message successfully sent !!") #helps you determine if your messsage is sent

if __name__=='__main__':
   julie_phone = "+1111111111" #because Julie's cause drama no offence edit the phone number to the one that belongs to the drama bomb dropper of your life
   #For your
   driver_me = setup_driver() #opens up a chrome webdriver for you
   input("Scan QR code then press Enter") #waits till you log in by scanning qr code and once done you'll have to press enter
   good_morning(driver_me,julie_phone,"Good Morning :)") #let the code do the rest ..... edit the message
   driver_me.quit()
   #To save your friend's or sibling's life too if sending to the same person
   #if different person than remove the hash out of julie_phone2 and edit the phone number
   #julie_phone2 = "+1111111111"
   #driver_friend = setup_driver()
   #input("Scan QR code then press Enter")
   #good_morning(driver_friend,julie_phone,"Good Morning :)")
   #driver_friend.quit()





