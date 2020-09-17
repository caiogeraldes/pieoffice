#!/usr/bin/env python3

"""PIE_py

A terminal based script converter for ancient (Proto-)Indo-European languages.

Usage:
    pie_py convert <language> [<text>]
    pie_py rules <language>
"""

from docopt import docopt

def main():
    arguments = docopt(__doc__)

    rules = False

    if arguments["convert"]:
        language = arguments["<language>"]
        if language == "pie":
            from pie_tk.pie import alpha_to_pie as conv
        if language == "linearb":
            from pie_tk.linearb import alpha_to_linearb as conv
        elif language == "luwian":
            from pie_tk.luwian import alpha_to_luwian as conv
        elif language == "armenian":
            from pie_tk.armenian import alpha_to_armenian as conv
        elif language == "avestan":
            from pie_tk.avestan import alpha_to_avestan as conv
        elif language == "avestantranslit":
            from pie_tk.avestan import alpha_to_avestan_trans as conv
        elif language == "ogham":
            from pie_tk.ogham import alpha_to_ogham as conv
        elif language == "cypriot":
            from pie_tk.cypriot import alpha_to_cypriot as conv


        if arguments['<text>']:
            print(conv(arguments['<text>']))
        else:
            print("Insert a text.")
            rules = True


    if arguments['rules'] or rules:
        language = arguments["<language>"]
        if language == "pie":
            from pie_tk.pie import __doc__ as doc
        if language == "linearb":
            from pie_tk.linearb import __doc__ as doc
        elif language == "luwian":
            from pie_tk.luwian import __doc__ as doc
        elif language == "armenian":
            from pie_tk.armenian import __doc__ as doc
        elif language == "avestan" or language == "avestantranslit":
            from pie_tk.avestan import __doc__ as doc
        elif language == "ogham":
            from pie_tk.ogham import __doc__ as doc
        elif language == "cypriot":
            from pie_tk.cypriot import __doc__ as doc
        print(doc)

if __name__ == "__main__":
    main()
