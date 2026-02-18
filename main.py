from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "html.parser")


price = soup.select_one("#priceblock_ourprice, #priceblock_dealprice, .a-price .a-offscreen").get_text()
price_cleaned = price.replace("₹", "").replace("INR", "").replace(",", "").strip()
price_as_float = float(price_cleaned)


title = soup.find(id="productTitle").get_text().strip()


BUY_Price = 10000

if price_as_float < BUY_Price:
    message = f"{title} is on sale for {price}"

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port = 587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr = os.environ["EMAIL_ADDRESS"],
            to_addrs = "faizzhsnn@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )

    print("Done")