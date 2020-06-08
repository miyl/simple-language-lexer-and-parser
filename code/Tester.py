from lexer import LexerTester
from mparser import ParserTester

print("Testing lexer")
l = LexerTester.LexerTester()
tokens = l()
l.writeTokensToFile()
# l.writeTokensToFile
print("Testing parser")
p = ParserTester.ParserTester()
command = p(tokens)
print(command)
