from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class okcupid():

    def testmethod(self, username,password):
        baseURL="https://www.okcupid.com/discover"
        likesyouURL ="https://www.okcupid.com/who-you-like?cf=likesIncoming"

        driver = webdriver.Firefox(executable_path="geckodriver.exe")
        #driver = webdriver.Firefox()
        
        driver.get(baseURL)
        wait = WebDriverWait(driver,100)
        mwait = WebDriverWait(driver,300)
        driver.maximize_window()

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[id='username']")))
        user=driver.find_element_by_css_selector("input[id='username']")
        user.send_keys(username)

        Pass = driver.find_element_by_css_selector("input[id='password']")
        Pass.send_keys(password)

        login = driver.find_element_by_css_selector("body.spa.desktop.whitebg.secure.no_navbar.windows.firefox.logged_out.page--login:nth-child(2) div.OkModal.OkModal--scrollingoverlay.modal-appear-done.modal-enter-done div.FullscreenOverlay div.FullscreenOverlay-inner div.OkModalContent.reactmodal.signin-modal.login-modal.login-modal-icon-cross div.OkModalContent-main div.reactmodal-contents div.signin-modal-content div.login div.login-container div.loginscreen form.oknf.oknf--gray.login-form div.login-actions > button.login-actions-button:nth-child(1)")
        login.click()
        accept_cookiie = driver.find_element_by_css_selector("button[id='onetrust-accept-btn-handler']")
        accept_cookiie.click()
        mwait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='navbar-link-text'][contains(text(),'Discover')]")))
        #for liking
        i=0
        while i !=5 :
            a= "body.spa.desktop.whitebg.secure.windows.firefox.spotlight.logged_in.page--home.has_navbar:nth-child(2) div.page-section:nth-child(2) div.qm div.qm-inner div.qm-content-stackholder div.stackswap-appear-done.stackswap-enter-done div.qmstack div.qmcard div.qmcard-contents div.qmcard-top div.cardactions button.pill-button.likes-pill-button.doubletake-like-button:nth-child(2) > div.likes-pill-button-inner"
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, a)))
            liker = driver.find_element_by_css_selector(a)
            liker.click()

input_email=input("Type your Email: ")
input_password=input("Type your Password: ")
#input_intro=input("Type the intro you wanna send to people you already liked: ")

ff = okcupid()
ff.testmethod(username=input_email, password=input_password)



