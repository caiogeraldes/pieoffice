#!/usr/bin/env python3

"""PIE-Office: (Proto-)Indo-European Office

A terminal based script converter for ancient (Proto-)Indo-European languages.

Usage:
    pieoffice convert <language> [<text>]
    pieoffice rules <language>
    pieoffice list
    pieoffice --help
    
Languages:
    pie                 Proto-Indo-European
    linearb             Mycenaean Libear B
    cypriot             Cypriot Greek Script
    luwian              Hieroglyphic Luwian
    lycian              Lycian
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
            from pieoffice.pie import alpha_to_pie as conv
        if language == "linearb":
            from pieoffice.linearb import alpha_to_linearb as conv
        elif language == "luwian":
            from pieoffice.luwian import alpha_to_luwian as conv
        elif language == "lycian":
            from pieoffice.lycian import alpha_to_lycian as conv
        elif language == "armenian":
            from pieoffice.armenian import alpha_to_armenian as conv
        elif language == "avestan":
            from pieoffice.avestan import alpha_to_avestan as conv
        elif language == "avestantranslit":
            from pieoffice.avestan import alpha_to_avestan_trans as conv
        elif language == "ogham":
            from pieoffice.ogham import alpha_to_ogham as conv
        elif language == "cypriot":
            from pieoffice.cypriot import alpha_to_cypriot as conv


        if arguments['<text>']:
            print(conv(arguments['<text>']))
        else:
            print("Insert a text.")
            rules = True


    if arguments['rules'] or rules:
        language = arguments["<language>"]
        if language == "pie":
            from pieoffice.pie import __doc__ as doc
        if language == "linearb":
            from pieoffice.linearb import __doc__ as doc
        elif language == "luwian":
            from pieoffice.luwian import __doc__ as doc
        elif language == "lycian":
            from pieoffice.lycian import __doc__ as doc
        elif language == "armenian":
            from pieoffice.armenian import __doc__ as doc
        elif language == "avestan" or language == "avestantranslit":
            from pieoffice.avestan import __doc__ as doc
        elif language == "ogham":
            from pieoffice.ogham import __doc__ as doc
        elif language == "cypriot":
            from pieoffice.cypriot import __doc__ as doc
        print(doc)

    if arguments['list']:
        print("""Languages:
            pie                 Proto-Indo-European
            linearb             Mycenaean Libear B
            cypriot             Cypriot Greek Script
            luwian              Hieroglyphic Luwian
            lycian              Lycian
            armenian            Armenian
            avestan             Avestan (script)
            avestantranslit     Avestan (romanized)
            ogham               Ogham Script
            """
            )


if __name__ == "__main__":
    main()
