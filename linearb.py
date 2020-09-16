#! /usr/bin python3

""" Linear B script converter

This scripts allows the user to convert between the latinized transliteration
of Linear B and the Linear B Script itself with (almost) simple rules.

The file can be imported as a module and contains the following functions:
    alpha_to_linearb - returns a converted string in Linear B script from
    a romanized string.
    linearb_to_alpha - returns a converted string in romanized linear B from a
    string in Linear B Script. (Might return problematic data due to double
    readings for the same grapheme in Linear B)

It also contains a dictionary:
    script - contains the equivalences between romanized and Linear B scripts.

Usage example:

    > a = ["a-pi-qo-i-ta do-e-ra MUL 32",
    >      "ko-wa me-zo-e 5 ko-wa me-wi-jo-e 15",
    >      "ko-wo me-wi-jo-e 4"]
    > b = [alpha_to_linearb(i) for i in a]
    > for i in b:
    >     print(i)
    + 𐀀𐀠𐀦𐀂𐀲 𐀈𐀁𐀨 𐂁 𐄒𐄈
    + 𐀒𐀷 𐀕𐀿𐀁 𐄋 𐀒𐀷 𐀕𐀹𐀍𐀁 𐄐𐄋
    + 𐀒𐀺 𐀕𐀹𐀍𐀁 𐄊
    > for i in b:
    >     print(linearb_to_alpha(i))
    + a-pi-qo-i-ta do-e-ra MUL 32
    + ko-wa me-zo-e 5 ko-wa me-wi-jo-e 15
    + ko-wo me-wi-jo-e 4
"""

from tools import get_key

script = {"a": "𐀀", "e": "𐀁", "i": "𐀂", "o": "𐀃", "u": "𐀄", "da": "𐀅", "de": "𐀆", "di": "𐀇", "do": "𐀈", "du": "𐀉", "ja": "𐀊", "je": "𐀋", "jo": "𐀍", "ju": "𐀎", "ka": "𐀏", "ke": "𐀐", "ki": "𐀑", "ko": "𐀒", "ku": "𐀓", "ma": "𐀔", "me": "𐀕", "mi": "𐀖", "mo": "𐀗", "mu": "𐀘", "na": "𐀙", "ne": "𐀚", "ni": "𐀛", "no": "𐀜", "nu": "𐀝", "pa": "𐀞", "pe": "𐀟", "pi": "𐀠", "po": "𐀡", "pu": "𐀢", "qa": "𐀣", "qe": "𐀤", "qi": "𐀥", "qo": "𐀦", "ra": "𐀨", "re": "𐀩", "ri": "𐀪", "ro": "𐀫", "ru": "𐀬", "sa": "𐀭", "se": "𐀮", "si": "𐀯", "so": "𐀰", "su": "𐀱", "ta": "𐀲", "te": "𐀳", "ti": "𐀴", "to": "𐀵", "tu": "𐀶", "wa": "𐀷", "we": "𐀸", "wi": "𐀹", "wo": "𐀺", "za": "𐀼", "ze": "𐀽", "zo": "𐀿", "a2": "𐁀", "a3": "𐁁", "dwe": "𐁃", "dwo": "𐁄", "nwa": "𐁅", "pte": "𐁇", "pu2": "𐁆", "ra2": "𐁈", "ra3": "𐁉", "ro2": "𐁊", "ta2": "𐁌", "two": "𐁍", "*18": "𐁐", "*19": "𐁑", "*22": "𐁒", "*34": "𐁓", "*47": "𐁔", "*49": "𐁕", "*56": "𐁖", "*63": "𐁗", "*64": "𐁘", "*65": "𐀎", "ju2": "𐀎", "*79": "𐁙", "*82": "𐁚", "*83": "𐁛", "*86": "𐁜", "*89": "𐁝", "VIR": "𐂀", "MUL": "𐂁", "CERV": "𐂂", "EQU": "𐂃", "EQUf": "𐂄", "EQUm": "𐂅", "OVISf": "𐂆", "OVISm": "𐂇", "CAPf": "𐂈", "CAPm": "𐂉", "SUSf": "𐂊", "SUSm": "𐂋", "BOSf": "𐂌", "BOSm": "𐂍", "GRA": "𐂎", "HORD": "𐂏", "OLIV": "𐂐", "AROM": "𐂑", "CYP": "𐂒", "KAPO": "𐂓", "KANAKO": "𐂔", "OLE": "𐂕", "VIN": "𐂖", "*132": "𐂗", "AREPA": "𐂘", "MERI": "𐂙", "AES": "𐂚", "AUR": "𐂛", "*142": "𐂜", "LANA": "𐂝", "*146": "𐂞", "*150": "𐂟", "CORNU": "𐂠", "*152": "𐂡", "*153": "𐂢", "*154": "𐂣", "TURO2": "𐂤", "*157": "𐂥", "*158": "𐂦", "TELA": "𐂧", "*160": "𐂨", "*161": "𐂩", "TUNICA": "𐂪", "ARMA": "𐂫", "*164": "𐂬", "*165": "𐂭", "*166": "𐂮", "*167": "𐂯", "*168": "𐂰", "*169": "𐂱", "*170": "𐂲", "*171": "𐂳", "*172": "𐂴", "LUNA": "𐂵", "*174": "𐂶", "ARBOR": "𐂷", "*177": "𐂸", "*178": "𐂹", "*179": "𐂺", "*180": "𐂻", "*181": "𐂼", "*182": "𐂽", "*183": "𐂾", "*184": "𐂿", "*185": "𐃀", "*189": "𐃁", "*190": "𐃂", "GALEA": "𐃃", "*220": "𐃄", "ALVEUS": "𐃅", "HASTA": "𐃆", "SAGITTA": "𐃇", "*232": "𐃈", "PUGIO": "𐃉", "*234": "𐃊", "*236": "𐃋", "BIGAE": "𐃌", "CURRUS": "𐃍", "CAPSUS": "𐃎", "ROTA": "𐃏", "*245": "𐃐", "*246": "𐃑", "DIPTE": "𐃒", "*248": "𐃓", "*249": "𐃔", "*251": "𐃕", "*252": "𐃖", "*253": "𐃗", "JACULUM": "𐃘", "*255": "𐃙", "*256": "𐃚", "*257": "𐃛", "*258": "𐃜", "*259": "𐃝", "*155": "𐃞", "*200": "𐃟", "*201": "𐃠", "*202": "𐃡", "*203": "𐃢", "*204": "𐃣", "*205": "𐃤", "*206": "𐃥", "*207": "𐃦", "*208": "𐃧", "*209": "𐃨", "*210": "𐃩", "*211": "𐃪", "*212": "𐃫", "*213": "𐃬", "*214": "𐃭", "*215": "𐃮", "*216": "𐃯", "*217": "𐃰", "*218": "𐃱", "*219": "𐃲", "*221": "𐃳", "*222": "𐃴", "*226": "𐃵", "*227": "𐃶", "*228": "𐃷", "*229": "𐃸", "*250": "𐃹", "*305": "𐃺", ",": "𐄀", "L": "𐄷", "M": "𐄸", "N": "𐄹", "P": "𐄺", "Q": "𐄻", "T": "𐄼", "S": "𐄽", "V": "𐄾", "Z": "𐄿", "1": "𐄇", "2": "𐄈", "3": "𐄉", "4": "𐄊", "5": "𐄋", "6": "𐄌", "7": "𐄍", "8": "𐄎", "9": "𐄏", "10": "𐄐", "20": "𐄑", "30": "𐄒", "40": "𐄓", "50": "𐄔", "60": "𐄕", "70": "𐄖", "80": "𐄗", "90": "𐄘", "100": "𐄙", "200": "𐄚", "300": "𐄛", "400": "𐄜", "500": "𐄝", "600": "𐄞", "700": "𐄟", "800": "𐄠", "900": "𐄡", "1000": "𐄢", "2000": "𐄣", "3000": "𐄤", "4000": "𐄥", "5000": "𐄦", "6000": "𐄧", "7000": "𐄨", "8000": "𐄩", "9000": "𐄪", "10000": "𐄫", "20000": "𐄬", "30000": "𐄭", "40000": "𐄮", "50000": "𐄯", "60000": "𐄰", "70000": "𐄱", "80000": "𐄲", "90000": "𐄳"}

