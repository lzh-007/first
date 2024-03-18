from selenium import webdriver
from selenium.webdriver.chrome.service import Service as  ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#全自动安装驱动
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.baidu.com")