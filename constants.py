from dotenv import load_dotenv

load_dotenv()
import os

ZOMATO_URL = "https://www.zomato.com/bangalore/dominos-pizza-shanti-nagar/order"

EMAIL_ID = os.environ.get("EMAIL")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")

OTP_WAIT_TIME = 360  # seconds


