import sys
import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


# baca file json
def read_credentials():
    secrets = 'secrets.json'
    with open(secrets) as f:
        keys = json.loads(f.read())
        return keys


class SIMkuliah:
    # prepare data
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.base_url = "https://ecampus.pelitabangsa.ac.id/pb/ecampus.jsp"
        # self.driver = webdriver.Chrome("E:\chromedriver.exe") # for cache
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.COMMAND_OR_CONTROL = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL

    # session 1
    def single_interation_over_session(self):
        self.login_to_simkuliah()
        time.sleep(5)
        self.driver.quit()

    # login and absen
    def login_to_simkuliah(self):
        self.driver.get(self.base_url)
        self.put_credentials_to_form()
        self.get_to_absen_simkuliah()

    # input data
    def put_credentials_to_form(self):
        try:
            # Enter user credentials and Click on Submit button to Logins
            self.driver.find_element_by_name("username").send_keys(self.login)
            time.sleep(2)
            password_field = self.driver.find_element_by_name("password")
            password_field.send_keys(self.password)
            password_field.submit()
            time.sleep(3)

        except NoSuchElementException:
            print("Exception NoSuchElementException")

    # click absen
    def get_to_absen_simkuliah(self):
        try:
            element = self.driver.find_element_by_xpath(
                "//*[@id='konfirmasi-kehadiran']")
            element.click()
            time.sleep(1)
            konfirm = self.driver.find_element_by_xpath(
                "//*[@class='confirm']")
            konfirm.click()
            time.sleep(2)
            print("Anda sudah Absen")
        except NoSuchElementException:
            print("Absen Belum ada")


if __name__ == '__main__':
    credentials = read_credentials()
    bot = SIMkuliah(credentials.get('username'),
                    credentials.get('password'))
    bot.single_interation_over_session()
