class CommandType:

  def __init__(self, name, tts, server_only):
    self.name = name
    self.token_types = tts # list of tokenTypes
    self.server_only = server_only

  def __str__(self):
    l = ""
    for tt in self.token_types:
      l = l + f"{tt.name} "
    return "Command:\n" + \
     f"Name: {self.name}\n" \
     f"Token types: {l}\n" \
     "Server only?: " + "Yes" if (self.server_only) else "No"
