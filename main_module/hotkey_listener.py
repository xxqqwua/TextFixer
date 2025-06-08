import keyboard
import logging


class HotkeyListener:
    def __init__(self, func, hotkey: str, callback=None):
        self.hotkey = hotkey
        self.callback = callback
        self.func = func

    def start(self):
        keyboard.add_hotkey(self.hotkey, self.func, suppress=True, trigger_on_release=True)
        logging.debug(f'Hotkey: {self.hotkey} for {self.func.__name__} is setup')
        keyboard.wait()
