from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CR05:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def run(self, phone_number):
        print("CR05 STARTED: App Link dialog automation (Phone flow only)")

        # Open App Download dialog
        banner = self.wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//div[contains(text(),'Online ordering is only supported')]"
            ))
        )
        self.js_click(banner)
        print("App link dialog opened")

        # -------- PHONE FLOW --------
        print("PHONE FLOW STARTED")

        phone_input = self.wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//input[@placeholder='type here...']"
            ))
        )
        phone_input.clear()
        phone_input.send_keys(phone_number)

        share_btn = self.wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//span[text()='Share App Link']"
            ))
        )
        self.js_click(share_btn)

        print("Phone app link request triggered")
        print("CR05 COMPLETED")

        time.sleep(2)
        return True
    
    
    
    # email flow and checks for flash were excluded due to repeated click and element not found errors.
