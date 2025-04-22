import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of SHL product catalog
url = "https://www.shl.com/solutions/products/product-catalog/"

# Send a GET request to the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# List to store assessment data
assessments = []

# Hypothetical structure: adjust based on actual page inspection
for item in soup.find_all('div', class_='assessment-item'):  # Update class based on actual HTML
    try:
        name = item.find('h2').text.strip()
        url = item.find('a')['href']
        remote_support = item.find('span', class_='remote-support').text.strip()
        adaptive_support = item.find('span', class_='adaptive-support').text.strip()
        duration = item.find('span', class_='duration').text.strip()
        test_type = item.find('span', class_='test-type').text.strip()
        description = item.find('p', class_='description').text.strip()

        assessments.append({
            'name': name,
            'url': url,
            'remote_support': remote_support,
            'adaptive_support': adaptive_support,
            'duration': duration,
            'test_type': test_type,
            'description': description
        })
    except AttributeError:
        continue  # Skip items with missing data

# Save to CSV
df = pd.DataFrame(assessments)
df.to_csv('assessments.csv', index=False)

print("Scraping complete. Data saved to assessments.csv")