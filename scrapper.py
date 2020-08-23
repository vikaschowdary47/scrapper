import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/LG-UltraWide-Inch-WFHD-Display/dp/B08CF4LZT1/ref=pd_sbs_147_3/260-6936583-6879307?_encoding=UTF8&pd_rd_i=B08CF4LZT1&pd_rd_r=3c4454c5-b33b-48f8-913c-2057d512da60&pd_rd_w=JxlSV&pd_rd_wg=Mtccs&pf_rd_p=00b53f5d-d1f8-4708-89df-2987ccce05ce&pf_rd_r=GR8S9W3SN65ZPEWM5SXB&psc=1&refRID=GR8S9W3SN65ZPEWM5SXB'

headers = {
    "USer-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='productTitle').get_text()
price = soup.find(id='priceblock_ourprice').get_text()
converted_price = float(price[2:8])

print(title.strip())
print(converted_price)
