#! /usr/bin/env python3

""" Linear B script converter

Glyphs with known syllabic values should be written in lower-case, syllabically
and numbered if +2. Glyphs with known logographic values should be written in
upper-case. The only exception for said rule are the gendered logograms, which
should be followed without space by a f or m. Glyphs with unknown value should
be written with an asterisk followed by the number (2 or 3 digits).

"""

from .tools import get_key

script = {"a": "𐀀", "e": "𐀁", "i": "𐀂", "o": "𐀃", "u": "𐀄", "da": "𐀅", "de": "𐀆", "di": "𐀇", "do": "𐀈", "du": "𐀉", "ja": "𐀊", "je": "𐀋", "jo": "𐀍", "ju": "𐀎", "ka": "𐀏", "ke": "𐀐", "ki": "𐀑", "ko": "𐀒", "ku": "𐀓", "ma": "𐀔", "me": "𐀕", "mi": "𐀖", "mo": "𐀗", "mu": "𐀘", "na": "𐀙", "ne": "𐀚", "ni": "𐀛", "no": "𐀜", "nu": "𐀝", "pa": "𐀞", "pe": "𐀟", "pi": "𐀠", "po": "𐀡", "pu": "𐀢", "qa": "𐀣", "qe": "𐀤", "qi": "𐀥", "qo": "𐀦", "ra": "𐀨", "re": "𐀩", "ri": "𐀪", "ro": "𐀫", "ru": "𐀬", "sa": "𐀭", "se": "𐀮", "si": "𐀯", "so": "𐀰", "su": "𐀱", "ta": "𐀲", "te": "𐀳", "ti": "𐀴", "to": "𐀵", "tu": "𐀶", "wa": "𐀷", "we": "𐀸", "wi": "𐀹", "wo": "𐀺", "za": "𐀼", "ze": "𐀽", "zo": "𐀿", "a2": "𐁀", "a3": "𐁁", "dwe": "𐁃", "dwo": "𐁄", "nwa": "𐁅", "pte": "𐁇", "pu2": "𐁆", "ra2": "𐁈", "ra3": "𐁉", "ro2": "𐁊", "ta2": "𐁌", "two": "𐁍", "*18": "𐁐", "*19": "𐁑", "*22": "𐁒", "*34": "𐁓", "*47": "𐁔", "*49": "𐁕", "*56": "𐁖", "*63": "𐁗", "*64": "𐁘", "*65": "𐀎", "ju2": "𐀎", "*79": "𐁙", "*82": "𐁚", "*83": "𐁛", "*86": "𐁜", "*89": "𐁝", "VIR": "𐂀", "MUL": "𐂁", "CERV": "𐂂", "EQU": "𐂃", "EQUf": "𐂄", "EQUm": "𐂅", "OVISf": "𐂆", "OVISm": "𐂇", "CAPf": "𐂈", "CAPm": "𐂉", "SUSf": "𐂊", "SUSm": "𐂋", "BOSf": "𐂌", "BOSm": "𐂍", "GRA": "𐂎", "HORD": "𐂏", "OLIV": "𐂐", "AROM": "𐂑", "CYP": "𐂒", "KAPO": "𐂓", "KANAKO": "𐂔", "OLE": "𐂕", "VIN": "𐂖", "*132": "𐂗", "AREPA": "𐂘", "MERI": "𐂙", "AES": "𐂚", "AUR": "𐂛", "*142": "𐂜", "LANA": "𐂝", "*146": "𐂞", "*150": "𐂟", "CORNU": "𐂠", "*152": "𐂡", "*153": "𐂢", "*154": "𐂣", "TURO2": "𐂤", "*157": "𐂥", "*158": "𐂦", "TELA": "𐂧", "*160": "𐂨", "*161": "𐂩", "TUNICA": "𐂪", "ARMA": "𐂫", "*164": "𐂬", "*165": "𐂭", "*166": "𐂮", "*167": "𐂯", "*168": "𐂰", "*169": "𐂱", "*170": "𐂲", "*171": "𐂳", "*172": "𐂴", "LUNA": "𐂵", "*174": "𐂶", "ARBOR": "𐂷", "*177": "𐂸", "*178": "𐂹", "*179": "𐂺", "*180": "𐂻", "*181": "𐂼", "*182": "𐂽", "*183": "𐂾", "*184": "𐂿", "*185": "𐃀", "*189": "𐃁", "*190": "𐃂", "GALEA": "𐃃", "*220": "𐃄", "ALVEUS": "𐃅", "HASTA": "𐃆", "SAGITTA": "𐃇", "*232": "𐃈", "PUGIO": "𐃉", "*234": "𐃊", "*236": "𐃋", "BIGAE": "𐃌", "CURRUS": "𐃍", "CAPSUS": "𐃎", "ROTA": "𐃏", "*245": "𐃐", "*246": "𐃑", "DIPTE": "𐃒", "*248": "𐃓", "*249": "𐃔", "*251": "𐃕", "*252": "𐃖", "*253": "𐃗", "JACULUM": "𐃘", "*255": "𐃙", "*256": "𐃚", "*257": "𐃛", "*258": "𐃜", "*259": "𐃝", "*155": "𐃞", "*200": "𐃟", "*201": "𐃠", "*202": "𐃡", "*203": "𐃢", "*204": "𐃣", "*205": "𐃤", "*206": "𐃥", "*207": "𐃦", "*208": "𐃧", "*209": "𐃨", "*210": "𐃩", "*211": "𐃪", "*212": "𐃫", "*213": "𐃬", "*214": "𐃭", "*215": "𐃮", "*216": "𐃯", "*217": "𐃰", "*218": "𐃱", "*219": "𐃲", "*221": "𐃳", "*222": "𐃴", "*226": "𐃵", "*227": "𐃶", "*228": "𐃷", "*229": "𐃸", "*250": "𐃹", "*305": "𐃺", ",": "𐄀", "L": "𐄷", "M": "𐄸", "N": "𐄹", "P": "𐄺", "Q": "𐄻", "T": "𐄼", "S": "𐄽", "V": "𐄾", "Z": "𐄿", "1": "𐄇", "2": "𐄈", "3": "𐄉", "4": "𐄊", "5": "𐄋", "6": "𐄌", "7": "𐄍", "8": "𐄎", "9": "𐄏", "10": "𐄐", "20": "𐄑", "30": "𐄒", "40": "𐄓", "50": "𐄔", "60": "𐄕", "70": "𐄖", "80": "𐄗", "90": "𐄘", "100": "𐄙", "200": "𐄚", "300": "𐄛", "400": "𐄜", "500": "𐄝", "600": "𐄞", "700": "𐄟", "800": "𐄠", "900": "𐄡", "1000": "𐄢", "2000": "𐄣", "3000": "𐄤", "4000": "𐄥", "5000": "𐄦", "6000": "𐄧", "7000": "𐄨", "8000": "𐄩", "9000": "𐄪", "10000": "𐄫", "20000": "𐄬", "30000": "𐄭", "40000": "𐄮", "50000": "𐄯", "60000": "𐄰", "70000": "𐄱", "80000": "𐄲", "90000": "𐄳", "0":""}

