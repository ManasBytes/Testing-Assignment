from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time   

class CR03:
    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    def run(self):
        print("CR03: Test execution started.")

        try:
            
            # STEP 1: Verify restaurant is CLOSED
            
            closed_badge = self.waiter.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(normalize-space(),'Closed')]")
                )
            )

            if not closed_badge.is_displayed():
                print("CR03: Restaurant is not closed. Test not applicable.")
                return False

            print("CR03: Closed status detected.")
            time.sleep(1)

            
            # STEP 2: Verify opening time is displayed
            
            opening_time = self.waiter.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(text(),'Opens')]")
                )
            )

            print(f"CR03: Opening time shown -> {opening_time.text}")

            
            # STEP 3: Verify page title
            
            if self.driver.title.strip():
                print("CR03: Title Test Passed.")
            else:
                print("CR03: Title Test Failed.")
                return False

            
            # STEP 4: Verify core menu container exists
            
            self.waiter.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//h4[contains(text(),\"Today's Exclusive Dishes\")]")
                )
            )

            print("CR03: Core menu container is visible.")

            
            # STEP 5: Verify menu items are visible
            
            menu_items = self.driver.find_elements(
                By.XPATH, "//h4[contains(@class,'sc-cdQEHs')]"
            )

            if len(menu_items) > 0:
                print(f"CR03: Menu items visible -> {len(menu_items)} items found.")
                time.sleep(1)
            else:
                print("CR03: No menu items visible.")
                return False

            
            # STEP 6: Validate all restaurant tabs load correctly
            
            print("CR03: Starting tab navigation validation.")

            tabs = {
                "Order Online": "https://www.zomato.com/bangalore/dominos-pizza-shanti-nagar/order",
                "Overview": "https://www.zomato.com/bangalore/dominos-pizza-shanti-nagar",
                "Reviews": "https://www.zomato.com/bangalore/dominos-pizza-shanti-nagar/reviews",
                "Photos": "https://www.zomato.com/bangalore/dominos-pizza-shanti-nagar/photos",
                "Menu": "https://www.zomato.com/bangalore/dominos-pizza-shanti-nagar/menu",
            }

            page_anchors = {
                "Order Online": "//span[contains(normalize-space(),'Closed')]",
                "Overview": "//h1 | //h2",
                "Reviews": "//h2[contains(text(),'Reviews')] | //div[contains(text(),'Reviews')]",
                "Photos": "//img | //h2[contains(text(),'Photos')]",
                "Menu": "//h4 | //div[contains(text(),'Menu')]",
            }

            for tab_name, tab_url in tabs.items():
                try:
                    self.driver.get(tab_url)

                    self.waiter.until(
                        EC.presence_of_element_located(
                            (By.XPATH, page_anchors[tab_name])
                        )
                    )

                    print(f"CR03: {tab_name} page loaded successfully. Test Passed.")
                    time.sleep(1)
                    

                except TimeoutException:
                    print(f"CR03: {tab_name} page failed to load. Test Failed.")
                    return False

            print("CR03: All restaurant tabs loaded successfully.")
            
            
            # STEP 7: Scroll Order Online page to bottom and verify stability
            
            print("CR03: Navigating back to Order Online page for scroll stability check.")

            order_online_url = "https://www.zomato.com/bangalore/dominos-pizza-shanti-nagar/order"
            self.driver.get(order_online_url)

            # Wait for page to load again
            self.waiter.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(normalize-space(),'Closed')]")
                )
            )

            print("CR03: Order Online page loaded. Starting scroll.")

            # Get initial page height
            last_height = self.driver.execute_script("return document.body.scrollHeight")

            while True:
                # Scroll to bottom
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                
                
                time.sleep(2)

                # Small wait for lazy-loaded content
                self.waiter.until(lambda d: True)

                new_height = self.driver.execute_script("return document.body.scrollHeight")

                if new_height == last_height:
                    break

                last_height = new_height

            print("CR03: Reached bottom of Order Online page.")

            # Verify page did not break after scrolling
            try:
                self.waiter.until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//footer | //div[contains(@class,'footer')]")
                    )
                )
                print("CR03: Footer visible. No page break detected.")
                time.sleep(3)
            except TimeoutException:
                print("CR03: Footer not found after scroll. Possible page break.")
                return False

            
            
            
            
            
            
            print("CR03: Test completed successfully.")
            return True

        except TimeoutException:
            print("CR03: Timeout occurred while validating elements.")
            return False

        except Exception as e:
            print(f"CR03: Unexpected error -> {e}")
            return False
