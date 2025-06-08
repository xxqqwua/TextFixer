import asyncio
import logging

import language_tool_python
from language_tool_python import utils


class Corrector:
    def __init__(self):
        self.LANG_CODE_MAP = {
            'en': 'en-US',  # English - default US
            'de': 'de-DE',  # German - region specification
            'it': 'it-IT',  # Italian
            'pl': 'pl-PL',  # Polish
            'pt': 'pt-PT',  # Portuguese - default EU
            'ro': 'ro-RO',  # Romanian
            'ru': 'ru-RU',  # Russian
            'sk': 'sk-SK',  # Slovakian
            'sl': 'sl-SI',  # Slovenian
            'uk': 'uk-UA',  # Ukrainian
            'zh-cn': 'zh-CN',  # Simplified Chinese
            'zh-tw': 'zh-TW',  # Traditional Chinese
            'ja': 'ja-JP',  # Japanese
        }

    async def correct_text(self, text, lang_code):
        lang_code = self.LANG_CODE_MAP.get(lang_code)
        logging.debug(f'lang_code: {lang_code}')

        if not lang_code:
            return text

        def run_check():
            with language_tool_python.LanguageTool(lang_code) as tool:
                matches = tool.check(text)
                corrected_text = utils.correct(text, matches)
                logging.debug(f'corrected_text: {corrected_text}')
                return corrected_text

        corrected_text = await asyncio.to_thread(run_check)
        return corrected_text
