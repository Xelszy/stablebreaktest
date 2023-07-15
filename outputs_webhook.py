import os
import time
import requests
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image
from tabulate import tabulate
from datetime import datetime

WEBHOOK_URL = 'https://discord.com/api/webhooks/1129451738823397386/NaKZGFF43BPw4-r6OeVTbl_DwTfljY6tyzeo9chos16X6RLzbS3CIRprUfCFddXanDYA'

def upload_file_to_discord(file_path):
    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(WEBHOOK_URL, files=files)
        if response.status_code == 200:
            print(f"📁 File submitted to Discord: {file_path}")
        else:
            print(f"❌ Failed to submit file to Discord: {response.text}")

def save_metadata_to_txt(image_path, metadata_info):
    txt_file = f"{os.path.splitext(image_path)[0]}_metadata.txt"
    table = tabulate(metadata_info, headers=['Metadata Key', 'Value'], tablefmt='grid')
    with open(txt_file, 'w') as file:
        file.write(table)
        file.write("\n\n⬆️ Diunggah melalui Discord webhook")
    return txt_file

def get_metadata_info(image_path):
    try:
        img = Image.open(image_path)
        metadata = img.info
        metadata_info = [[key, value] for key, value in metadata.items()]
        return metadata_info
    except Exception as e:
        print(f"❌ Failed to extract metadata information from {image_path}: {e}")
        return None

class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        if event.src_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            print(f"📸 New image detected: {event.src_path}")
            metadata_info = get_metadata_info(event.src_path)
            if metadata_info:
                txt_file = save_metadata_to_txt(event.src_path, metadata_info)
                upload_file_to_discord(event.src_path)
                upload_file_to_discord(txt_file)
                print(f"⌚Uploaded at: {datetime.now()}")

def start_image_watcher():
    event_handler = ImageHandler()
    observer = Observer()

    # Search path folder /outputs/txt2img-images
    current_dir = os.getcwd()
    path_to_watch = os.path.join(current_dir, 'outputs', 'txt2img-images')
    observer.schedule(event_handler, path=path_to_watch, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
start_image_watcher()

def main():
    watcher_thread = threading.Thread(target=start_image_watcher)
    watcher_thread.start()
    while True:
        print("Running another script...")
        time.sleep(1)
if __name__ == "__main__":
    main()
