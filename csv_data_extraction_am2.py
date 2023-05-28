# reading the links from csv created before and extrxting info from each page
from bs4 import BeautifulSoup
import requests
import csv
 
# Function to extract product details from URL
def extract_product_details(url):
    # Send a GET request to the product URL
    response = requests.get(url)
    # if response.status_code == 200:
    html = response.text

        # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

        # Find and extract the desired information
    Description = soup.find('span', id='productTitle')
    Asin = soup.find('th', string='ASIN').find_next('td')
    Product_description = soup.find('div', id='productDescription')
    Manufacturer = soup.find('a', id='bylineInfo')
    
    description = Description.text.strip() if Description else None
    asin = Asin.text.strip() if Asin else None
    product_description = Product_description.text.strip() if Product_description else None
    manufacturer = Manufacturer.text.strip() if Manufacturer else None



        # Return the extracted information
    return description, asin, product_description, manufacturer

    

# Create a list to store the extracted data
data = []

# Loop through each URL
for url_num in range(1, 11):
    # Get the URL from the product_data.csv file
    with open('test/product_data.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            
            product_url = row[2]  # Assuming the product URL is in the 5th column of the CSV file

            # Extract product details from the URL
            product_details = extract_product_details(product_url)
            if product_details is not None:

                # Add the data to the list
                data.append(product_details)
                print(f"saved{product_details}")
# Write the data to a new CSV file
with open('test/product_details.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Description', 'ASIN', 'Product Description', 'Manufacturer'])
    writer.writerows(data)
