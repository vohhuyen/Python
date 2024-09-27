import threading
import requests
import os

class Downloader(threading.Thread):
    def __init__(self, url, filename):
        threading.Thread.__init__(self)
        self.url = url
        self.filename = filename

    def run(self):
        print(f"Starting download: {self.url}")
        response = requests.get(self.url)

        if response.status_code == 200:
            with open(self.filename, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {self.filename}")
        else:
            print(f"Failed to download: {self.url} with status code {response.status_code}")


def download_files(urls):
    threads = []
    
    for i, url in enumerate(urls):
        filename = f"downloaded_file_{i + 1}.html"
        downloader = Downloader(url, filename)
        threads.append(downloader)
        downloader.start()

    for thread in threads:
        thread.join()

    print("All downloads completed.")


if __name__ == "__main__":
    urls_to_download = [
        'https://www.example.com',
        'https://www.wikipedia.org',
        'https://www.python.org',
        'https://www.github.com',
        'https://www.stackoverflow.com'
    ]
    
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    os.chdir('downloads') 
    download_files(urls_to_download)
