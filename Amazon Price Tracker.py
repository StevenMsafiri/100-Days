import requests
from bs4 import BeautifulSoup
import  smtplib

# URL of the Amazon product page
url = "https://www.amazon.com/OnePlus-Smartphone-Unlocked-co-Developed-Hasselblad/dp/B09S8BV4D9/ref=sr_1_3?crid=3QT5W6ZNKL9GC&dib=eyJ2IjoiMSJ9.bVh8yw7eXZZxmPel2V1aS1xNjm2x1KA5NUG5NGKKuD5a3bxiNT-hbtwmR6yTv5E6Fc52f0wryiG28IP6Jp2xpedoj0DJAHccRX6Kfm1QlsvwU-s5tw3FFNBGma3DVmFualGtjIKsgY-8LYD_427ruJw36i7iJL2X_fEuDGj9jTXPDoaNiOn2sA3lSnKKVWmmiNxvddMN4TsXd3r8KBZHRtQfywIc39LMMnilDIj_efo.TLr6TUeB1ms7MEwAv3QigzG4ojPq0mwvtmAPZkYYbOg&dib_tag=se&keywords=oneplus%2B10%2Bpro&qid=1729594265&sprefix=oneplus%2B10%2Bpro%2Caps%2C397&sr=8-3&th=1"

# Set user agent to mimic a browser request
headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0",
           "Accept-Language": "en-US,en;q=0.9,en;q=0.8"
           }

# Send a GET request
response = requests.get(url, headers=headers)

# Parse HTML content
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

# Extract specific data (e.g., product title)
price = int(soup.find(class_="a-price-whole").get_text().strip("."))
# print(price)
# print(type(price))

while price < 380:

    email = smtplib.SMTP(host="smtp.gmail.com", port=587)
    email.starttls()

    email.login(user="ianleonardmk47@gmail.com", password="vbwtuxcedgdtfozi")

    email.sendmail(from_addr="ianleonardmk47@gmail.com", to_addrs="stevenmsafir@gmail.com",
                   msg=f"Subject:The price is {price}\n"
                       f"Buy now"
                   )
    email.quit()