def alpha_to_linearb(input, numbers=True):
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

    # output = input.split()
    # if numbers:
    #     for i in range(len(output)):
    #         if output[i].isnumeric():
    #             num_out = 0
    #             print(output[i])
    #             num = [int(j) for j in output[i]]
    #             tens = [10**n for n in range(len(num)-1,-1,-1)]
    #             for i in range(len(tens)):
    #                 num_out = num + script[str(num[i]*tens[i])]
    #         output[i] = num_out

    
    output = input.replace("-", "")

    # output = " ".join(output).replace("-", "")

    output = output.replace("*132", "𐂗")
    output = output.replace("*142", "𐂜")
    output = output.replace("*146", "𐂞")
    output = output.replace("*150", "𐂟")
    output = output.replace("*152", "𐂡")
    output = output.replace("*153", "𐂢")
    output = output.replace("*154", "𐂣")
    output = output.replace("*155", "𐃞")
    output = output.replace("*157", "𐂥")
    output = output.replace("*158", "𐂦")
    output = output.replace("*160", "𐂨")
    output = output.replace("*161", "𐂩")
    output = output.replace("*164", "𐂬")
    output = output.replace("*165", "𐂭")
    output = output.replace("*166", "𐂮")
    output = output.replace("*167", "𐂯")
    output = output.replace("*168", "𐂰")
    output = output.replace("*169", "𐂱")
    output = output.replace("*170", "𐂲")
    output = output.replace("*171", "𐂳")
    output = output.replace("*172", "𐂴")
    output = output.replace("*174", "𐂶")
    output = output.replace("*177", "𐂸")
    output = output.replace("*178", "𐂹")
    output = output.replace("*179", "𐂺")
    output = output.replace("*180", "𐂻")
    output = output.replace("*18", "𐁐")
    output = output.replace("*181", "𐂼")
    output = output.replace("*182", "𐂽")
    output = output.replace("*183", "𐂾")
    output = output.replace("*184", "𐂿")
    output = output.replace("*185", "𐃀")
    output = output.replace("*189", "𐃁")
    output = output.replace("*190", "𐃂")
    output = output.replace("*19", "𐁑")
    output = output.replace("*200", "𐃟")
    output = output.replace("*201", "𐃠")
    output = output.replace("*202", "𐃡")
    output = output.replace("*203", "𐃢")
    output = output.replace("*204", "𐃣")
    output = output.replace("*205", "𐃤")
    output = output.replace("*206", "𐃥")
    output = output.replace("*207", "𐃦")
    output = output.replace("*208", "𐃧")
    output = output.replace("*209", "𐃨")
    output = output.replace("*210", "𐃩")
    output = output.replace("*211", "𐃪")
    output = output.replace("*212", "𐃫")
    output = output.replace("*213", "𐃬")
    output = output.replace("*214", "𐃭")
    output = output.replace("*215", "𐃮")
    output = output.replace("*216", "𐃯")
    output = output.replace("*217", "𐃰")
    output = output.replace("*218", "𐃱")
    output = output.replace("*219", "𐃲")
    output = output.replace("*220", "𐃄")
    output = output.replace("*221", "𐃳")
    output = output.replace("*222", "𐃴")
    output = output.replace("*226", "𐃵")
    output = output.replace("*227", "𐃶")
    output = output.replace("*228", "𐃷")
    output = output.replace("*229", "𐃸")
    output = output.replace("*22", "𐁒")
    output = output.replace("*232", "𐃈")
    output = output.replace("*234", "𐃊")
    output = output.replace("*236", "𐃋")
    output = output.replace("*245", "𐃐")
    output = output.replace("*246", "𐃑")
    output = output.replace("*248", "𐃓")
    output = output.replace("*249", "𐃔")
    output = output.replace("*250", "𐃹")
    output = output.replace("*251", "𐃕")
    output = output.replace("*252", "𐃖")
    output = output.replace("*253", "𐃗")
    output = output.replace("*255", "𐃙")
    output = output.replace("*256", "𐃚")
    output = output.replace("*257", "𐃛")
    output = output.replace("*258", "𐃜")
    output = output.replace("*259", "𐃝")
    output = output.replace("*305", "𐃺")
    output = output.replace("*34", "𐁓")
    output = output.replace("*47", "𐁔")
    output = output.replace("*49", "𐁕")
    output = output.replace("*56", "𐁖")
    output = output.replace("*63", "𐁗")
    output = output.replace("*64", "𐁘")
    output = output.replace("*65", "𐀎")
    output = output.replace("*79", "𐁙")
    output = output.replace("*82", "𐁚")
    output = output.replace("*83", "𐁛")
    output = output.replace("*86", "𐁜")
    output = output.replace("*89", "𐁝")
    output = output.replace("AES", "𐂚")
    output = output.replace("ALVEUS", "𐃅")
    output = output.replace("ARBOR", "𐂷")
    output = output.replace("AREPA", "𐂘")
    output = output.replace("ARMA", "𐂫")
    output = output.replace("AROM", "𐂑")
    output = output.replace("AUR", "𐂛")
    output = output.replace("BIGAE", "𐃌")
    output = output.replace("BOSf", "𐂌")
    output = output.replace("BOSm", "𐂍")
    output = output.replace("CAPSUS", "𐃎")
    output = output.replace("CAPf", "𐂈")
    output = output.replace("CAPm", "𐂉")
    output = output.replace("CERV", "𐂂")
    output = output.replace("CORNU", "𐂠")
    output = output.replace("CURRUS", "𐃍")
    output = output.replace("CYP", "𐂒")
    output = output.replace("DIPTE", "𐃒")
    output = output.replace("EQUf", "𐂄")
    output = output.replace("EQUm", "𐂅")
    output = output.replace("EQU", "𐂃")
    output = output.replace("GALEA", "𐃃")
    output = output.replace("GRA", "𐂎")
    output = output.replace("HASTA", "𐃆")
    output = output.replace("HORD", "𐂏")
    output = output.replace("JACULUM", "𐃘")
    output = output.replace("KANAKO", "𐂔")
    output = output.replace("KAPO", "𐂓")
    output = output.replace("LANA", "𐂝")
    output = output.replace("LUNA", "𐂵")
    output = output.replace("MERI", "𐂙")
    output = output.replace("MUL", "𐂁")
    output = output.replace("OLE", "𐂕")
    output = output.replace("OLIV", "𐂐")
    output = output.replace("OVISf", "𐂆")
    output = output.replace("OVISm", "𐂇")
    output = output.replace("PUGIO", "𐃉")
    output = output.replace("ROTA", "𐃏")
    output = output.replace("SAGITTA", "𐃇")
    output = output.replace("SUSf", "𐂊")
    output = output.replace("SUSm", "𐂋")
    output = output.replace("TELA", "𐂧")
    output = output.replace("TUNICA", "𐂪")
    output = output.replace("TURO2", "𐂤")
    output = output.replace("VIN", "𐂖")
    output = output.replace("VIR", "𐂀")
    output = output.replace("da", "𐀅")
    output = output.replace("de", "𐀆")
    output = output.replace("di", "𐀇")
    output = output.replace("do", "𐀈")
    output = output.replace("du", "𐀉")
    output = output.replace("dwe", "𐁃")
    output = output.replace("dwo", "𐁄")
    output = output.replace("je", "𐀋")
    output = output.replace("jo", "𐀍")
    output = output.replace("ju2", "𐀎")
    output = output.replace("ju", "𐀎")
    output = output.replace("ka", "𐀏")
    output = output.replace("ke", "𐀐")
    output = output.replace("ki", "𐀑")
    output = output.replace("ko", "𐀒")
    output = output.replace("ku", "𐀓")
    output = output.replace("ma", "𐀔")
    output = output.replace("me", "𐀕")
    output = output.replace("mi", "𐀖")
    output = output.replace("mo", "𐀗")
    output = output.replace("mu", "𐀘")
    output = output.replace("na", "𐀙")
    output = output.replace("ne", "𐀚")
    output = output.replace("ni", "𐀛")
    output = output.replace("no", "𐀜")
    output = output.replace("nu", "𐀝")
    output = output.replace("nwa", "𐁅")
    output = output.replace("ja", "𐀊")
    output = output.replace("pa", "𐀞")
    output = output.replace("pe", "𐀟")
    output = output.replace("pi", "𐀠")
    output = output.replace("po", "𐀡")
    output = output.replace("pte", "𐁇")
    output = output.replace("pu2", "𐁆")
    output = output.replace("pu", "𐀢")
    output = output.replace("qa", "𐀣")
    output = output.replace("qe", "𐀤")
    output = output.replace("qi", "𐀥")
    output = output.replace("qo", "𐀦")
    output = output.replace("ra2", "𐁈")
    output = output.replace("ra3", "𐁉")
    output = output.replace("ra", "𐀨")
    output = output.replace("re", "𐀩")
    output = output.replace("ri", "𐀪")
    output = output.replace("ro2", "𐁊")
    output = output.replace("ro", "𐀫")
    output = output.replace("ru", "𐀬")
    output = output.replace("sa", "𐀭")
    output = output.replace("se", "𐀮")
    output = output.replace("si", "𐀯")
    output = output.replace("so", "𐀰")
    output = output.replace("su", "𐀱")
    output = output.replace("ta2", "𐁌")
    output = output.replace("ta", "𐀲")
    output = output.replace("te", "𐀳")
    output = output.replace("ti", "𐀴")
    output = output.replace("to", "𐀵")
    output = output.replace("tu", "𐀶")
    output = output.replace("two", "𐁍")
    output = output.replace("u", "𐀄")
    output = output.replace("wa", "𐀷")
    output = output.replace("we", "𐀸")
    output = output.replace("wi", "𐀹")
    output = output.replace("wo", "𐀺")
    output = output.replace("za", "𐀼")
    output = output.replace("ze", "𐀽")
    output = output.replace("zo", "𐀿")

    output = output.replace("e", "𐀁")
    output = output.replace("a2", "𐁀")
    output = output.replace("a3", "𐁁")
    output = output.replace("a", "𐀀")
    output = output.replace("i", "𐀂")
    output = output.replace("o", "𐀃")

    output = output.replace(",", "𐄀")
    output = output.replace("V", "𐄾")
    output = output.replace("M", "𐄸")
    output = output.replace("N", "𐄹")
    output = output.replace("T", "𐄼")
    output = output.replace("P", "𐄺")
    output = output.replace("Q", "𐄻")
    output = output.replace("L", "𐄷")
    output = output.replace("S", "𐄽")
    output = output.replace("Z", "𐄿")
    
    output = output.split()
    if numbers:
        for i in range(len(output)):
            if output[i].isnumeric():
                num_out = ""
                num = [int(j) for j in output[i]]
                tens = [10**n for n in range(len(num)-1,-1,-1)]
                for j in range(len(tens)):
                    num_out = num_out + script[str(num[j]*tens[j])]
                output[i] = num_out

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
    a = ["apiqoita doe-ra MUL 32",
         "ko-wa me-zo-e 5 ko-wa me-wi-jo-e 15",
         "ko-wo me-wi-jo-e 4"]
    b = [alpha_to_linearb(i) for i in a]
    for i in b:
        print(i)

    for i in b:
        print(linearb_to_alpha(i))
        
