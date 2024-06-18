import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading
from App import app


class TestUniquePathsUI(unittest.TestCase):
    driver = None
    server_thread = None

    @classmethod
    def setUpClass(cls):
        # Start the Flask server in a separate thread
        cls.server_thread = threading.Thread(target=app.run, kwargs={'debug': False, 'use_reloader': False})
        cls.server_thread.daemon = True
        cls.server_thread.start()

        # Give the server a moment to ensure it is running
        time.sleep(3)  # Increased sleep time

        # Initialize the WebDriver
        cls.driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed and in your PATH
        cls.driver.get("http://127.0.0.1:5000")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # Additional cleanup if necessary

    def setUp(self):
        # Per-test setup code
        pass

    def tearDown(self):
        # Per-test teardown code
        pass

    def test_calculate_unique_paths(self):
        driver = self.driver

        try:
            # Wait for the input elements to be present
            m_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "m"))
            )
            n_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "n"))
            )
        except Exception as e:
            driver.save_screenshot('screenshot_calculate_unique_paths.png')
            raise e

        m_input.clear()
        n_input.clear()

        m_input.send_keys("3")
        n_input.send_keys("7")
        n_input.send_keys(Keys.RETURN)

        try:
            # Wait for the result to be rendered
            result = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "h2"))
            ).text
            self.assertIn("Number of unique paths: 28", result)
        except Exception as e:
            driver.save_screenshot('screenshot_calculate_unique_paths_result.png')
            raise e

    def test_invalid_input(self):
        driver = self.driver

        try:
            # Wait for the input elements to be present
            m_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "m"))
            )
            n_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "n"))
            )
        except Exception as e:
            driver.save_screenshot('screenshot_invalid_input.png')
            raise e

        m_input.clear()
        n_input.clear()

        m_input.send_keys("0")
        n_input.send_keys("100")
        n_input.send_keys(Keys.RETURN)

        # Wait for any potential error to be handled
        time.sleep(1)

    def test_empty_input(self):
        driver = self.driver

        try:
            # Wait for the input elements to be present
            m_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "m"))
            )
            n_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "n"))
            )
        except Exception as e:
            driver.save_screenshot('screenshot_empty_input.png')
            raise e

        m_input.clear()
        n_input.clear()

        n_input.send_keys(Keys.RETURN)

        # Wait for any potential error to be handled
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
