#!/usr/bin/env python3

"""PIE-Office: (Proto-)Indo-European Office

A terminal based script converter for ancient (Proto-)Indo-European languages.

Usage:
    pie-office convert <language> [<text>]
    pie-office rules <language>
    
Languages:
    pie                 Proto-Indo-European
    linearb             Mycenaean Libear B
    cypriot             Cypriot Greek Script
    luwian              Hieroglyphic Luwian
    armenian            Armenian
    avestan             Avestan (script)
    avestantranslit     Avestan (romanized)
    ogham               Ogham Script

Options:
    -h --help           Show this screen.

"""

from docopt import docopt

def main():
    arguments = docopt(__doc__)

    rules = False

    if arguments["convert"]:
        language = arguments["<language>"]
        if language == "pie":
            from pie-office.pie import alpha_to_pie as conv
        if language == "linearb":
            from pie-office.linearb import alpha_to_linearb as conv
        elif language == "luwian":
            from pie-office.luwian import alpha_to_luwian as conv
        elif language == "armenian":
            from pie-office.armenian import alpha_to_armenian as conv
        elif language == "avestan":
            from pie-office.avestan import alpha_to_avestan as conv
        elif language == "avestantranslit":
            from pie-office.avestan import alpha_to_avestan_trans as conv
        elif language == "ogham":
            from pie-office.ogham import alpha_to_ogham as conv
        elif language == "cypriot":
            from pie-office.cypriot import alpha_to_cypriot as conv


        if arguments['<text>']:
            print(conv(arguments['<text>']))
        else:
            print("Insert a text.")
            rules = True


    if arguments['rules'] or rules:
        language = arguments["<language>"]
        if language == "pie":
            from pie-office.pie import __doc__ as doc
        if language == "linearb":
            from pie-office.linearb import __doc__ as doc
        elif language == "luwian":
            from pie-office.luwian import __doc__ as doc
        elif language == "armenian":
            from pie-office.armenian import __doc__ as doc
        elif language == "avestan" or language == "avestantranslit":
            from pie-office.avestan import __doc__ as doc
        elif language == "ogham":
            from pie-office.ogham import __doc__ as doc
        elif language == "cypriot":
            from pie-office.cypriot import __doc__ as doc
        print(doc)

if __name__ == "__main__":
    main()
