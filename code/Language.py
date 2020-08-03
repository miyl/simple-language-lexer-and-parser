class Language:

  def __init__(self):
      token_types = []
      command_types = []

  # Get TokenType by name
  def gtt(self, name):
    return next(x for x in self.token_types if x.name == name)

  # TODO: This currently isn't used at all?!
  # Get CommandType by name
  def gct(self, name):
    return next(x for x in self.command_types if x.name == name)

  # Should the lexer or parser handle/validate max number of characters?
  # Edit: Or maybe none of them should and I should handle it afterwards in the main program?
