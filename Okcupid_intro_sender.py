from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class okcupid():

    def testmethod(self, username,password,intro):
        baseURL="https://www.okcupid.com/discover"
        likesyouURL ="https://www.okcupid.com/who-you-like?cf=likesIncoming"
        driver = webdriver.Firefox(executable_path="geckodriver.exe")

        #driver = webdriver.Firefox()
        driver.get(baseURL)
        wait = WebDriverWait(driver,100)
        fwait = WebDriverWait(driver, 5)
        mwait = WebDriverWait(driver, 300)
        driver.maximize_window()

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[id='username']")))
        user=driver.find_element_by_css_selector("input[id='username']")
        user.send_keys(username)

        Pass = driver.find_element_by_css_selector("input[id='password']")
        Pass.send_keys(password)

        login = driver.find_element_by_css_selector("body.spa.desktop.whitebg.secure.no_navbar.windows.firefox.logged_out.page--login:nth-child(2) div.OkModal.OkModal--scrollingoverlay.modal-appear-done.modal-enter-done div.FullscreenOverlay div.FullscreenOverlay-inner div.OkModalContent.reactmodal.signin-modal.login-modal.login-modal-icon-cross div.OkModalContent-main div.reactmodal-contents div.signin-modal-content div.login div.login-container div.loginscreen form.oknf.oknf--gray.login-form div.login-actions > button.login-actions-button:nth-child(1)")
        login.click()
        
        """
        #for liking
        i=0
        while i !=5 :
            a= "body.spa.desktop.whitebg.secure.windows.firefox.spotlight.logged_in.page--home.has_navbar:nth-child(2) div.page-section:nth-child(2) div.qm div.qm-inner div.qm-content-stackholder div.stackswap-appear-done.stackswap-enter-done div.qmstack div.qmcard div.qmcard-contents div.qmcard-top div.cardactions button.pill-button.likes-pill-button.doubletake-like-button:nth-child(2) > div.likes-pill-button-inner"
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, a)))
            elmsss3 = driver.find_element_by_css_selector(a)
            elmsss3.click()
        """
        accept_cookiie = driver.find_element_by_css_selector("button[id='onetrust-accept-btn-handler']")
        accept_cookiie.click()
        mwait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='navbar-link-text'][contains(text(),'Discover')]")))
        
        def newfunc():
            driver.get(likesyouURL)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[class='userthumb-img']")))
            first_image = driver.find_element_by_css_selector("img[class='userthumb-img']")
            first_image.click()

            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='profile-userinfo-buttons']//div[@class='profile-pill-buttons-button-inner']")))
            message = driver.find_element_by_xpath("//div[@class='profile-userinfo-buttons']//div[@class='profile-pill-buttons-button-inner']")
            message.click()
            try:
                fwait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[class='messenger-composer']")))
                typingtext = driver.find_element_by_css_selector("textarea[class='messenger-composer']")
                typingtext.send_keys(intro)
            except:
                cross=driver.find_element_by_xpath("//button[@class='messenger-user-row-close']//span[@class='icon i-close']")
                cross.click()
                fwait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='profile-userinfo-buttons']//span//div[@class='profile-pill-buttons']//button[@id='pass-button']//div[@class='pass-pill-button-inner'][contains(text(),'PASS')]")))
                unmatch = driver.find_element_by_xpath("//div[@class='profile-userinfo-buttons']//span//div[@class='profile-pill-buttons']//button[@id='pass-button']//div[@class='pass-pill-button-inner'][contains(text(),'PASS')]")
                unmatch.click()
                driver.close()
                ffg = okcupid()
                ffg.testmethod(jj, input_password, input_intro)
            sendingtext = driver.find_element_by_css_selector(".messenger-toolbar-send")
            sendingtext.click()
            cross = driver.find_element_by_css_selector(".connection-view-container-close-button > span:nth-child(1)")
            cross.click()

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[id='nav_ratings']")))

        
        i=0
        while i!=5 :
            newfunc()

input_email=input("Type your Email: ")
input_password=input("Type your Password: ")
input_intro=input("Type the intro you wanna send to people you already liked: ")

ff = okcupid()
ff.testmethod(username=input_email, password=input_password, intro=input_intro)



