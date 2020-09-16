#!/usr/bin/env python3

"""PIE_py

Usage:
    pie_py convert <language> [<text>]
    pie_py rules <language>
"""

from docopt import docopt

def main():
    arguments = docopt(__doc__)
    if arguments["convert"]:
        language = arguments["<language>"]
        if language == "linearb":
            from linearb import alpha_to_linearb as conv
        elif language == "luwian":
            from luwian import alpha_to_luwian as conv
        elif language == "armenian":
            from armenian import alpha_to_armenian as conv
        if arguments['<text>']:
            print(conv(arguments['<text>']))
        else:
            print("Insira um texto")
    elif arguments['rules']:
        language = arguments["<language>"]
        if language == "linearb":
            from linearb import script
        elif language == "luwian":
            from luwian import script
        elif language == "armenian":
            from armenian import script
        print(script)

if __name__ == "__main__":
    main()
