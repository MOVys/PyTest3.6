import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
# Встроенная функция pytest_addoption для захвата из консоли параметра окружения, у нас '--language'
    parser.addoption('--language', action='store', default='ru', help='Choose language')


@pytest.fixture(scope='function')
# Встроенная фикстура request 
def browser(request):
    language_user = request.config.getoption('language')
    options = Options()
# Класс Options и метод add_experimental_option. Передаем Браузеру с каким языком запускать
    options.add_experimental_option('prefs', {'intl.accept_languages': language_user})
    print('\nstart browser...')
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nquit browser...')
    browser.quit()
 