def alpha_to_linearb(input):
    """ Converts text in Latin Alphabet to Linear B Script

    Each syllable should be separated by a sing dash, each word by a space.

    Parameters
    ----------
    input : str
        Text input with syllables separated by dashes and words by spaces.

    Returns
    -------
    output : str
        Transliterated text in Linear B Script

    Usage
    -----
    
    > alpha_to_linearb("to-so-jo pe-ma GRA 32")
    + 𐀵𐀰𐀍 𐀟𐀔 𐂎 𐄒𐄈

    """

    output = []
    input = input.split(" ")
    for word in input:
        word_out = ""
        if word.isnumeric():
            word = [int(i) for i in word]
            tens = [10**n for n in range(len(word)-1,-1,-1)]
            for i in range(len(tens)):
                word_out = word_out + script[str(word[i]*tens[i])]
        elif "-" in word:
            for syllabe in word.split("-"):
                word_out = word_out + script[syllabe]
        else:
            word_out = script[word]

        output.append(word_out)

    return " ".join(output)


def linearb_to_alpha(input):
    """ Converts text in Linear B Script to Latin Alphabet

    Some errors might occur if a syllable has multiple values.

    Parameters
    ----------
    input : str
        Text input in Linear B Script

    Returns
    -------
    output : str
        Transliterated text in Latin Alphabet

    Usage
    -----
    
    > linearb_to_alpha("𐀵𐀰𐀍 𐀟𐀔 𐂎 𐄒𐄈")
    + to-so-jo pe-ma GRA 32

    """
    output = []
    input = input.split()
    for word in input:
        word_out = ""
        if len(word) > 1:
            syllabes = [sy for sy in word]
            for syllabe in syllabes:
                word_out = word_out + get_key(syllabe, script) + "-"
            word_out = str(word_out)
            if len(word_out) > 1 and word_out[-1] == "-":
                word_out = word_out[:-1]
        else:
            word_out = get_key(word, script)
        output.append(word_out)
        for i in range(len(output)):
            if output[i].split("-")[0].isnumeric():
                output[i] = str(sum([int(i) for i in output[i].split("-")]))

    return " ".join(output)

if __name__ == "__main__":
    a = ["a-pi-qo-i-ta do-e-ra MUL 32",
         "ko-wa me-zo-e 5 ko-wa me-wi-jo-e 15",
         "ko-wo me-wi-jo-e 4"]
    b = [alpha_to_linearb(i) for i in a]
    for i in b:
        print(i)

    for i in b:
        print(linearb_to_alpha(i))
        
