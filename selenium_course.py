from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #explicit wait
from selenium.webdriver.support import expected_conditions as EC #expected conditions for explicit wait
import time #time.sleep() for pause Before the next step


"""initialization of the web driver """
service_object= Service("C:\\Windows\\chromedriver.exe")
driver= webdriver.Chrome(service=service_object)

""" 1) application commands """

driver.get("Your Website Url") #driver.get() is used to open a website
time.sleep(5) #to pause the execution for 5 seconds, not a conditional command , just added for reference
driver.title() #driver.title() is used to get the title of the website
driver.current_url() #driver.current_url() is used to get the current url of the website
driver.page_source() #driver.page_source() is used to get the page source of the website
driver.maximize_window() #driver.maximize_window() is used to maximize the window of the website
driver.get_window_size #driver.get_window_size() is used to get the window size of the website
driver.set_window_size(1024, 768) #driver.set_window_size() is used to set the window size of the website
driver.delete_all_cookies() #driver.delete_all_cookies() is used to delete all the cookies of the website
driver.get_cookies() #driver.get_cookies() is used to get all the cookies of the website
driver.mobile_emulation() #driver.mobile_emulation() is used to emulate the mobile view of the website


"""2) conditional commands"""
searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']") # for conditional commands we have to store the element in a variable
searchbox.is_displayed() #searchbox.is_displayed() is used to check if the element is displayed on the website returns the boolean value
searchbox.is_enabled() #searchbox.is_enabled() is used to check if the element is enabled on the website returns the boolean value
searchbox.is_selected() #searchbox.is_selected() is used to check if the element is selected on the website returns the boolean value
                        # print("Enabled status:", searchbox.is_enabled())  # True
                        #is_selected() - for radio buttons and check boxes

"""3) click() and send_keys()"""                        
searchbox.send_keys("laptop") #searchbox.send_keys() is used to enter the text in the search box
searchbox.click() #searchbox.click() is used to click on the search box

"""4) browser commands and navigational commands"""
driver.close() #driver.close() is used to close the current browser
driver.quit() #driver.quit() is used to close all the browsers
driver.back() #driver.back() is used to go back to the previous page
driver.forward() #driver.forward() is used to go forward to the next page
driver.refresh() #driver.refresh() is used to refresh the page
driver.maximize_window() #driver.maximize_window() is used to maximize the window of the website
driver.get_window_size #driver.get_window_size() is used to get the window size of the website
driver.set_window_size(1024, 768) #driver.set_window_size() is used to set the window size of the website
driver.delete_all_cookies() #driver.delete_all_cookies() is used to delete all the cookies of the website
driver.get_cookies() #driver.get_cookies() is used to get all the cookies of the website
driver.mobile_emulation() #driver.mobile_emulation() is used to emulate the mobile view of the website

"""5) wait commands"""
driver.implicitly_wait(10) #driver.implicitly_wait() is used to wait for the element to load on the website, this remains active for all elements on the website coded after this command
wait = WebDriverWait(driver, 10) #wait = WebDriverWait(driver, 10) is used to wait for the element to load on the website, this remains 
element = wait.until(EC.presence_of_element_located((By.ID, "search"))) #element = wait.until(EC.presence_of_element_located((By.ID, "search"))) is used to wait for the element to load on the website, this remains active for the element coded after this command

#difference between implicitly_wait and WebDriverWait is that implicitly_wait is used for all the elements on the website coded after this command and WebDriverWait is used for a specific element coded after this command

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[4]/button[1]").click() #another way
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[4]/button[1]").send_keys("laptop") #another way
time.sleep(5)
driver.maximize_window()
driver.find_element(By.LINK_TEXT, " this is for a ref scenario which contains links ") # for images with links 
sliders=driver.find_elements(By.CLASS_NAME, "homeslider container") # no of sliders on a image 
links=driver.find_elements(By.TAG_NAME, "a") #no of links on a page 
print(len(sliders))
print(len(links))
#driver.close()
#driver.quit()
#driver.close() closes one browser at a time
 #driver.quit()   closes all browsers 

#css selector ( tag and id , tag and class , tag and attribute , tag , class and attribute)
driver.find_element(By.CSS_SELECTOR,"input#email")

#locators= id , name, linktext, classname , tagname
#Customized_locators= CSS Selector, Xpath and Xpath Axes


