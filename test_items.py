from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_basket_should_be_on_the_page(browser):
    browser.get(link)
    #time.sleep(3)
    assert browser.find_element(By.CLASS_NAME, 'btn-add-to-basket'), 'На сайте с заданным языком кнопка Добавления товара в корзину упущена'