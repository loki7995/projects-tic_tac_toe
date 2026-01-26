import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    try:
        # Send HTTP request
        response = requests.get(url)
        response.raise_for_status()

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all article titles (example: <h2> tags)
        titles = soup.find_all('h2')

        if not titles:
            print("No titles found.")
            return

        print("Extracted Titles:\n")
        for idx, title in enumerate(titles, start=1):
            print(f"{idx}. {title.get_text(strip=True)}")

    except requests.exceptions.RequestException as e:
        print("Error fetching the webpage:", e)


# Example usage
url = input("Enter the website URL: ")
scrape_titles(url)
#OUTPUT
'''
Enter the website URL: https://www.youtube.com/watch?v=dR9B_gPxjkk&list=RDdR9B_gPxjkk&start_radio=1
No titles found.'''