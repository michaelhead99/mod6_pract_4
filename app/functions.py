# functions.py

import requests
from bs4 import BeautifulSoup


def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information
        page_title = soup.title.string if soup.title else "No title"
        page_content = soup.get_text()[:200]
        image_count = len(soup.find_all('img'))

        return page_title, page_content, image_count

    except requests.RequestException as e:
        return f"Error: {e}", "", 0
    except Exception as e:
        return f"An unexpected error occurred: {e}", "", 0
