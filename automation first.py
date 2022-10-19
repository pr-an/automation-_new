from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='C:\\webdriver\\chromedriver.exe')
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3F%26ext_vrnc%3Dhi%26tag%3Dgooghydrabk1-21%26ref%3Dnav_signin%26adgrpid%3D60612964962%26hvpone%3D%26hvptwo%3D%26hvadid%3D486452179346%26hvpos%3D%26hvnetw%3Dg%26hvrand%3D4724291247435228510%26hvqmt%3De%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9062088%26hvtargid%3Dkwd-296458777401%26hydadcr%3D14454_2154375%26gclid%3DCjwKCAjwwL6aBhBlEiwADycBIL3WOXqQRi0oVz5RGQRgj0z9NGBqdtOwcEVQROVH9ash6cS-NtZ9URoCt6wQAvD_BwE&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
driver.maximize_window()

#login

driver.find_element(By.ID,"ap_email").send_keys("8600262131")
driver.find_element(By.ID,"continue").submit()
driver.find_element(By.ID,"ap_password").send_keys('Pran1555@')
driver.find_element(By.ID,'signInSubmit').submit()

driver.find_element(By.ID,'twotabsearchtextbox').send_keys("samsung galaxy S22 5g")
driver.find_element(By.ID,'nav-search-submit-button').submit()


