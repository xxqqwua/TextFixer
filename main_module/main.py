import asyncio
import configparser
import logging

from clipboard_handler import ClipboardHandler
from corrector import Corrector
from hotkey_listener import HotkeyListener
from logging_config import LOGGING_CONFIG
from validator import Validator

clip = ClipboardHandler()
corr = Corrector()
v = Validator()

config = configparser.ConfigParser()


async def main():
    text = clip.get_clipboard()
    lang_code = clip.detect_language(text)

    corrected_text = await corr.correct_text(text, lang_code)

    clip.send_corrected(corrected_text)
    clip.paste_corrected()


def hotkey_callback():
    asyncio.run(main())


if __name__ == '__main__':
    logging.config.dictConfig(LOGGING_CONFIG)
    v.validate_settings_file()

    config.read(v.settings_path, encoding="utf-8")
    HOTKEY = config.get("Hotkeys", "correct_text", fallback="ctrl+q+g")

    HL = HotkeyListener(hotkey_callback, HOTKEY)
    HL.start()
