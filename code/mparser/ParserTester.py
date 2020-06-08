import sys

from mparser.Parser import Parser

# Appending the parent dir to be able to import ChatLanguage
sys.path.append('..')
from ChatLanguage import ChatLanguage

class ParserTester:

    def __call__(self, tokens):
        lang = ChatLanguage()
        p = Parser(lang.token_types, lang.command_types)
        return p.parseSingle(tokens)
