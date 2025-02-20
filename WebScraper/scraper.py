import requests
from bs4 import BeautifulSoup

def scraper(url):
    
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Find and print the first <h1> tag content
        links = []
        data_tag = soup.find('a', 'data-introtext'==True)  # You can adjust this to any tag you want
        for x in data_tag:
            if x['attrs']
            links.append(x['attrs'])
        print(links)
        if h1_tag:
            print(h1_tag.text)
        
        # Example: Find all links on the page
        links = soup.find_all('a', href=True)  # Finds all <a> tags with href attributes
        for link in links:
            print(link['href'])
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    return 

if __name__ == "__main__":
    scraper('https://www.ospedalesanmartino.it/it/mappa-geo.html?start_catid=230')
