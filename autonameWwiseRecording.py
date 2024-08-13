import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

class FileRenameHandler(FileSystemEventHandler):
    def __init__(self, directory):
        self.directory = directory
        super().__init__()

    def on_modified(self, event):
        if event.is_directory:
            return

        if event.src_path.endswith('RecorderIn.wav') or event.src_path.endswith('RecorderInput.wav'):
            self.rename_file(event.src_path)

    def rename_file(self, file_path):
        base, ext = os.path.splitext(file_path)
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        new_file_path = f"{base}_{timestamp}{ext}"
        
        if os.path.isfile(file_path):
            shutil.copy(file_path, new_file_path)
            print(f"File {file_path} renamed to {new_file_path}")

if __name__ == "__main__":
    directory_to_watch = '.'  # Change this to your target directory
    event_handler = FileRenameHandler(directory_to_watch)
    observer = Observer()
    observer.schedule(event_handler, path=directory_to_watch, recursive=False)
    
    try:
        print(f"Watching directory: {directory_to_watch}")
        observer.start()
        while True:
            pass  # Run indefinitely
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
