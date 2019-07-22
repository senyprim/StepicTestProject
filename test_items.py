import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver



def test_exist_btn_add_to_basket(browser):
    lang=browser.execute_script("return navigator.language || navigator.userLanguage")
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    try:
        WebDriverWait(browser,7).until(EC.presence_of_element_located((By.CSS_SELECTOR,".btn-add-to-baskett")))
        assert True
    except:
        assert False,f'Кнопка "добавить в корзину"" отсутствует на странице. Browser={browser.capabilities["browserName"]} Language={lang}'



