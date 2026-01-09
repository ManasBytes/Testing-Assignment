from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CR05:
   

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def run(self, phone_number):
        banner = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(text(),'Online ordering is only supported')]"
                )
            )
        )
        banner.click()

        phone_input = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//input[@placeholder='type here...']"
                )
            )
        )
        phone_input.send_keys(phone_number)
        share_btn = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//span[text()='Share App Link']"
                )
            )
        )
        share_btn.click()

        time.sleep(2)

        print("APP LINK SHARE FLOW TRIGGERED SUCCESSFULLY")
        return True
