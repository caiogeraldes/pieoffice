#!/usr/bin/env python3

""" Armenian script converter

This scripts allows the user to convert between the latinized transliteration
of Armenian and the Armenian Script itself with (almost) simple rules.
Types supported with the flag -t:
    - armenian or none: Armenian alphabet
    - maiscules: Armenian alphabet in maiscules only
    - iso:  ISO romanization
    - Classical:  Classical romanization

Usage
-----
pieoffice armenian <text>
pieoffice armenian <text> --type
    ----------------------------------------------------------------
    | a 	 ա | b	    բ | g	 գ | d	    դ | e	 ե |
    | ye	 ե | z      զ | ee	 է | e'     ը | t'	 թ | 
    | zh	 ժ | i	    ի | l	 լ | x	    խ | c	 ծ | 
    | k 	 կ | h      հ | j	 ձ | g.     ղ | l.	 ղ |
    | ch.	 ճ | m      մ | y	 յ | n      ն | sh	 շ |
    | o 	 ո | ch     չ | p	 պ | jh     ջ | r.	 ռ | 
    | s	         ս | v	    վ | t        տ | r	    ր | c'	 ց |
    | w          ւ | p'     փ | k'       ք | o'     օ | f 	 ֆ |
    | u	         ու| ev     և | ?	 ՞ | .      ։ | .'	 ՝ |
    | ;          ՟ | ;'     ՛ | !	 ՜ | ``     « | ''	 » |
    ----------------------------------------------------------------


"""

import re

ASCII_TO_ARMENIAN_SCRIPT_MINISCULES = [
        # Complex input (+1 char)
        (r"ew",     "և"),
        (r"ee",     "է"),
        (r"e'",     "ը"),
        (r"t'",     "թ"),
        (r"zh",     "ժ"),
        (r"[lg]'",  "ղ"),
        (r"ch'",    "չ"),
        (r"ch",     "ճ"),
        (r"sh",     "շ"),
        (r"jh",     "ջ"),
        (r"c'",     "ց"),
        (r"p'",     "փ"),
        (r"k'",     "ք"),
        (r"o'",     "օ"),
        (r"r'",     "ռ"),

        (r"a",      "ա"),
        (r"b",      "բ"),
        (r"g",      "գ"),
        (r"d",      "դ"),
        (r"e",      "ե"),
        (r"z",      "զ"),
        (r"i",      "ի"),
        (r"l",      "լ"),
        (r"x",      "խ"),
        (r"c",      "ծ"),
        (r"k",      "կ"),
        (r"h",      "հ"),
        (r"j",      "ձ"),
        (r"m",      "մ"),
        (r"y",      "յ"),
        (r"n",      "ն"),
        (r"o",      "ո"),
        (r"p",      "պ"),
        (r"s",      "ս"),
        (r"v",      "վ"),
        (r"t",      "տ"),
        (r"r",      "ր"),
        (r"w",      "ւ"),
        (r"f",      "ֆ"),
        (r"u",      "ու"),
]

ASCII_TO_ARMENIAN_SCRIPT_MAISCULES = [
        # Complex input (+1 char)
        (r"EE",     "Է"),
        (r"E'",     "Ը"),
        (r"T'",     "Թ"),
        (r"Z[Hh]",  "Ժ"),
        (r"[LG]'",  "Ղ"),
        (r"C[Hh]'", "Չ"),
        (r"C[Hh]",  "Ճ"),
        (r"S[Hh]",  "Շ"),
        (r"J[Hh]",  "Ջ"),
        (r"C'",     "Ց"),
        (r"P'",     "Փ"),
        (r"K'",     "Ք"),
        (r"O'",     "Օ"),
        (r"R'",     "Ռ"),

        (r"A",      "Ա"),
        (r"B",      "Բ"),
        (r"G",      "Գ"),
        (r"D",      "Դ"),
        (r"E",      "Ե"),
        (r"Z",      "Զ"),
        (r"I",      "Ի"),
        (r"L",      "Լ"),
        (r"X",      "Խ"),
        (r"C",      "Ծ"),
        (r"K",      "Կ"),
        (r"H",      "Հ"),
        (r"J",      "Ձ"),
        (r"M",      "Մ"),
        (r"Y",      "Յ"),
        (r"N",      "Ն"),
        (r"O",      "Ո"),
        (r"P",      "Պ"),
        (r"S",      "Ս"),
        (r"V",      "Վ"),
        (r"T",      "Տ"),
        (r"R",      "Ր"),
        (r"W",      "Ւ"),
        (r"F",      "Ֆ"),
        (r"U",      "ՈՒ")
]

