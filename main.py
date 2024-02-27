from bs4 import BeautifulSoup
import openpyxl

# Read the HTML file
with open('Properties3.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with class="grid-details ng-star-inserted"
property_divs = soup.find_all('div', class_='grid-details ng-star-inserted')

# Create a new Excel workbook
workbook = openpyxl.Workbook()
sheet = workbook.active

# Write headers
sheet.append(['Name/Location', 'Type', 'Price', 'No. of Bedrooms', 'Size', 'Car Park', 'Bathrooms', 'Swimming Pool'])

# Iterate through each property div
for div in property_divs:
    # Find elements within the div
    name_location = div.find('div', class_='grid-address').text.strip()
    prop_type = div.find('div', class_='grid-type ng-star-inserted').text.strip()
    price = div.find('div', class_='grid-price').find('span', class_='ng-star-inserted').text.strip()
    
    # Try to find elements, if not found set to empty string
    no_bedrooms = div.find('li', class_='bed ng-star-inserted').div.text.strip() if div.find('li', class_='bed ng-star-inserted') else ""
    size = div.find('li', class_='acres ng-star-inserted').span.text.strip() if div.find('li', class_='acres ng-star-inserted') else ""
    car_park = div.find('li', class_='car-park ng-star-inserted').span.text.strip() if div.find('li', class_='car-park ng-star-inserted') else ""
    bathrooms = div.find('li', class_='bath ng-star-inserted').div.text.strip() if div.find('li', class_='bath ng-star-inserted') else ""
    swimming_pool = div.find('li', class_='swimming ng-star-inserted').span.text.strip() if div.find('li', class_='swimming ng-star-inserted') else ""
    
    # Write data to Excel
    sheet.append([name_location, prop_type, price, no_bedrooms, size, car_park, bathrooms, swimming_pool])

# Save the Excel file
workbook.save('property_details3.xlsx')