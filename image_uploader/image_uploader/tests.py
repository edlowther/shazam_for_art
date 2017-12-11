from django.test import TestCase
import pytest
from splinter import Browser
import time
# Create your tests here.

@pytest.fixture()
def browser():
    browser = Browser()
    yield browser
    browser.quit()

def test_upload_picture_test_present(browser):
    browser.visit('http://127.0.0.1:8000/images/')
    assert browser.is_text_present('Upload picture')

def test_upload_picture_button_seems_to_work(browser):
    browser.visit('http://127.0.0.1:8000/images')
    button = browser.find_by_name('upload')
    button.click()
    assert browser.is_text_present('Picture uploaded successfully')

# time.sleep(3)
# browser.quit()
