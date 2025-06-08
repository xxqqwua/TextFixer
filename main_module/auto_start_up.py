import getpass as getpass
import logging
import os


class AutoStartUp:
    def __init__(self):
        self.app_name = "TextFixer.exe"
        self.app_lnk = "TextFixer.lnk"
        self.app_path = os.path.abspath(self.app_name)
        self.user_name = getpass.getuser()
        self.start_up_folder = fr'C:\Users\{self.user_name}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'

    def set_auto_startup(self):
        if not os.path.exists(self.app_path):
            logging.error("File not found. AutoStartUp is not set.")
            return False

        logging.debug("Setting AutoStartUp...")
        # vbs code to create a shortcut for .exe
        vbs_code = fr"""
           Set oWS = WScript.CreateObject("WScript.Shell")
           sLinkFile = "{self.start_up_folder}\{self.app_lnk}"
           Set oLink = oWS.CreateShortcut(sLinkFile)
           oLink.TargetPath = "{self.app_path}"
           oLink.WorkingDirectory = "{os.path.dirname(self.app_path)}"
           oLink.Save
               """

        temp_vbs = os.path.join(os.getenv("TEMP"), "create_shortcut.vbs")  # get TEMP users folder
        with open(temp_vbs, "w", encoding="utf-8") as f:
            f.write(vbs_code)

        os.system(f'cscript //nologo "{temp_vbs}"')

        os.remove(temp_vbs)
        return True

    def remove_auto_startup(self):
        logging.debug("Removing AutoStartUp...")
        try:
            os.remove(fr'{self.start_up_folder}\{self.app_lnk}')
        except FileNotFoundError:
            logging.error("File not found. AutoStartUp is not set.")

    def check_auto_startup(self):
        logging.debug("Checking AutoStartUp...")
        if os.path.exists(fr'{self.start_up_folder}\{self.app_lnk}'):
            return True
        else:
            return False
