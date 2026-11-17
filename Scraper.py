import requests
import json
from bs4 import BeautifulSoup
import pandas

page = 1
products_list = []
while(True):
    url = f"https://example-store.com/zaryadni-stancii?page={page}"

    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "YOUR_SESSION_COOKIES_HERE",
        "origin": "https://example-store.com",
        "priority": "u=1, i",
        "referer": "https://example-store.com/zaryadni-stancii?page=2",
        "sec-ch-ua": "\"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"156\", \"Google Chrome\";v=\"156\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }

    data = f"action=load_products&data%5Bpage%5D={page}"

    response = requests.post(url, headers=headers, data=data)
    print(f"Response status: {response.status_code}")

    json_data = response.json()

    html_content = json_data.get("html", "")

    soup = BeautifulSoup(html_content, "lxml")

    all_products = soup.select("div.js_ProductItem")

    if(not all_products):
        print("All pages were parsed!")
        break

    saved_elements_count = 0
    for product in all_products:
        if "darkened" in product.get("class", []):
            continue

        name = product.get("data-seo-name")
        price = product.find("div", class_="price").text.strip()
        url ="https://example-store.com" + product.find("a", class_="addToSeo").get("href")
        saved_elements_count += 1

        products_list.append({
            "Name" : name,
            "Price" : price,
            "URL" : url
        })

    print(f"Number of parsed page: {page} | Amount of parsed elements: {saved_elements_count}")
    page += 1



df = pandas.DataFrame(products_list)
df.to_csv("Parsed_Data.csv", index=False, encoding="utf-8-sig")