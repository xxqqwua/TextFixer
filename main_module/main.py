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
    try:
        text = clip.get_clipboard()
        lang_code = clip.detect_language(text)

        corrected_text = await corr.correct_text(text, lang_code)
        clip.send_corrected(corrected_text)

        if IS_NOTIFY_ENABLED:
            n.notify('Your text has been corrected & will be pasted.')

        if IS_NOTIFY_SOUND_ENABLED:
            n.sound_notify(str(sound_path))

        if IS_PASTE_ENABLED:
            clip.paste_corrected()

    except Exception as e:
        logging.exception(f'Something went wrong: \n{e}')
        if IS_NOTIFY_SOUND_ENABLED:
            n.sound_notify(str(bad_sound_path))


def hotkey_callback():
    asyncio.run(main())


if __name__ == '__main__':
    import main_module.tray  # script

    logging.config.dictConfig(LOGGING_CONFIG)
    v.validate_settings_file()
    v.validate_sound_file()
    sound_path = v.sound_path
    bad_sound_path = v.bad_sound_path

    config.read(v.settings_path, encoding="utf-8")
    HOTKEY = config.get("Hotkeys", "correct_text", fallback="ctrl+q+g")
    IS_NOTIFY_ENABLED = config.getboolean("General", "enable_windows_notifications", fallback=True)
    IS_NOTIFY_SOUND_ENABLED = config.getboolean("General", "enable_notifications_sound", fallback=True)
    IS_PASTE_ENABLED = config.getboolean("General", "enable_paste_after_success", fallback=True)

    HL = HotkeyListener(hotkey_callback, HOTKEY)
    HL.start()
