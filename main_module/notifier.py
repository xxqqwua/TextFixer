from win10toast import ToastNotifier

class Notifier:
    def __init__(self):
        self.toast = ToastNotifier()

    def notify(self, text):
        self.toast.show_toast(title='Text Fixer!', msg=text, threaded=True)