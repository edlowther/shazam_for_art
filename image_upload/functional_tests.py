from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:4567/upload')

assert 'Picture' in browser.title
