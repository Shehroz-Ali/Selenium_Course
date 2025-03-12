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


"""locators= id , name, linktext, classname , tagname"""
driver.find_element(By.ID, "username")      #driver.find_element(By.ID, " ") is used to find the element by id
                                            #html code syntax: <input id="username" name="username" type="text"> 
driver.find_element(By.NAME, "username")    #driver.find_element(By.NAME, "text ") is used to find the element by name
                                            #html code syntax: <input id="username" name="username" type="text">
driver.find_element(By.LINK_TEXT, "Sign in")#driver.find_element(By.LINK_TEXT, "text") is used to find the element by link text
                                            #html code syntax: <a href="https://www.google.com">Sign in</a>
driver.find_element(By.CLASS_NAME, "text")  #driver.find_element(By.CLASS_NAME, "text ") is used to find the element by class name
                                            #html code syntax: <p class="text">text</p>
driver.find_element(By.TAG_NAME, "p")       #driver.find_element(By.TAG_NAME, "text ") is used to find the element by tag name
                                            #html code syntax: <p>text</p>

"""Customized locators= CSS Selector, Xpath and Xpath Axes"""\
""" 1) CSS Selector"""
# 1️⃣ Tag + ID Selector
# 📝 Corresponding HTML:
# <input type="text" id="username" placeholder="Enter username">
# Selects an input field with the ID "username" and enters text.
driver.find_element(By.CSS_SELECTOR, "input#username").send_keys("admin")

# 2️⃣ Tag + Class Selector
# 📝 Corresponding HTML:
# <button class="submit-btn">Submit</button>
# Selects a button with class "submit-btn" and clicks it.
driver.find_element(By.CSS_SELECTOR, "button.submit-btn").click()

# 3️⃣ Tag + Attribute Selector
# 📝 Corresponding HTML:
# <input type="email" name="email" placeholder="Enter your email">
# Selects an input field with name="email" and enters an email address.
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("test@example.com")

# 4️⃣ Tag + Class + Attribute Selector
# 📝 Corresponding HTML:
# <input class="form-control" type="text" name="search" placeholder="Search...">
# Selects an input field with class="form-control" and type="text", then enters text.
driver.find_element(By.CSS_SELECTOR, "input.form-control[type='text']")

# 5️⃣ Tag + Multiple Classes Selector
# 📝 Corresponding HTML:
# <button class="btn primary-btn">Click Me</button>
# Selects a button with both "btn" and "primary-btn" classes and clicks it.
driver.find_element(By.CSS_SELECTOR, "button.btn.primary-btn")

"""2) Xpath"""
# 1️⃣ Absolute XPath (Not Recommended)
# 📝 Corresponding HTML:
# <html>
#   <body>
#     <div>
#       <form id="loginForm">
#         <input type="text" id="username" name="username" placeholder="Enter Username">
# Selects the username input field using the full path
driver.find_element(By.XPATH, "/html/body/div/form/input").send_keys("admin")

# 2️⃣ Relative XPath (Recommended)
# 📝 Corresponding HTML:
# <input type="text" id="username" name="username" placeholder="Enter Username">
# Selects the username input field using its ID (More reliable)
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("admin")

# 3️⃣ XPath using Contains Function
# 📝 Corresponding HTML:
# <button class="btn primary-btn">Submit</button>
# Selects a button where class contains "primary"
driver.find_element(By.XPATH, "//button[contains(@class, 'primary')]").click()

# 4️⃣ XPath using Starts-With Function
# 📝 Corresponding HTML:
# <input type="email" name="emailAddress" placeholder="Enter Email">
# Selects an input field where the name starts with "email"
driver.find_element(By.XPATH, "//input[starts-with(@name, 'email')]")

# 5️⃣ XPath using Text Function
# 📝 Corresponding HTML:
# <a href="#">Forgot Password?</a>
# Selects an anchor tag using its text
driver.find_element(By.XPATH, "//a[text()='Forgot Password?']")

# 6️⃣ XPath using Logical Operators
# 📝 Corresponding HTML:
# <input type="text" id="username" name="username" placeholder="Enter Username">
# Selects the username input field using the "and" operator
driver.find_element(By.XPATH, "//input[@id='username' and @name='username']")
#if 3 conditions are there then use "and" operator
driver.find_element(By.XPATH, "//input[@id='username' and @name='username' and @type='text']")
