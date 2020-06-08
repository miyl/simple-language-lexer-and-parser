class Command:

  def __init__(self, ctype, value):
    self.command_type = ctype  # CommandType
    self.value = value         # Token list

  def __str__(self):
    l = ""
    for t in self.value:
      l = l + f"{t.value} "
    return f"Command Type: {self.command_type.name} | " + \
           f"Value: {l}"
