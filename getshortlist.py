from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time as ti

def get_list(gesu, base_url):
    shortlist = []
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(base_url)
    for i in range(1, gesu+1):
        wait = WebDriverWait(driver, 100)
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='다음 동영상']")))
        next_button.click()
        ti.sleep(2)
        next_video_url = driver.current_url
        shortlist.append(next_video_url)
        print(f"Next video URL: {next_video_url}")
    driver.quit()
    return shortlist

# print(get_list(20, "https://www.youtube.com/shorts/AD7iJY0HEQI"))