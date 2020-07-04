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

  # This was originally written in java, I still haven't decided whether it's relevant or whether it should just be deleted or implemented a totally different way
  # def hasServerOnlyCommands( commands ):
  #   for (c in commands) {
  #     if ( t.getType().getServerOnly() ) return True
  #   }
  #   return False // If no Commands are server only
  #

 # Returns a Command? Or just a boolean (true when it matches one)? Maybe this should be rewritten to really only expect a single command, and then a different method to expect/deal with multiple ones in succession
  def parseSingle(self, tokens):

    c = None
    # Loop through all CommandTypes to see if one matches the first token received
    for ct in self.command_types:
      if (tokens[0].token_type.name == ct.token_types[0][0].name):
        debug("Found matching command!")
        # We found a matching command!
        c = ct
        break
    if (not c): debug("First token didn't match any Command"); sys.exit(-1) # Put debug into lib class and replace with debug here. This one should also sys.exit, so put that functionality into debug

    if len(c.token_types) > len(tokens): debug(f"Not enough tokens received to match the Command: {c.name}"); sys.exit(-1)

    # Loop through the identified Command's TokenTypes to see if they all match the received token list
    tts_received = []
    # Isolate just the token types from all tokens received
    for t in tokens: tts_received.append(t.token_type)

    # Loop through all token_types of the identified command to see if they match the lexed token list
    i = 0
    for ctt in c.token_types:
      # Check if the next received token matches the command's
      if ctt[0].name != tts_received[i].name: debug(f"Token list didn't match Command: {c.name}"); sys.exit(-1)
      # Special handling for TokenTypes in a command that should be allowed to be there more than once
      if ctt[1] != 1:
        # a value of zero means any number, any other positive value means that specific number
        num = None if ctt[1] == 0 else ctt[1]+1
        for t in tts_received[i:num]:
          if ctt[0].name == t.name:
            i+=1
          else:
            i-=1; break # If the current token doesn't match the type take one step back in the list, since a step forward will be taken in the next line
      i+=1

    if len(tts_received) > i: debug(f"A Command was fully matched but the received list contain additional tokens?: {c.name}"); sys.exit(-1)
    # If both conditionals above never fired it means the tokens received matches a full command
    else: debug(f"Successfully parsed an instance of Command: {c.name}")

    return Command(c, tokens);
