class Token:

  def __init__(self, ttype, value):
    self.token_type = ttype # TokenType
    self.value = value

  def __str__(self):
    return f"Type: {self.token_type.name} | " + \
           f"Value: {self.value}"
