import sys

from lexer.Lexer import Lexer

# Appending the parent dir to be able to import ChatLanguage
sys.path.append('..')
from ChatLanguage import ChatLanguage

class LexerTester:

  def __call__(self):
    print("Running Lexer Tester")

    testText1 = "DATA mjav mbq:woot 123 " # Valid input
    testText2 = "DATA mjav " # Invalid input
    testText3 = "mjav" # Invalid input
    testText4 = " JOIN " # Invalid input
    testText5 = "JOIN testUser, 123.123.123.123:8000" # Valid input
    testText6 = "LIST woo sim sala locus sfs" # Valid input

    lang = ChatLanguage()
    print("ChatLanguage initialized")
    l = Lexer( lang.token_types )

    print("About to Lex")

    # token list
    self.tokens = l.lex(testText6)

    if (self.tokens == None):
      print("The input is a different language than the one expressed by the token types.")
      print("Exiting!")
      sys.exit(-1)

    print("Done: Lexing")
    return self.tokens

  def writeTokensToFile(self):

    print("Writing to file")

    with open('tokens.txt', 'w') as f:
      for t in self.tokens:
        f.write( str(t) + "\n")

    print("Done: Writing to file")

# Run the test

#l = LexerTester()
#l.test()
# l.writeTokensToFile
