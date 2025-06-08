import logging

import pyautogui
import pyperclip
import win32clipboard
from langdetect import detect


class ClipboardHandler:
    def __init__(self):
        pass

    @staticmethod
    def get_clipboard():  # get clipboard data
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        logging.debug(f'Got clipboard data: {data}')
        return data

    @staticmethod
    def get_text_to_clipboard():
        pyautogui.hotkey('ctrl', 'a')
        logging.debug('Hotkey "ctrl+a" is pressed')
        pyautogui.hotkey('ctrl', 'c')
        logging.debug('Hotkey "ctrl+c" is pressed')

    @staticmethod
    def send_corrected(text):  # send corrected text to clipboard
        pyperclip.copy(text)
        logging.debug(f'Send corrected text to clipboard: {text}')

    @staticmethod
    def paste_corrected():  # paste corrected text from clipboard
        pyautogui.hotkey('ctrl', 'v')
        logging.debug('paste corrected text from clipboard')

    @staticmethod
    def detect_language(text):
        logging.debug(f'Detect language: {detect(text)}')
        return detect(text)
