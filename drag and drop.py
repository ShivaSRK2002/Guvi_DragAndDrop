from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.action_chains import ActionChains

# Define the path to chromedriver
paths = r"C:\Users\shiva\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
# Configure Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
# Allow time for the driver to initialize
time.sleep(2)
# Maximize the browser window
driver.maximize_window()
# Open the target URL
driver.get("https://jqueryui.com/droppable/")
# Allow time for the page to load
time.sleep(2)
# Switch to the frame containing the draggable and droppable eleme
driver.switch_to.frame(0)
# Locate the source and destination elements
source = driver.find_element(By.ID,"draggable")
destination = driver.find_element(By.ID,"droppable")
# Allow time for elements to be located
time.sleep(2)
# Initialize ActionChains
actions = ActionChains(driver)
time.sleep(2)
# Perform the drag-and-drop action
actions. drag_and_drop(source,destination)
actions. perform()
time. sleep(5)
# Close the browser
driver.close()