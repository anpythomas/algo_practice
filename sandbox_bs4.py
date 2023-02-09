import requests
from bs4 import BeautifulSoup


# Headers Dictionary
headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
"Accept-Language": "en-US,en;q=0.9",
"Referer": "https://google.com",
"DNT": "1",
}
"https://whiskyauctioneer.com/auction-search?text=weller+12&sort=field_reference_field_end_date+DESC&items_per_page=500"
"https://whiskyauctioneer.com/auction-search?items_per_page=500&sort=field_reference_field_end_date%20DESC&text=weller%2012&page=1"
"https://whiskyauctioneer.com/auction-search?items_per_page=500&sort=field_reference_field_end_date%20DESC&text=weller%20107&page=1"

url = "https://www.exchange-rates.org/Rate/GBP/USD"

# Soupify data
r = requests.get(url, headers=headers)

# Soupify data
soup = BeautifulSoup(r.text, 'html.parser')
print(soup)

# gen_list = soup.select("span DFlfde")
#
# print(gen_list)