from bs4 import BeautifulSoup as bs4
import requests

def get_filename(href):
    if href:
        return href.split('#')[0]


def write_text_file(filename, text):
    with open(f'../{filename}', 'w') as file:
        file.write(text)


def write_binary_file(filename, chunks):
    with open(f'../{filename}', 'wb') as file:
        for chunk in chunks:
            file.write(chunk)


base_url = 'https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/'

toc_file = 'book-Z-H-4.html'
toc_url = f'{base_url}{toc_file}#%_toc_start'
toc_resp = requests.get(toc_url)
toc_soup = bs4(toc_resp.text, 'html.parser')
toc_links =  toc_soup.find_all('a') + toc_soup.find_all('link')

write_text_file(toc_file, toc_resp.text)

page_names = [ get_filename(link.get('href')) for link in toc_links ]
page_names = list(set([ name for name in page_names if name ]))
image_names = []
for i, page_name in enumerate(page_names):
    print(f'Fetching page #{i+1} of {len(page_names)} ({page_name})...')
    page_url = f'{base_url}{page_name}'
    page_resp = requests.get(page_url)

    page_soup = bs4(page_resp.text, 'html.parser')
    image_names += [ img.get('src') for img in page_soup.find_all('img')]

    write_text_file(page_name, page_resp.text)


image_names = list(set(image_names))
for i, image_name in enumerate(image_names):
    print(f'Fetching image #{i+1} of {len(image_names)} ({image_name})...')
    image_url = f'{base_url}{image_name}'
    image_resp = requests.get(image_url)

    write_binary_file(image_name, image_resp)

