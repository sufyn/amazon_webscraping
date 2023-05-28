import csv
import requests

# Specify the CSV file path containing the URLs
csv_file = 'test/product_data.csv'

# Specify the directory where you want to save the HTML files
save_directory = 'test/files/'

# Read URLs from the CSV file
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    # Skip the header row if it exists
    next(reader)
    # Loop through each row in the CSV
    for row in reader:
        url = row[2]  # Assuming the URL is in the first column (index 0)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Create a filename for the HTML file
              for i in range(1,25):  
                filename = f"amz{i}" + '.html'
                # Save the web content as an HTML file
                with open(save_directory + filename, 'w', encoding='utf-8') as html_file:
                    html_file.write(response.text)
                print(f'Successfully saved HTML for {url}')
            else:
                print(f'Failed to fetch HTML for {url}. Status code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Failed to fetch HTML for {url}. Error: {e}')
