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
    assert browser.is_text_present('Upload Picture')

# time.sleep(3)
# browser.quit()
