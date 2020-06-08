import sys

from mparser.Command import Command

# Appending the parent dir to be able to import Lib
sys.path.append('..')
from Lib import debug

# Returns true/false for valid + a list of commands? serverOnly check should be done at the end since it doesn't really belong in parsing, maybe?
class Parser:

  def __init__(self, tts, cts):
    self.token_types = tts
    self.command_types = cts

  # public boolean hasServerOnlyCommands( List<Command> commands ) {
  #   for (Command c : commands) {
  #     if ( t.getType().getServerOnly() ) return true; 
  #   }
  #   return false; // If no Commands are server only
  # }

 # Returns a Command? Or just a boolean (true when it matches one)? Maybe this should be rewritten to really only expect a single command, and then a different method to expect/deal with multiple ones in succession
  def parseSingle(self, tokens):

    c = None
    # Loop through all CommandTypes to see if one matches the first token received
    for ct in self.command_types:
      if (tokens[0].token_type.name == ct.token_types[0].name):
        debug("Found matching command!")
        # We found a matching command!
        c = ct
        break
    if (not c): debug("First token didn't match any Command"); sys.exit(-1) # Put debug into lib class and replace with debug here. This one should also sys.exit, so put that functionality into debug

    if len(c.token_types) > len(tokens): debug(f"Not enough tokens received to match the Command: {c.name}"); sys.exit(-1)

    # Loop through the identified Command's TokenTypes to see if they all match the received token list
    tts_received = []
    for t in tokens: tts_received.append(t.token_type)
    for ctt, ttt in zip(c.token_types, tts_received):
      if ctt.name != ttt.name: debug(f"Token list didn't match Command: {c.name}"); sys.exit(-1)

    # If the conditional above never fired it means the tokens received at least matches a full command (tho)
    debug(f"Successfully parsed an instance of Command: {c.name}")

    # Written to assume we might have multiple commands, so we only create a command from the number of tokens matching the CommandType.
    return Command(c, tokens[0:len(c.token_types)+1]);
