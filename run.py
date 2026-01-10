from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from constants import ZOMATO_URL, OTP_WAIT_TIME, PHONE_NUMBER, EMAIL_ID
from testcases import CR04, CR05, CR03


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
driver.maximize_window()

try:
    driver.get(ZOMATO_URL)





    #Critical regression test case 3.
    #To run it, comment out test, result and run this file.

    # test = CR03(driver)  #Critical Regression Test Case - 03
    # result = test.run()
    
    
    
    
    
    
    # Critical regression test case 5.
    # To run it, comment out test, result and run run.py file.

    test = CR05(driver)
    result = test.run(phone_number=PHONE_NUMBER)
    
    
    
    
    
    
    
    #Critical regression test case 4.
    #To run it, comment out test, result and then if else block and run run.py file.
    
    # test = CR04(driver)

    # result = test.run_google_login_flow(timeout=OTP_WAIT_TIME)

    # if result:
    #     print("TEST CASE CR04 : PASS")
    # else:
    #     print("TEST CASE CR04 : FAIL")
    
    
    
    
    
    

   
    
    
    
    
    
    
    
    
    
except Exception as e:
    print(e)
    
    
    



finally:
    driver.quit()
