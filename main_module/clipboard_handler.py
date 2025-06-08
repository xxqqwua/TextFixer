import logging

import keyboard
import pyperclip
from langdetect import detect


class ClipboardHandler:
    def __init__(self):
        pass

    @staticmethod
    def get_clipboard():  # get clipboard data
        data = pyperclip.paste()

        logging.debug(f'Got clipboard data: {data}')
        return data

    @staticmethod
    def send_corrected(text):  # send corrected text to clipboard
        pyperclip.copy(text)
        logging.debug(f'Send corrected text to clipboard: {text}')

    @staticmethod
    def paste_corrected():  # paste corrected text from clipboard
        keyboard.press_and_release('ctrl+v')
        logging.debug('paste corrected text from clipboard')

    @staticmethod
    def detect_language(text):
        logging.debug(f'Detect language: {detect(text)}')
        return detect(text)
