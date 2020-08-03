from Language import Language
from lexer.TokenType import TokenType
# Renamed from parser to mparser since parser is the name of a builtin package
from mparser.CommandType import CommandType

import re

# Central to any Language are the methods getTokenType and getCommandTypes
class ChatLanguage(Language):

  # TODO: Remember to lowercase the input, so both JOIN, join and JoIn works? Or maybe not if it's entirely computer handled?
  # Returns a TokenType list

    def __init__(self):
      super().__init__()

      # Order matters!
      # Commands
      self.token_types = [ TokenType("join",     re.compile("^JOIN")),
                           TokenType("ok",       re.compile("^J_OK")),
                           TokenType("er",       re.compile("^J_ER")),
                           TokenType("data",     re.compile("^DATA")),
                           TokenType("imav",     re.compile("^IMAV")),
                           TokenType("quit",     re.compile("^QUIT")),
                           TokenType("list",     re.compile("^LIST")),
                           # Both client and server
                           TokenType("ip",       re.compile("^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}")), # server_ip. 255.255.255.255 or something above 255 is not really valid but whatever for now.
                           TokenType("number",   re.compile("^\\d+")),      # port or err_code
                           TokenType("string",   re.compile("^[a-zA-Z0-9\\-_]+")), # user_name, message or err_msg. TODO: to contain spaces or not?
                           # To create a dedicated username string or not? regex: a-zA-Z0-9\\-_   max 12 characters
                           TokenType("colon",    re.compile("^:")),
                           TokenType("comma",    re.compile("^,")) ]

      # Should the lexer or parser handle/validate max number of characters?
      # Edit: Or maybe none of them should and I should handle it afterwards in the main program?

      ONE = 1 # Could just write 1 and 0 directly but these stand out more in the source code, and for now I just need these two specifically, not 0-9
      ANY = 0
      joinTokens = [ (super().gtt("join"), ONE), (super().gtt("string"), ONE), (super().gtt("comma"), ONE), (super().gtt("ip"), ONE), (super().gtt("colon"), ONE), (super().gtt("number"), ONE) ] # string, or should I create a dedicated username string?
      okTokens   = [ (super().gtt("ok"), ONE) ]
      erTokens   = [ (super().gtt("er"), ONE), (super().gtt("number"), ONE), (super().gtt("colon"), ONE), (super().gtt("string"), ONE) ]
      # datatokens is recursive if the string TT shouldn't have spaces. Technically this could just be "string, ANY", but keeping the username separate for now, since it probably should be turned into its own type later
      dataTokens = [ (super().gtt("data"), ONE), (super().gtt("string"), ONE), (super().gtt("string"), ANY) ]
      imavTokens = [ (super().gtt("imav"), ONE) ]
      quitTokens = [ (super().gtt("quit"), ONE) ]
      listTokens = [ (super().gtt("list"), ONE), (super().gtt("string"), ANY) ] # recursive!

      self.command_types = [ CommandType("join", joinTokens, False), # Need to validate port (1-65536) and ip (1-254) afterwards
                             CommandType("ok",   okTokens,   True),
                             CommandType("er",   erTokens,   True),
                             CommandType("data", dataTokens, False), # Max 250 characters
                             CommandType("imav", imavTokens, False),
                             CommandType("quit", quitTokens, False),
                             CommandType("list", listTokens, True)]
