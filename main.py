import requests
from bs4 import BeautifulSoup

xml_url = "https://data.cdc.gov/api/views/9j2v-jamp/rows.xml?accessType=DOWNLOAD"

try:
    response = requests.get(xml_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'xml')

    rows = soup.find_all('row')
    for row in rows:
        indicator = row.find('indicator')
        unit = row.find('unit')
        year = row.find('year')
        estimate = row.find('estimate')
        
        indicator_text = indicator.text if indicator else "NA"
        unit_text = unit.text if unit else "NA"
        year_text = year.text if year else "NA"
        estimate_text = estimate.text if estimate else "NA"
        
        print(f"Indicator: {indicator_text}, Unit: {unit_text}, Year: {year_text}, Estimate: {estimate_text}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")