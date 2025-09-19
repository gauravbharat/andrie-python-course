from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

chrome_browser = webdriver.Chrome()
try:
    chrome_browser.get('https://gaurav-r6ci.onrender.com/contact.html')
    wait = WebDriverWait(chrome_browser, timeout=6)
    wait.until(lambda _: 'Contact - Gaurav Mendse' == chrome_browser.title)

    assert 'Contact - Gaurav Mendse' == chrome_browser.title
    print(f'Title "{chrome_browser.title}" assertion passed')

    form = chrome_browser.find_element(By.CLASS_NAME, 'reveal-content')
    print(f'Form handle passed')

    email = chrome_browser.find_element(By.NAME, 'email')
    email.send_keys('pgmendse@gmail.com')
    print(f'email field set')
    subject = chrome_browser.find_element(By.NAME, 'subject')
    subject.send_keys('Final automation test')
    print(f'subject field set')
    message = chrome_browser.find_element(By.NAME, 'message')
    message.send_keys('Testing automated contact form submission from automation.py using Selenium.')
    print(f'message field set')

    send_button = form.find_element(By.TAG_NAME, 'button')
    send_button.click()
    # assert 'Send' == send_button.get_attribute('innerHTML')
    print(f'Send button clicked')

    assert 'Thank you - Gaurav Mendse' == chrome_browser.title
    print(f'Post form submission title "{chrome_browser.title}" assertion passed')

except NoSuchElementException as nsee:
    print(f'Element not found: {nsee}')
finally:
    chrome_browser.quit()

