import logging
import os
from pathlib import Path


class Validator:
    def __init__(self):
        self.folder_name = "TextFixer"
        self.home_dir = Path.home()
        self.possible_docs_folders = ["Documents", "Документы"]  # may vary depending on the language of the system
        self.documents_path = None
        self.app_folder_path = None
        self.settings_path = None
        self.settings_default_text = """[General]
enable_notifications = true

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
