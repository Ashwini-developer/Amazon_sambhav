import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URLs for Indian Trade Portal and DGFT
ITC_PORTAL_URL = 'https://www.indiantradeportal.in/'
DGFT_PORTAL_URL = 'https://www.dgft.gov.in/'

# Function to scrape the Indian Trade Portal for export-related data
def get_export_policy_data():
    # Example: Scraping the home page for export policy-related info
    response = requests.get(ITC_PORTAL_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find relevant links related to RODTEP and Duty Drawback (you'll need to inspect HTML structure)
        export_policy_section = soup.find_all('a', href=True, text='Export Policy')  # Change text to actual section name
        rodtep_section = soup.find_all('a', href=True, text='RODTEP')
        duty_drawback_section = soup.find_all('a', href=True, text='Duty Drawback')

        # Print URLs for scraping
        policy_links = [link['href'] for link in export_policy_section]
        rodtep_links = [link['href'] for link in rodtep_section]
        drawback_links = [link['href'] for link in duty_drawback_section]

        print("Export Policy Links: ", policy_links)
        print("RODTEP Links: ", rodtep_links)
        print("Duty Drawback Links: ", drawback_links)
        
        return policy_links, rodtep_links, drawback_links

# Function to scrape the DGFT website for duty drawback and export policy data
def get_dgft_policy_data():
    response = requests.get(DGFT_PORTAL_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find specific sections or links related to the policies
        export_policy_section = soup.find_all('a', href=True, text='Export Policy')
        duty_drawback_section = soup.find_all('a', href=True, text='Duty Drawback')

        # Extract the links
        policy_links = [link['href'] for link in export_policy_section]
        drawback_links = [link['href'] for link in duty_drawback_section]

        print("DGFT Export Policy Links: ", policy_links)
        print("DGFT Duty Drawback Links: ", drawback_links)
        
        return policy_links, drawback_links

# Scrape and display data
export_policy_links, rodtep_links, duty_drawback_links = get_export_policy_data()
dgft_policy_links, dgft_drawback_links = get_dgft_policy_data()

# Combine results into a DataFrame
data = {
    "Export Policy Links (ITC)": export_policy_links,
    "RODTEP Links (ITC)": rodtep_links,
    "Duty Drawback Links (ITC)": duty_drawback_links,
    "Export Policy Links (DGFT)": dgft_policy_links,
    "Duty Drawback Links (DGFT)": dgft_drawback_links
}

df = pd.DataFrame(data)
print(df)

# Optionally save the result as a CSV file
df.to_csv("export_policy_links.csv", index=False)
