import sys

from lexer.Token import Token

# Appending the parent dir to be able to import Lib
sys.path.append('..')
from Lib import debug

class Lexer:

  def __init__(self, tokenTypes):
    self.TOKEN_TYPES = tokenTypes

  # Takes a string, returns a token list
  def lex(self, to_lex):
    tokens_found = []

    # Remove preceding and trailing white space.
    to_lex = to_lex.strip()
    remaining = to_lex

    # Loop through the entire input string received
    while (len(to_lex) != 0):

      # debug("Offset: " + offset)
      # debug("Length: " + len(to_lex)
      # debug("Current to_lex: " + to_lex[offset])
      # debug("Current to_lex: " + to_lex)

      # Try to match each token_type to the current position in the input string
      for tt in self.TOKEN_TYPES:
        matcher = tt.regex.match(to_lex)
        if ( matcher ): # matcher returns true on success
          debug("TokenType " + tt.name + " matched!")
          tokens_found.append( Token( tt, matcher.group() ) )
          # Find offset of the end of the match, and remove whitespace (TODO: should it only be preceding? Then .lstrip() instead)
          remaining = to_lex[matcher.end():].strip()
          break # If a match is found break, so next elements are checked against ALL token types and in the right order.

        else: debug("TokenType " + tt.name + " didn't match.")

      # If all token types where tried and none matched, either the Lexer is faulty or the TokenList doesn't match the to_lex.
      if (to_lex == remaining): return None
      else: to_lex = remaining

    return tokens_found