ASCII_TO_ARMENIAN_SCRIPT_PUNCT = [
    (r"\?", "՞"),
    (r"\.", "։"),
    (r"\.'", "՝"),
    (r";", "՟"),
    (r";'", "՛"),
    (r"!", "՜"),
    (r"``", "«"),
    (r"''", "»")
]

ASCII_TO_ARMENIAN_ISO = [
         # Miniscules
        (r"ee",             r"ē"),
        (r"e'",             r"ë"),
        (r"o'",             r"ò"),
        (r"([ptk])'",       r"\1’"),
        (r"zh",             r"ž"),
        (r"[lg]'",          r"ġ"),
        (r"ch'",            r"č"),
        (r"ch",             r"č̣"),
        (r"sh",             r"š"),
        (r"jh",             r"ǰ"),
        (r"r'",             r"ṙ"),
        (r"c",              r"ç"),
        (r"ç'",             r"c’"),
        # Maiscules
        (r"EE",             r"Ē"),
        (r"E'",             r"Ë"),
        (r"O'",             r"Օ"),
        (r"([PTKC])'",      r"\1’"),
        (r"Z[Hh]",          r"Ž"),
        (r"[LG]'",          r"Ġ"),
        (r"C[Hh]'",         r"Č̣"),
        (r"C[Hh]",          r"Č"),
        (r"S[Hh]",          r"Š"),
        (r"J[Hh]",          r"ǰ"),
        (r"R'",             r"Ṙ"),
        (r"C",              r"Ç"),
]

ASCII_TO_ARMENIAN_CLASSICAL = [
         # Miniscules
        (r"ee",             r"ē"),
        (r"e'",             r"ə"),
        (r"o'",             r"ō"),
        (r"([ptkc])'",      r"\1ʿ"),
        (r"zh",             r"ž"),
        (r"[lg]'",          r"ł"),
        (r"ch'",            r"čʿ"),
        (r"ch",             r"č"),
        (r"sh",             r"š"),
        (r"jh",             r"ǰ"),
        (r"r'",             r"r̄"),
        # Maiscules
        (r"EE",             r"Ē"),
        (r"E'",             r"Ə"),
        (r"O'",             r"Ō"),
        (r"([PTKC])'",      r"\1ʿ"),
        (r"Z[Hh]",          r"Ž"),
        (r"[LG]'",          r"Ł"),
        (r"C[Hh]'",         r"Čʿ"),
        (r"C[Hh]",          r"Č"),
        (r"S[Hh]",          r"Š"),
        (r"J[Hh]",          r"ǰ"),
        (r"R'",             r"R̄")
]

ARMENIAN_SCRIPT_NUMBERS = [
        (r"9(\d\d\d)",   r"Ք\1"),
        (r"8(\d\d\d)",   r"Փ\1"),
        (r"7(\d\d\d)",   r"Ւ\1"),
        (r"6(\d\d\d)",   r"Ց\1"),
        (r"5(\d\d\d)",   r"Ր\1"),
        (r"4(\d\d\d)",   r"Տ\1"),
        (r"3(\d\d\d)",   r"Վ\1"),
        (r"2(\d\d\d)",   r"Ս\1"),
        (r"1(\d\d\d)",   r"Ռ\1"),
        (r"9(\d\d)",     r"Ջ\1"),
        (r"8(\d\d)",     r"Պ\1"),
        (r"7(\d\d)",     r"Չ\1"),
        (r"6(\d\d)",     r"Ո\1"),
        (r"5(\d\d)",     r"Շ\1"),
        (r"4(\d\d)",     r"Ն\1"),
        (r"3(\d\d)",     r"Յ\1"),
        (r"2(\d\d)",     r"Մ\1"),
        (r"1(\d\d)",     r"Ճ\1"),
        (r"9(\d)",       r"Ղ\1"),
        (r"8(\d)",       r"Ձ\1"),
        (r"7(\d)",       r"Հ\1"),
        (r"6(\d)",       r"Կ\1"),
        (r"5(\d)",       r"Ծ\1"),
        (r"4(\d)",       r"Խ\1"),
        (r"3(\d)",       r"Լ\1"),
        (r"2(\d)",       r"Ի\1"),
        (r"1(\d)",       r"Ժ\1"),
        (r"9",           r"Թ"),
        (r"8",           r"Ը"),
        (r"7",           r"Է"),
        (r"6",           r"Զ"),
        (r"5",           r"Ե"),
        (r"4",           r"Դ"),
        (r"3",           r"Գ"),
        (r"2",           r"Բ"),
        (r"1",           r"Ա"),
        (r"0",           r""),
]

