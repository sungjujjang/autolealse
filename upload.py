from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time as ti

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
import time as ti

def upload(files, id, pw):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = uc.Chrome()
    driver.get("https://www.youtube.com/")
    wait = WebDriverWait(driver, 10)
    loginbtn = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')))
    loginbtn.click()
    ti.sleep(1)
    email = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    email.send_keys(id)
    emails = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
    emails.click()
    ti.sleep(5)
    password = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    password.send_keys(pw)
    passwords = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')
    passwords.click()
    ti.sleep(5)
    for file in files:
        createbtn = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button')
        createbtn.click()
        ti.sleep(0.2)

        uploadbtn = driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a')
        uploadbtn.click()

        uploadvideo = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/input')
        uploadvideo.send_keys(file)
        ti.sleep(10)

        nextbtn = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[1]/div[1]')
        nextbtn.click()

        nextbtns = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/ytcp-button-shape/button')
        nextbtns.click()

        ti.sleep(0.3)
        nextbtns = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/ytcp-button-shape/button')
        nextbtns.click()

        ti.sleep(0.3)
        nextbtns = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/ytcp-button-shape/button')
        nextbtns.click()

        ti.sleep(0.3)
        nextbtns = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[1]/div[1]')
        nextbtns.click()

        ti.sleep(0.3)
        nextbtns = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/ytcp-button-shape/button')
        nextbtns.click()
        ti.sleep(10)
        driver.get("https://www.youtube.com/")
        ti.sleep(3)


# upload([], "cxes0634@gmail.com", "victory6969!!")