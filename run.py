from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from constants import ZOMATO_URL, OTP_WAIT_TIME, PHONE_NUMBER
from testcases import CR04, CR05, CR03


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
driver.maximize_window()

try:
    driver.get(ZOMATO_URL)

    # test = CR04(driver)

    # result = test.run_google_login_flow(timeout=OTP_WAIT_TIME)

    # if result:
    #     print("TEST CASE CR04 : PASS")
    # else:
    #     print("TEST CASE CR04 : FAIL")

    # test = CR05(driver)

    # result = test.run(phone_number=PHONE_NUMBER)

    # if result:
    #     print("TEST CASE CB05 : PASS")
    # else:
    #     print("TEST CASE CB05 : FAIL")
    
    
    
    
    
    
    
    
    test = CR03(driver)  #Critical Regression Test Case - 03
    result = test.run()
    
except Exception as e:
    print(e)
    
    
    



finally:
    driver.quit()