class AsciiConverter:
    """
    Replace ASCII notation with an Unicode transliteration scheme for
    Classical Armenian.

    Attributes
    ----------
    scheme : str
        String with the name of the transliteration scheme to be used.

    script_set: list
        List with correspondences to be used in the conversion method.

    Methods
    -------
    __init__(self, scheme)
        Constructs the converter with the transliteration scheme.

        Parameters
        -----------
            scheme : str
                String with the name of the transliteration scheme to be used.
                Options: "armenian_alphabet", "armenian_maiscules",
                         "iso", "classical"
                Default: "armenian_alphabet"

    converter (self, ascii_string)
        Converts a ascii string to the converter's scheme.

        Parameters
        ----------
            ascii_string : str
                String with the text to be converted in ASCII notation.

    >>> from cltk.alphabet.arm.ascii_to_unicode import AsciiConverter
    >>> ascii_replace = AsciiConverter()
    >>> string = "Patasxani et hreshtakn ew asee c'na."
    >>> ascii_replace.converter(string)
    "Պատասխանի ետ հրեշտակն և ասէ ցնա։"
    >>> ascii_replace_iso = AsciiConverter("iso")
    >>> ascii_replace_iso.converter(string)
    "Patasxani et hreštakn ew asē c’na."
    >>> ascii_replace_classical = AsciiConverter("classical")
    >>> ascii_replace_classical.converter(string)
    "Patasxani et hreštakn ew asē cʿna."
    >>> ascii_replace_maiscules = AsciiConverter("armenian_maiscules")
    >>> ascii_replace_maiscules.converter(string)
    "ՊԱՏԱՍԽԱՆԻ ԵՏ ՀՐԵՇՏԱԿՆ ԵՒ ԱՍԷ ՑՆԱ։"
    """

    def __init__(self, scheme="armenian_alphabet"):
        if scheme == "armenian_alphabet":
            self.scheme = "armenian_alphabet"
            self.script_set = ASCII_TO_ARMENIAN_SCRIPT_MINISCULES\
                    + ASCII_TO_ARMENIAN_SCRIPT_MAISCULES + ASCII_TO_ARMENIAN_SCRIPT_PUNCT\
                    + ARMENIAN_SCRIPT_NUMBERS
        elif scheme == "armenian_maiscules":
            self.scheme = "armenian_maiscules"
            self.script_set = ASCII_TO_ARMENIAN_SCRIPT_MAISCULES + ASCII_TO_ARMENIAN_SCRIPT_PUNCT\
                    + ARMENIAN_SCRIPT_NUMBERS
        elif scheme == "iso":
            self.scheme = "iso"
            self.script_set = ASCII_TO_ARMENIAN_ISO
        elif scheme == "classical":
            self.scheme = "classical"
            self.script_set = ASCII_TO_ARMENIAN_CLASSICAL

    def converter(self, ascii_text):
        if self.scheme == "armenian_maiscules":
            output = ascii_text.upper()
        else:
            output = ascii_text

        for pair in self.script_set:
            output = re.sub(pair[0], pair[1], output)
        return output



def alpha_to_armenian(input_string):
    converter = AsciiConverter(scheme="armenian_alphabet")
    output = converter.converter(input_string)
    return(output)


def alpha_to_iso_armenian(input_string):
    converter = AsciiConverter(scheme="iso")
    output = converter.converter(input_string)
    return(output)

def alpha_to_classical_armenian(input_string):
    converter = AsciiConverter(scheme="classical")
    output = converter.converter(input_string)
    return(output)
