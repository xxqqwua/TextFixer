import logging
import os
from pathlib import Path

import requests


class Validator:
    def __init__(self):
        self.folder_name = "TextFixer"
        self.home_dir = Path.home()
        self.possible_docs_folders = ["Documents", "Документы"]  # may vary depending on the language of the system
        self.documents_path = None
        self.app_folder_path = None
        self.settings_path = None
        self.sound_path = None
        self.bad_sound_path = None
        self.sound_url = 'https://raw.githubusercontent.com/xxqqwua/TextFixer/refs/heads/master/src/sound.mp3'
        self.bad_sound_url = 'https://raw.githubusercontent.com/xxqqwua/TextFixer/refs/heads/master/src/bad_sound.mp3'
        self.settings_default_text = """[General]
enable_windows_notifications = true
enable_notifications_sound = true
enable_paste_after_success = true

[Hotkeys]
correct_text = ctrl+q+g"""

    def create_folder(self):
        for folder in self.possible_docs_folders:
            potential_path = self.home_dir / folder
            if potential_path.is_dir():
                self.documents_path = potential_path
                logging.debug(f"Documents folder found at {self.documents_path}")
                break

        if self.documents_path:
            full_path_to_new_folder = self.documents_path / self.folder_name

            try:
                os.makedirs(full_path_to_new_folder, exist_ok=True)
                self.app_folder_path = full_path_to_new_folder
                logging.debug(f"Folder {self.folder_name} created successfully or it already exists.")
            except OSError as e:
                logging.error(f"Error creating folder {self.folder_name}: {e}")
            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")
        else:
            logging.error("Documents folder not found.")

    def validate_settings_file(self):
        self.create_folder()

        self.settings_path = self.app_folder_path / 'settings.ini'

        if not os.path.exists(self.settings_path):
            with open(self.settings_path, 'w') as f:
                f.write(self.settings_default_text)

        return True

    def validate_sound_file(self):
        self.create_folder()

        self.sound_path = self.app_folder_path / 'sound.mp3'
        self.bad_sound_path = self.app_folder_path / 'bad_sound.mp3'

        def download_sounds(url, path):
            r = requests.get(url)

            with open(path, 'wb') as file:
                file.write(r.content)

        if not os.path.exists(self.sound_path):
            download_sounds(self.sound_url, self.sound_path)

        if not os.path.exists(self.bad_sound_path):
            download_sounds(self.bad_sound_url, self.bad_sound_path)
