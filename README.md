# PIE_tk: A terminal based script converter for ancient (Proto-)Indo-European languages.

This application is a tentative to convert my editor-based keybinding plugins for typing ancient Indo-European languages `pievim` and `pie-macs` to a standalone application.
I am not much of a GUI person, so this comes as a terminal based converter, but it will hopefully be more useful for those not using `vim` or `emacs`.
Generally, this project will lag behind the `pievim`, since it is being done in a rather hobbist fashion.

So far, the mappings cover:
 - Proto-Indo-European (`pie_tk convert pie <text>`)
 <!-- - Vedic: Harvard-Kyoto transliteration to IAST (autoload/ie/vedichk.vim) -->
 <!-- - Old Persian Cuneiform (autoload/ie/oldpersian.vim) -->
 - Avestan: 
     - Script (`pie_tk avestan convert <text>`) 
     - Transliterated (`pie_tk convert avestantranslit <text>`)
 <!-- - Old Church Slavonic Glagolitic (glagolitic) -->
 <!-- - Oscan Script (autoload/ie/oscan.vim) -->
 <!-- - Ogham Script (autoload/ie/ogham.vim) -->
 <!-- - Gothic (autoload/ie/gothic.vim) -->
 - Armenian Script (`pie_tk convert armenian <text>`)
 - Greek:
    <!-- - Polytonic Greek (autoload/ie/polytonicgreek.vim) -->
    - Mycenaean Linear B Script (`pie_tk convert linearb <text>`)
    <!-- - Cypriot Syllabary (autoload/ie/cypriot.vim) -->
 - Anatolian:
    - Hieroglyphic Luwian (`pie_tk convert luwian <text>`)
    <!-- - Lydian (autoload/ie/lydian.vim) -->
    <!-- - Lycian (autoload/ie/lycian.vim) -->
    <!-- - Carian (autoload/ie/carian.vim) -->



# TODO

## JSON

It could be better having the dictionary structures converted to json, since it would allow some fancier techniques, maybe?

# Contribute

This is a hobbist project, so please let me know if you would employ a different algorithm or make a pull request.
Any tinkering with the code is most welcome.

