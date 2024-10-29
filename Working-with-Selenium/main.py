from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Initialize WebDriver with ChromeDriver
options = webdriver.ChromeOptions()
options.binary_location = "/snap/bin/chromium"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.amazon.com")
driver.quit()