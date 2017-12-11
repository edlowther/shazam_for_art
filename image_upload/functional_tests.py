from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:4567/upload')

        self.assertIn('Picture', self.browser.title)
        # self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away
        # [...rest of comments as before]

if __name__ == '__main__':
    unittest.main(warnings='ignore')


# browser = webdriver.Firefox()
# browser.get('http://localhost:4567/upload')
#
# assert 'Picture' in browser.title
