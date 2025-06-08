import asyncio
import configparser
import logging

from main_module.clipboard_handler import ClipboardHandler
from main_module.corrector import Corrector
from main_module.hotkey_listener import HotkeyListener
from main_module.logging_config import LOGGING_CONFIG
from main_module.notifier import Notifier
from main_module.validator import Validator

clip = ClipboardHandler()
corr = Corrector()
v = Validator()
n = Notifier()

config = configparser.ConfigParser()


async def main():
    text = clip.get_clipboard()
    lang_code = clip.detect_language(text)

    corrected_text = await corr.correct_text(text, lang_code)

    clip.send_corrected(corrected_text)

    if IS_NOTIFY_ENABLED:
        n.notify('Your text has been corrected & will be pasted.')

    clip.paste_corrected()


def hotkey_callback():
    asyncio.run(main())


if __name__ == '__main__':
    import main_module.tray  # script

    logging.config.dictConfig(LOGGING_CONFIG)
    v.validate_settings_file()

    config.read(v.settings_path, encoding="utf-8")
    HOTKEY = config.get("Hotkeys", "correct_text", fallback="ctrl+q+g")
    IS_NOTIFY_ENABLED = config.getboolean("General", "enable_notifications", fallback=True)

    HL = HotkeyListener(hotkey_callback, HOTKEY)
    HL.start()
