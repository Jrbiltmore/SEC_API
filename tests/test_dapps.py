
# /tests/test_dapps.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010125

import unittest
from selenium import webdriver

class TestDApps(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("file:///path/to/NextGenFinancialSystem/ethereum/dapps/PersonalFinanceDapp/index.html")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_dapp_title(self):
        self.assertEqual(self.driver.title, "Personal Finance DApp")

    def test_dapp_content(self):
        content = self.driver.find_element_by_id("app").text
        self.assertIn("Welcome to the Personal Finance DApp!", content)

if __name__ == "__main__":
    unittest.main()
