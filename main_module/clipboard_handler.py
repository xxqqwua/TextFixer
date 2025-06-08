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

        return data

    @staticmethod
    def send_corrected(text):  # send corrected text to clipboard
        pyperclip.copy(text)

    @staticmethod
    def paste_corrected():  # paste corrected text from clipboard
        pyperclip.paste()

    @staticmethod
    def detect_language(text):
        return detect(text)
