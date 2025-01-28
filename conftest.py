import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
добавляем возможность считывания параметра языка из командной строки
'''
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, es, fr, etc.")


''' 
фикстура для инициализации браузера с введенным пользователем языком и закрытия браузера
'''
@pytest.fixture(scope="function")
def browser(request):
    
    language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option(
    'prefs', {'intl.accept_languages': language})
    
    browser = webdriver.Chrome(options=options)
    
    yield browser
    
    print("\nquit browser..")
    browser.quit()