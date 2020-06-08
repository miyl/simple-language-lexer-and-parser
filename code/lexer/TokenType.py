class TokenType:

  name = ""
  regex = "" # Pattern

  def __init__(self, name, regex):
    self.name = name
    self.regex = regex

  def __str__(self):
    return f"Name: {self.name}\n"
