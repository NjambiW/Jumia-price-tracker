import requests
from bs4 import BeautifulSoup
import smtplib
import os

new_url ="https://www.jumia.co.ke/catalog/?q=oraimo+earbuds"
MY_EMAIL = os.environ.get("my_email")
PASSWORD =  os.environ.get("password")
recipient_mail =  os.environ.get("recipient_mail")
MY_PRICE = int(input("Enter the amount you prefer buying with:\n"))

response = requests.get(new_url)
data = response.text

soup = BeautifulSoup(data, "html.parser")
price = soup.find(name="div", class_="prc").getText().split("KSh")[1]
price_as_int = price.replace(",", "")
if float(price_as_int) < MY_PRICE:
    new_price = price
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            MY_EMAIL,
            recipient_mail,
            msg=f"PRICE DROP\n\nThere is a price drop in your bookmarked product to KSH {price}")
