#!/usr/bin/env python3

# This program generates a DuckDuckGo link with the no-region setting active.
# The query string is ascii-escaped for obfuscation
# Input is taken as commandline arguments (if any) or from standard input

from sys import argv

escape_char = lambda char: "%%%02x" % ord(char)
escape = lambda string: "".join([escape_char(ch) for ch in string])

link = "ddg.gg/?kl=wt-wt&q={}"
if len(argv) > 1:
    input_string = " ".join(argv[1:])
else:
    input_string = input("input> ")
escaped = escape(input_string)
output = link.format(escaped)
print(output)