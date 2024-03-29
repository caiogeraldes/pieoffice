# PIE-Office: A terminal based script converter for ancient (Proto-)Indo-European languages.

This application is a tentative to convert my editor-based keybinding plugins for typing ancient Indo-European languages `pievim` and `pie-macs` to a standalone application.
I am not much of a GUI person, so this comes as a terminal based converter, but it will hopefully be more useful for those not using `vim` or `emacs`.
Generally, this project will lag behind the `pievim`, since it is being done in a rather hobbist fashion.

So far, the mappings cover:
 - Proto-Indo-European (`pieoffice convert pie <text>`)
 - Indic:
    - Vedic / Sanskrit:
        - Devanagari (`pieoffice vedic convert <text>` or `pieoffice sanskrit convert <text>`)
        - ISO (`pieoffice vedic convert <text> -t iso` or `pieoffice sanskrit convert <text> -t iso`)
        - IAST (`pieoffice vedic convert <text> -t iast` or `pieoffice sanskrit convert <text> -t iast`)
 - Iranic:
     - Avestan:
         - Script (`pieoffice avestan convert <text>`)
         - Transliterated as in Hoffman (`pieoffice convert avestan <text> -t translit`)
     - Old Persian Cuneiform (`pieoffice convert oldpersian <text>`)
 - Celtic:
     - Ogham Script (`pieoffice convert ogham <text>`)
 - Italic:
     - Oscan Script (`pieoffice convert oscan <text>`)
 - Germanic:
     - Gothic Script (`pieoffice convert gothic <text>`)
 - Armenian:
     - Script (`pieoffice convert armenian <text>` or `pieoffice convert armenian <text> -t armenian`)
     - Script, Maiscules only (`pieoffice convert armenian <text> -t maiscules`)
     - Romanized in ISO (`pieoffice convert armenian <text> -t iso`)
     - Romanized in Classical (`pieoffice convert armenian <text> -t maiscules`)
 - Greek:
    - Polytonic Greek (`pieoffice convert greek <text>`)
    - Mycenaean Linear B Script (`pieoffice convert linearb <text>`)
    - Cypriot Syllabary (`pieoffice convert cypriot <text>`)
 - Anatolian:
    - Hieroglyphic Luwian (`pieoffice convert luwian <text>`)
    - Lydian (`pieoffice convert lydian <text>`)
    - Lycian (`pieoffice convert lycian <text>`)
    - Carian (`pieoffice convert carian <text>`)

# Installation

The easiest way so far is, if you have pip, to run:

```bash
pip install --user pieoffice
```

And to upgrade:

```bash
pip install --upgrade pieoffice
```

# Usage

To figure out what are the languages available:

```bash
pieoffice list
```

To check the rules for a given language:

```bash
pieoffice rules <language>
```

To convert:

```bash
pieoffice convert <language> <text>
```

# TODO

## JSON

It could be better having the dictionary structures converted to json, since it would allow some fancier techniques, maybe?

# Contribute

This is a hobbist project, so please let me know if you would employ a different algorithm or make a pull request.
Any tinkering with the code is most welcome.

