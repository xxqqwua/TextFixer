import asyncio

import language_tool_python
from language_tool_python import utils


class Corrector:
    def __init__(self):
        pass

    @staticmethod
    async def correct_text(text, lang_code):
        def run_check():
            tool = language_tool_python.LanguageTool(lang_code)
            matches = tool.check(text)
            corrected_text = utils.correct(text, matches)
            return corrected_text

        corrected_text = await asyncio.to_thread(run_check)
        return corrected_text
