import asyncio

from clipboard_handler import ClipboardHandler
from corrector import Corrector
from hotkey_listener import HotkeyListener

clip = ClipboardHandler()
corr = Corrector()


async def main():
    text = clip.get_clipboard()
    lang_code = clip.detect_language(text)

    corrected_text = await corr.correct_text(text, lang_code)

    clip.send_corrected(corrected_text)
    clip.paste_corrected()


def hotkey_callback():
    asyncio.run(main())


if __name__ == '__main__':
    import logging
    from logging_config import LOGGING_CONFIG

    logging.config.dictConfig(LOGGING_CONFIG)

    hotkey = HotkeyListener(hotkey_callback)
    hotkey.start()
