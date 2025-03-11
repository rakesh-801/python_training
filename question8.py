import os
import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def download_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return None


def extract_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for tag in soup.find_all('a', href=True):
        href = tag['href']
        if href.startswith('http'):
            links.add(href)
        else:
            links.add(base_url + href)
    return links

# Function to download a single link
def download_link(url):
    content = download_page(url)
    if content:
        filename = f"downloads/{url.replace('http://', '').replace('https://', '').replace('/', '_')}.html"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Downloaded {url}")

# ThreadPoolExecutor
def download_links_threadpool(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_link, urls)

# ProcessPoolExecutor
def download_links_processpool(urls):
    with ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(download_link, urls)

# Asyncio-based downloader
async def async_download_link(session, url):
    try:
        async with session.get(url) as response:
            content = await response.text()
            filename = f"downloads/{url.replace('http://', '').replace('https://', '').replace('/', '_')}.html"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"Downloaded {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

async def download_links_async(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [async_download_link(session, url) for url in urls]
        await asyncio.gather(*tasks)


def main():
    url = "https://knowledge.hubspot.com/files/copy-and-update-the-url-of-files-uploaded-to-the-file-manager"  # Change this to the target URL
    html = download_page(url)
    
    if not html:
        return
    
    links = extract_links(html, url)
    print(f"Found {len(links)} links.")
    
    
    # download_links_threadpool(links)
     download_links_processpool(links)
    asyncio.run(download_links_async(links))

if __name__ == "__main__":
    main()
