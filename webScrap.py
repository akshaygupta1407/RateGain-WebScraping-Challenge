# Akshay Gupta
import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

def scrape_page(url):
    r = requests.get(url, headers=headers)
    r.raise_for_status()  # Raises HTTPError for bad requests
    soup = BeautifulSoup(r.text, 'html.parser')

    data = {'title': [], 'date': [], 'image_url': [], 'likes_count': []}

    for article in soup.select('article.blog-item.category-blog'):
        title_elem = article.select_one('.content h6 a')
        date_elem = article.select_one('.blog-detail .bd-item:first-child span')
        image_url_elem = article.select_one('.wrap .img a')
        likes_count_elem = article.select_one('.wrap .content > a.zilla-likes i ~ span')

        title = title_elem.contents[0] if title_elem else 'No Title'
        date = date_elem.contents[0] if date_elem else 'No Date'
        image_url = image_url_elem.get('data-bg') if image_url_elem else 'No Image URL'
        likes_count = likes_count_elem.contents[0] if likes_count_elem else 'No Likes'

        data['title'].append(title)
        data['date'].append(date)
        data['image_url'].append(image_url)
        data['likes_count'].append(likes_count)

    return data

def main():
    base_url = "https://rategain.com/blog/page/"
    total_pages = 45
    all_data = {'title': [], 'date': [], 'image_url': [], 'likes_count': []}

    for page in range(1, total_pages + 1):
        url = f"{base_url}{page}"
        page_data = scrape_page(url)

        all_data['title'].extend(page_data['title'])
        all_data['date'].extend(page_data['date'])
        all_data['image_url'].extend(page_data['image_url'])
        all_data['likes_count'].extend(page_data['likes_count'])

    df = pd.DataFrame(all_data)
    df.to_csv("output.csv", index=False)

if __name__ == "__main__":
    main()
