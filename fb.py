from selenium import webdriver
#importing webdriver from selenium

from webdriver_manager.chrome import ChromeDriverManager
#Implementation of chrome driver provide by selenium.webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
#instance of Firefox WebDriver is created.

driver.maximize_window()
#maximize the size of chrome browser window 

url="https://www.facebook.com"  #url for facebook
username=input("Enter your username\n")  #input username
password=input("Enter your password\n")	 #input password

driver.get(url) #The driver.get method will navigate to a page given by the URL. WebDriver will wait until the page has fully loaded. 


usernm = driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)	#input username gives to the username field of facebook login page via xpath 
code = driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)   ##input password gives to the password field of facebook login page via xpath 
login =driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()	#click on the Login button using xpath

print("\n------ LOGIN SUCCESSFULLY ------\n")  #after successfully login print statement executed

#driver.close() 
#after uncomment we can also close webdriver i.e. browser 


