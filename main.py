from bs4 import BeautifulSoup
import requests
import smtplib

MY_EMAIL = "Your email"
PASSWORD = "Your Password"
email = "your sending email"

url = "https://www.amazon.in/gp/product/1861972784/ref=ox_sc_saved_image_7?smid=A1WYWER0W24N8S&psc=1"
headers = {
    "Accept-Language": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;"
                       "q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36 Avast/114.0.21608.199"
}
response = requests.get(url=url, headers=headers)
data = response.text

soup = BeautifulSoup(data, "html.parser")
price = soup.find(name="span", id="price")
product = soup.find(name="span", id="productTitle").getText()
actual_price = price.getText()
actual_price = actual_price.replace('₹', '')
actual_price = float(actual_price)
if actual_price <= 564:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=email,
                            msg=f"Subject: Price Drop Alert.\n\n {product} is available in less amount.\n Tap a link"
                                f" .\n {url}.")


