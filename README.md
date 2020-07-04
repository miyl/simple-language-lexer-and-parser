# Simple language lexer and parser

For an assignment I tried to write this lexer and parser to verify whether messages sent back and forth between a chat
client and server were valid.

But I don't know if it really qualifies as a parser, because it doesn't generate a parse tree as there's no nesting, so
it's all a (flat) list.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

The `Lexer` produces a list of `Tokens`, each of which has a concrete value and a `TokenType`.  
A `TokenType` basically corresponds to a regular expression.

The `Parser` takes the output of the `Lexer` - the list of `Tokens`, runs through that list comparing it to all
`CommandTypes`, ultimately producing a `Command` if it succeeds.  
A `CommandType` basically corresponds to a list of `TokenTypes`.

## TODO

- Create a config file (INI-like?) and move debug being true/false to there
  Maybe it should also include the language to lex/parse? Should it just be by name, still requiring a .py file for the language, or
  should it actually contain the entire language there as well, say in JSON format or whatever?
- Support the two commands that contain an arbitrary number of tokens: the user LIST and the message itself (DATA)
