from bs4 import BeautifulSoup
import requests
import os

URL = "https://yandex.ru/images/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

def get_image(image_url, name, index):
    if not os.path.isdir(name):
        os.mkdir(name)
    picture = requests.get(f"https:{image_url}", HEADERS)
    saver = open(os.path.join(f"{name}/{str(index).zfill(4)}.jpg"), "wb")
    saver.write(picture.content)
    saver.close()

def download_img(path, key):
    os.chdir(path)
    if not os.path.isdir("dataset"):
        os.mkdir("dataset")
    os.chdir("dataset")
    
    count = 0
    page = 0
    
    while count < 1000:
        key1=key.replace(" ", "%20")
        url = f'{URL}search?p={page}&text={key}&from=tabbar'
        print(f'Fetching URL: {url}')
        
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "lxml")
        images = soup.findAll('img', class_='serp-item__thumb justifier__thumb')
        if not images:
            print("No images found on this page.")
            break

        for image in images:
            if count == 1020:
                return
            image_url = image.get("src")
            if image_url and not image_url.startswith("data:"):
                get_image(image_url, key, count)
                count += 1
        print(count)
        page += 1





def main():
    directory = os.getcwd()
    download_img(directory, 'brownbear')
    download_img(directory, 'polarbear')

if __name__ == "__main__":
    main()