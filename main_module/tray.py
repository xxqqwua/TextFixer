import os
import threading

from PIL import Image, ImageDraw
from pystray import Icon, Menu, MenuItem as Item

from main_module.auto_start_up import AutoStartUp
from main_module.validator import Validator

ASUp = AutoStartUp()
AutoStartUp_is_set = ASUp.check_auto_startup()


def on_quit():
    icon.stop()
    os._exit(0)


def generate_icon_image():
    width, height = 500, 100
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    checkmark_points = [(20, 60), (40, 80), (80, 20)]
    draw.line(checkmark_points, fill="black", width=10)

    line_start = (120, 50)
    line_end = (300, 50)
    draw.line([line_start, line_end], fill="gray", width=10)

    magnifying_glass_radius = 40
    magnifying_glass_center = (450, 50)

    draw.ellipse(
        (
            magnifying_glass_center[0] - magnifying_glass_radius,
            magnifying_glass_center[1] - magnifying_glass_radius,
            magnifying_glass_center[0] + magnifying_glass_radius,
            magnifying_glass_center[1] + magnifying_glass_radius,
        ),
        outline="black",
        width=5,
    )

    handle_start = (450, 90)
    handle_end = (400, 90)
    draw.line([handle_start, handle_end], fill="black", width=10)

    return image


def set_auto_start_up():
    global AutoStartUp_is_set

    if AutoStartUp_is_set:
        ASUp.remove_auto_startup()
        AutoStartUp_is_set = False
    else:
        ASUp.set_auto_startup()
        AutoStartUp_is_set = True


def open_settings():
    v = Validator()
    v.validate_settings_file()
    settings_file_path = v.settings_path

    try:
        os.startfile(settings_file_path)
    except Exception:
        pass


menu = Menu(
    Item('AutoStartUp', set_auto_start_up, checked=lambda i: ASUp.check_auto_startup()),
    # Double display for AutoStartUP in logs is normal:
    # The first time is when the menu is just being built: you need to understand which items are checked.
    # The second time is when the menu is actually shown to the user, to update the state
    # (in case something changed between opening and rendering).
    Item('Open Settings', open_settings),
    Item('Exit', on_quit)
)

icon = Icon('My app', icon=generate_icon_image(), menu=menu)


def run_tray():
    icon.run()


tray_thread = threading.Thread(target=run_tray)
tray_thread.daemon = True  # Set as daemon so it exits when main thread exits
tray_thread.start()
