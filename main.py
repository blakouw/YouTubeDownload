from pytube import YouTube
from tqdm import tqdm
import urllib.request

def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        file_size = video.filesize

        print(f"Pobieranie: {yt.title}")

        with tqdm(total=file_size, unit='B', unit_scale=True) as pbar:
            def progress_callback(count, block_size):
                progress = count * block_size
                pbar.update(progress - pbar.n)

            urllib.request.urlretrieve(video.url, f"videos/{yt.title}.mp4", reporthook=progress_callback)

        print("Pobieranie zakończone!")

    except Exception as e:
        print("Wystąpił błąd podczas pobierania:", str(e))

def main():
    video_url = input("Podaj URL filmu na YouTube: ")
    download_video(video_url)

if __name__ == "__main__":
    main()