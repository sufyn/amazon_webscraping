from bs4 import BeautifulSoup
import csv




data = []

for page in range(1,21):
    with open(f'test/amazon/Amazon{page}.html', 'r') as file:
        html = file.read()

    # Parse the HTML 
    soup = BeautifulSoup(html, 'html.parser')

    # Find all divs
    # divs = soup.find_all('div', class_='s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t3 puis-include-content-margin puis puis-v3mswmdmewdea31z8uag8cukeii s-latency-cf-section s-card-border')
    divs = soup.find_all('div', class_='s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t3 puis-include-content-margin puis s-latency-cf-section s-card-border')



    # Extract 
    for div in divs:
        product_name = div.find('span', class_='a-size-medium a-color-base a-text-normal')
        product_price = div.find('span', class_='a-price-whole')
        product_url = div.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
        product_reviews = div.find('span', class_='a-size-base s-underline-text')
        product_rating = div.find('span', class_='a-icon-alt')

        Product_Name = product_name.text.strip() if product_name else 'None'
        Product_Price = product_price.text.strip() if product_price else 'None'
        Product_Url = "https://www.amazon.com"+ product_url.get("href") if product_url else 'None'
        Product_Reviews = product_reviews.text.strip() if product_reviews else 'None'
        Product_Rating = product_rating.text.strip()[:4] if product_rating else 'None'

        data.append([Product_Name, Product_Price, Product_Url, Product_Reviews, Product_Rating])

#data to a CSV file
with open('test/product_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product_Name', 'Product_Price', 'Product_Url', 'Product_Reviews', 'Product_Rating'])
    writer.writerows(data)
