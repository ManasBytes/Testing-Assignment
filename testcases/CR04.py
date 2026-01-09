import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CR04:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_login(self):
        login_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[text()='Log in']")
            )
        )
        login_btn.click()

    def click_google_login(self):
        """
        Best-effort click on Google login.
        Actual authentication is MANUAL.
        """
        google_btn = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'nsm7Bb-HzV7m-LgbsSe-bN97Pc')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            google_btn
        )
        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            google_btn
        )

    def wait_for_manual_login_and_verify(self, timeout=120):
        """
        Waits for the USER to complete login manually
        and verifies successful login on Zomato.
        """
        print("Waiting for manual login...")

        start = time.time()
        while time.time() - start < timeout:
            try:
                # Logged-in state: Login button disappears
                self.driver.find_element(
                    By.XPATH,
                    "//a[text()='Log in']"
                )
                time.sleep(2)
            except:
                print("LOGIN SUCCESSFUL")
                return True

        print("LOGIN FAILED / TIMEOUT")
        return False

    def run_google_login_flow(self, timeout=120):
        self.open_login()
        self.click_google_login()
        return self.wait_for_manual_login_and_verify(timeout)
