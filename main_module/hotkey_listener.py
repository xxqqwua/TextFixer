import keyboard


class HotkeyListener:
    def __init__(self, func, hotkey: str = 'ctrl+alt+g', callback=None):
        self.hotkey = hotkey
        self.callback = callback
        self.func = func

    def start(self):
        keyboard.add_hotkey(self.hotkey, self.func, suppress=True, trigger_on_release=True)
        keyboard.wait()
