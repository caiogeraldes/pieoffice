#! /usr/bin python3

""" Hieroglyphic Luwian script converter

This scripts allows the user to convert between the latinized transliteration
of Hieroglyphic Luwian and the Hieroglyphic Luwian Script itself with (almost) simple rules.

The file can be imported as a module and contains the following functions:
    alpha_to_luwian - returns a converted string in Hieroglyphic Luwian script from
    a romanized string.
    luwian_to_alpha - returns a converted string in romanized linear B from a
    string in Hieroglyphic Luwian Script. (!!! WILL RETURN PROBLEMATIC DATA DUE
    TO DOUBLE READINGS FOR THE SAME GRAPHEME IN HIEROGLYPHIC LUWIAN)

It also contains a dictionary:
    script - contains the equivalences between romanized and Hieroglyphic Luwian scripts.

Usage
-----

> a = ["MAGNUS.REX MAGNUS-TONITRUS MAGNUS.REX HEROS ka-ra-ka-mi-sà REGIO REX",
>      "???-pa-VIR-ti-sa MAGNUS.REX HEROS INFANS-ní-mu-za",
>      "wa-tu-tá-a CORNU-ra-ti REGIO LIS arha'-SPHINX"]
> b = [alpha_to_luwian(i) for i in a]
> for i in b:
>     print(i)
+ 𔐒  𔖙𔓢  𔐒  𔐕  𔗧𔖱𔗧𔖻𔑶  𔔆  𔐑
+ X𔕸𔕠𔑣𔗔  𔐒  𔐕  𔐰𔓵𔑾𔖪
+ 𔗬𔑢𔐞𔗷  𔒂𔖱𔑣  𔔆  𔐘  𔓹𔒒
> for i in b:
>     print(luwian_to_alpha(i)) # NOTICE THE ERRORS
+ EXPECT ERRORS, THIS FUNCTION IS EXPERIMENTAL
+ MAGNUS.REX MAGNUS-TONITRUS MAGNUS.REX HEROS ka-ra-ka-4-CAPRA REGIO REX
+ EXPECT ERRORS, THIS FUNCTION IS EXPERIMENTAL
+ ???-pa-VIR-PES-sa MAGNUS.REX HEROS INFANS-ní-BOS+MI-za
+ EXPECT ERRORS, THIS FUNCTION IS EXPERIMENTAL
+ wa-tu-tá-a CORNU-ra-PES REGIO LIS FINES+ha-SPHINX

"""

from tools import get_key

script = {
    "EGO" : "𔐀",
    "EGO2" : "𔐁",
    "*003" : "𔐂",
    "MONS2" : "𔐃",
    "*005" : "𔐄",
    "ADORARE" : "𔐅",
    "EDERE" : "𔐆",
    "BIBERE" : "𔐇",
    "AMPLECTI" : "𔐈",
    "CAPUT" : "𔐉",
    "CAPUT+SCALPRUM" : "𔐊",
    "*011" : "𔐋",
    "STATUA" : "𔐌",
    "*013" : "𔐍",
    "pari" : "𔐎",
    "PRAE" : "𔐎",
    "DOMINA" : "𔐏",
    "MAGNUS.DOMINA" : "𔐐",
    "REX" : "𔐑",
    "MAGNUS.REX" : "𔐒",
    "á" : "𔐓",
    "*020" : "𔐔",
    "HEROS" : "𔐕",
    "LOQUI" : "𔐖",
    "*023" : "𔐗",
    "LIS" : "𔐘",
    "OCULUS" : "𔐙",
    "FRONS" : "𔐚",
    "VERSUS" : "𔐛",
    "LIBARE" : "𔐜",
    "FORTIS" : "𔐝",
    "tá" : "𔐞",
    "*030" : "𔐟",
    "PUGNUS+PUGNUS" : "𔐠",
    "LIGARE" : "𔐠",
    "BRACCHIUM" : "𔐡",
    "*033" : "𔐢",
    "POST" : "𔐣",
    "na" : "𔐤",
    "LITUS+na" : "𔐥",
    "*037" : "𔐦",
    "*038" : "𔐧",
    "PUGNUS" : "𔐨",
    "PUGNUS+x" : "𔐩",
    "*040" : "𔐪",
    "tà" : "𔐫",
    "CAPERE" : "𔐫",
    "tà'" : "𔐬",
    "ta-x" : "𔐭",
    "CAPERE2.CAPERE2" : "𔐭",
    "CAPERE2" : "𔐮",
    "*044" : "𔐯",
    "INFANS" : "𔐰",
    "FILIUS" : "𔐰",
    "FRATER" : "𔐰",
    "FILIA" : "𔐱",
    "REX.INFANS.FILIUS" : "𔐲",
    "REX.FILIUS" : "𔐲",
    "REX.FILIA" : "𔐳",
    "MAGNUS.FILIA" : "𔐴",
    "*047" : "𔐵",
    "*048" : "𔐶",
    "a+tá" : "𔐷",
    "*050" : "𔐸",
    "*051" : "𔐹",
    "MANUS.CULTER" : "𔐺",
    "ENSIS" : "𔐻",
    "MANUS+CULTER" : "𔐻",
    "*054" : "𔐼",
    "nì" : "𔐽",
    "ká" : "𔐾",
    "ká'" : "𔐿",
    "SUB" : "𔐿",
    "INFRA" : "𔐿",
    "CUM" : "𔑀",
    "MANUS" : "𔑁",
    "*060" : "𔑂",
    "*061" : "𔑃",
    "MANUS+MINUS" : "𔑄",
    "LONGUS" : "𔑄",
    "*063" : "𔑅",
    "*064" : "𔑆",
    "PONERE" : "𔑇",
    "DARE" : "𔑈",
    "pi" : "𔑈",
    "pi'" : "𔑉",
    "DARE.DARE" : "𔑊",
    "MANDARE" : "𔑊",
    "MANDARE2" : "𔑋",
    "*067" : "𔑌",
    "*068" : "𔑍",
    "*069" : "𔑎",
    "SUPER" : "𔑏",
    "sari" : "𔑏",
    "sara" : "𔑏",
    "*071" : "𔑐",
    "*072" : "𔑑",
    "AURIS+tu+mi" : "𔑒",
    "AUDIRE+tu+mi" : "𔑒",
    "*074" : "𔑓",
    "*075" : "𔑔",
    "*076" : "𔑕",
    "*077" : "𔑖",
    "ALA" : "𔑗",
    "FEMINA" : "𔑘",
    "MATER" : "𔑘",
    "SARMA" : "𔑙",
    "SARMA2" : "𔑚",
    "ta6" : "𔑛",
    "CRUS" : "𔑛",
    "CRUS+FLUMEN" : "𔑜",
    "CRUS2" : "𔑝",
    "nà" : "𔑝",
    "GENUFLECTERE" : "𔑞",
    "CRUS.CRUS" : "𔑟",
    "*087" : "𔑠",
    "*088" : "𔑡",
    "tu" : "𔑢",
    "PES" : "𔑣",
    "ti" : "𔑣",
    "PES.SCALA.ROTAE" : "𔑤",
    "*092" : "𔑥",
    "PES2" : "𔑦",
    "*094" : "𔑧",
    "PES2.PES2" : "𔑨",
    "PES2.PES" : "𔑩",
    "LEO" : "𔑪",
    "BESTIA" : "𔑪",
    "LEO2" : "𔑫",
    "CANIS" : "𔑬",
    "CANIS2" : "𔑭",
    "EQUUS" : "𔑮",
    "ASINUS" : "𔑯",
    "ta" : "𔑯",
    "ta'" : "𔑰",
    "ASINUS2" : "𔑱",
    "ASINUS2A" : "𔑲",
    "CERVUS" : "𔑳",
    "rú" : "𔑳",
    "CERVUS2" : "𔑴",
    "rú'" : "𔑴",
    "rú''" : "𔑵",
    "CERVUS3" : "𔑵",
    "CAPRA" : "𔑶",
    "sà" : "𔑶",
    "sà'" : "𔑷",
    "CAPRA2" : "𔑸",
    "sà''" : "𔑸",
    "CAPRA2A" : "𔑹",
    "sà'''" : "𔑹",
    "BOS" : "𔑺",
    "u" : "𔑺",
    "BOS'" : "𔑻",
    "u'" : "𔑻",
    "BOS2" : "𔑼",
    "u''" : "𔑼",
    "*106" : "𔑽",
    "BOS+MI" : "𔑾",
    "mu" : "𔑾",
    "muwa" : "𔑾",
    "mu'" : "𔑿",
    "muwa'" : "𔑿",
    "BOS.MI" : "𔒀",
    "mu''" : "𔒀",
    "muwa''" : "𔒀",
    "BOS2.MI" : "𔒁",
    "mu'''" : "𔒁",
    "muwa'''" : "𔒁",
    "CORNU" : "𔒂",
    "sú" : "𔒂",
    "VITELLUS" : "𔒃",
    "ma-x" : "𔒃",
    "OVIS" : "𔒄",
    "ma" : "𔒄",
    "ma'" : "𔒅",
    "OVIS2" : "𔒆",
    "ma''" : "𔒆",
    "OVIS3" : "𔒇",
    "LINGERE" : "𔒈",
    "za4" : "𔒈",
    "*113" : "𔒉",
    "LITUUS+U" : "𔒊",
    "LEPUS" : "𔒋",
    "tapa" : "𔒋",
    "LEPUS2" : "𔒌",
    "tapa'" : "𔒌",
    "*116" : "𔒍",
    "*117" : "𔒎",
    "*118" : "𔒏",
    "*119" : "𔒐",
    "GRYLLUS" : "𔒑",
    "SPHINX" : "𔒒",
    "*122" : "𔒓",
    "*123" : "𔒔",
    "*124" : "𔒕",
    "lí'" : "𔒖",
    "UNGULA" : "𔒗",
    "li-x" : "𔒗",
    "*126" : "𔒘",
    "*127" : "𔒙",
    "AVIS" : "𔒚",
    "zi4" : "𔒚",
    "*129" : "𔒛",
    "AVIS3" : "𔒜",
    "AVIS5" : "𔒝",
    "AVIS2" : "𔒞",
    "AQUILA" : "𔒟",
    "AVIS4" : "𔒟",
    "ara" : "𔒟",
    "ari" : "𔒟",
    "ara'" : "𔒠",
    "ari'" : "𔒠",
    "AVIS-x" : "𔒡",
    "*135A" : "𔒢",
    "*136" : "𔒣",
    "LIBATIO" : "𔒤",
    "PISCIS" : "𔒥",
    "*139" : "𔒦",
    "*140" : "𔒧",
    "*141" : "𔒨",
    "*142" : "𔒩",
    "*143" : "𔒪",
    "*144" : "𔒫",
    "*145" : "𔒬",
    "*146" : "𔒭",
    "*147" : "𔒮",
    "JANUS" : "𔒯",
    "*149" : "𔒰",
    "*150" : "𔒱",
    "TELIPINU" : "𔒲",
    "*152" : "𔒳",
    "nu" : "𔒴",
    "*154" : "𔒵",
    "*155" : "𔒶",
    "*156" : "𔒷",
    "*157" : "𔒸",
    "*158" : "𔒹",
    "*159" : "𔒺",
    "VITIS" : "𔒻",
    "wi'" : "𔒻",
    "wi(ya)" : "𔒻",
    "*161" : "𔒼",
    "*162" : "𔒽",
    "*163" : "𔒾",
    "*164" : "𔒿",
    "BONUS" : "𔓀",
    "wà" : "𔓀",
    "wì" : "𔓀",
    "wá" : "𔓁",
    "wí" : "𔓁",
    "*167" : "𔓂",
    "*168" : "𔓃",
    "*169" : "𔓄",
    "*170" : "𔓅",
    "*171" : "𔓆",
    "ta5" : "𔓇",
    "ti5" : "𔓇",
    "lá" : "𔓇",
    "lí" : "𔓇",
    "HASTARIUS" : "𔓈",
    "si" : "𔓉",
    "LINGUA" : "𔓊",
    "la" : "𔓊",
    "la+la" : "𔓋",
    "LINGUA+CLAVUS" : "𔓌",
    "la+ra+a" : "𔓍",
    "HORDEUM" : "𔓎",
    "hwi-x" : "𔓎",
    "*180" : "𔓏",
    "PANIS" : "𔓐",
    "pa-x" : "𔓐",
    "CAELUM" : "𔓑",
    "*183" : "𔓒",
    "*184" : "𔓓",
    "*185" : "𔓔",
    "*186" : "𔓕",
    "*187" : "𔓖",
    "*188" : "𔓗",
    "*189" : "𔓘",
    "SOL2" : "𔓙",
    "SOL" : "𔓚",
    "ORIENS" : "𔓛",
    "LUNA" : "𔓜",
    "*194" : "𔓝",
    "*195" : "𔓞",
    "HATTI" : "𔓟",
    "há" : "𔓟",
    "HATTI+LI" : "𔓠",
    "HATTUSILI" : "𔓠",
    "há-li" : "𔓠",
    "*198" : "𔓡",
    "TONITRUS" : "𔓢",
    "FULGUR" : "𔓣",
    "TERRA" : "𔓤",
    "LOCUS" : "𔓤",
    "wa6" : "𔓤",
    "wi6" : "𔓤",
    "VIA+TERRA.SCALPRUM" : "𔓥",
    "VIA+TERRA+SCALPRUM" : "𔓦",
    "(DEUS)VIA+TERRA" : "𔓧",
    "*203" : "𔓨",
    "wa5" : "𔓩",
    "wi5" : "𔓩",
    "*205" : "𔓪",
    "*206" : "𔓫",
    "MONS" : "𔓬",
    "wa5'" : "𔓬",
    "wi5'" : "𔓬",
    "LEO+MONS.tu+LEO" : "𔓭",
    "*208" : "𔓮",
    "i" : "𔓯",
    "i(a)" : "𔓯",
    "i+ra" : "𔓰",
    "i+ri" : "𔓰",
    "ia" : "𔓱",
    "*211" : "𔓲",
    "FLUMEN" : "𔓳",
    "*213" : "𔓴",
    "ní" : "𔓵",
    "FONS" : "𔓶",
    "ha" : "𔓷",
    "FINES" : "𔓸",
    "arha" : "𔓸",
    "FINES+ha" : "𔓹",
    "arha'" : "𔓹",
    "*217" : "𔓺",
    "*218" : "𔓻",
    "*219" : "𔓼",
    "*220" : "𔓽",
    "VIA" : "𔓾",
    "*222" : "𔓿",
    "sa6" : "𔔀",
    "*224" : "𔔁",
    "URBS" : "𔔂",
    "ISHUWA" : "𔔃",
    "*227" : "𔔄",
    "URBS+li" : "𔔅",
    "URBS-li" : "𔔅",
    "MURSILI" : "𔔅",
    "REGIO" : "𔔆",
    "tu4" : "𔔆",
    "mí.REGIO" : "𔔇",
    "*230" : "𔔈",
    "CASTRUM" : "𔔉",
    "*232" : "𔔊",
    "*233" : "𔔋",
    "*234" : "𔔌",
    "*235" : "𔔍",
    "*236" : "𔔎",
    "PORTA" : "𔔏",
    "*238" : "𔔐",
    "PORTA2" : "𔔑",
    "*240" : "𔔒",
    "ki-x" : "𔔓",
    "*242" : "𔔔",
    "CUBITUM" : "𔔕",
    "AEDIFICIUM" : "𔔖",
    "VACUUS" : "𔔗",
    "AEDIFICIUM+MINUS" : "𔔗",
    "AEDIFICARE" : "𔔘",
    "AEDIFICIUM.PONERE" : "𔔘",
    "DOMUS" : "𔔙",
    "DELERE" : "𔔚",
    "DOMUS+MINUS" : "𔔚",
    "DEUS.DOMUS" : "𔔛",
    "MAGNUS.DOMUS" : "𔔜",
    "DOMUS+x" : "𔔝",
    "DOMUS+SCALA" : "𔔞",
    "*253" : "𔔟",
    "EUNUCHUS2" : "𔔠",
    "HORREUM" : "𔔡",
    "*256" : "𔔢",
    "ARGENTUM" : "𔔣",
    "*258" : "𔔤",
    "*259" : "𔔥",
    "*260" : "𔔦",
    "*261" : "𔔧",
    "*262" : "𔔨",
    "*263" : "𔔩",
    "PODIUM" : "𔔪",
    "*265" : "𔔫",
    "PES.REGIO" : "𔔬",
    "STELE" : "𔔭",
    "LAPIS+SCALPRUM" : "𔔭",
    "LAPIS" : "𔔮",
    "SCALPRUM" : "𔔯",
    "EXERCITUS" : "𔔰",
    "*270" : "𔔱",
    "*271" : "𔔲",
    "SCUTUM" : "𔔳",
    "*273" : "𔔴",
    "*274" : "𔔵",
    "*275" : "𔔶",
    "FRATER2" : "𔔷",
    "IUDEX.la" : "𔔸",
    "IUDEX+la" : "𔔸",
    "li" : "𔔹",
    "*279" : "𔔺",
    "MALLEUS" : "𔔻",
    "wa9" : "𔔻",
    "wi9" : "𔔻",
    "ASCIA" : "𔔼",
    "*282" : "𔔽",
    "tuzzi" : "𔔾",
    "*284" : "𔔿",
    "IACULUM" : "𔕀",
    "*285" : "𔕀",
    "zuwa" : "𔕀",
    "wa7" : "𔕁",
    "wi7" : "𔕁",
    "*287" : "𔕂",
    "CURRUS" : "𔕃",
    "AURIGA" : "𔕄",
    "AURIGA2" : "𔕅",
    "hara" : "𔕆",
    "hari" : "𔕆",
    "lì" : "𔕇",
    "ROTA" : "𔕈",
    "hala" : "𔕈",
    "hali" : "𔕈",
    "*293" : "𔕉",
    "THRONUS" : "𔕊",
    "MENSA" : "𔕊",
    "THRONUS'" : "𔕋",
    "MENSA2" : "𔕋",
    "SARPA" : "𔕋",
    "SOL2.THRONUS/MENSA" : "𔕌",
    "*295" : "𔕌",
    "(DEUS)MONS.SARPA" : "𔕍",
    "(DEUS)MONS.MENSA" : "𔕍",
    "THRONUS''" : "𔕍",
    "*297" : "𔕎",
    "THRONUS2" : "𔕏",
    "SOLIUM" : "𔕐",
    "í" : "𔕐",
    "iá" : "𔕑",
    "NEPOS" : "𔕒",
    "LECTUS" : "𔕓",
    "*302" : "𔕔",
    "SARA" : "𔕕",
    "SARI" : "𔕕",
    "mà" : "𔕖",
    "FUSUS" : "𔕗",
    "hí" : "𔕘",
    "hu" : "𔕙",
    "*308" : "𔕚",
    "CRUX" : "𔕛",
    "CRUX2" : "𔕜",
    "*310" : "𔕝",
    "*311" : "𔕞",
    "*312" : "𔕟",
    "VIR" : "𔕠",
    "zí" : "𔕠",
    "ha-x" : "𔕡",
    "kar" : "𔕢",
    "sa7" : "𔕣",
    "*317" : "𔕤",
    "TESHUB" : "𔕥",
    "ta4" : "𔕦",
    "ti4" : "𔕦",
    "la'" : "𔕦"   ,
    "li'" : "𔕦",
    "*320" : "𔕧",
    "*321" : "𔕨",
    "PURUS" : "𔕩",
    "*323" : "𔕪",
    "*324" : "𔕫",
    "tú" : "𔕬",
    "SCRIBA" : "𔕭",
    "tù" : "𔕭",
    "SIGILLUM" : "𔕮",
    "sa5" : "𔕮",
    "pu" : "𔕯",
    "REL" : "𔕰",
    "kwi" : "𔕰",
    "kwa" : "𔕰",
    "*329A" : "𔕱",
    "CAPERE+SCALPRUM" : "𔕲",
    "AVUS" : "𔕳",
    "NEG" : "𔕴",
    "NEG2" : "𔕵",
    "ná" : "𔕵",
    "NEG3" : "𔕶",
    "*333" : "𔕷",
    "pa" : "𔕸",
    "zá" : "𔕹",
    "ANNUS" : "𔕺",
    "PITHOS.SCUTELLA" : "𔕺",
    "PITHOS" : "𔕺",
    "zì" : "𔕺",
    "zì'" : "𔕻",
    "zà" : "𔕼",
    "za-x" : "𔕽",
    "PITHOS'" : "𔕾",
    "CULTER" : "𔕿",
    "*339" : "𔖀",
    "ANNUS+ANNUS" : "𔖁",
    "VAS" : "𔖂",
    "*342" : "𔖃",
    "PITHOS''" : "𔖄",
    "CONTRACTUS" : "𔖅",
    "URCEUS" : "𔖆",
    "POCULUM" : "𔖇",
    "hú" : "𔖈",
    "*348" : "𔖉",
    "*349" : "𔖊",
    "*350" : "𔖋",
    "*351" : "𔖌",
    "*352" : "𔖍",
    "*353" : "𔖎",
    "*354" : "𔖏",
    "SACERDOS" : "𔖐",
    "*356" : "𔖑",
    "*357" : "𔖒",
    "DIES" : "𔖓",
    "*359" : "𔖔",
    "*359A" : "𔖕",
    "DEUS" : "𔖖",
    "*361" : "𔖗",
    "má" : "𔖘",
    "MAGNUS" : "𔖙",
    "ur" : "𔖙",
    "u'''" : "𔖚",
    "mu''''" : "𔖛",
    "*365" : "𔖜",
    "OMNIS(+mi)" : "𔖝",
    "tala" : "𔖞",
    "MALUS" : "𔖟",
    "MALUS2" : "𔖠",
    "VITA" : "𔖡",
    "BONUS2" : "𔖢",
    "su" : "𔖢",
    "IUSTITIA" : "𔖣",
    "IUDEX" : "𔖣",
    "IUDEX+ra" : "𔖤",
    "IUDEX+ri" : "𔖤",
    "IUDEX+tara" : "𔖤",
    "IUDEX+tari" : "𔖤",
    "SACERDOS2" : "𔖥",
    "*373" : "𔖦",
    "*374" : "𔖧",
    "*375" : "𔖨",
    "zi" : "𔖩",
    "za'" : "𔖩",
    "za" : "𔖪",
    "LITUUS" : "𔖫",
    "OCCIDENS" : "𔖬",
    "ià" : "𔖬",
    "1" : "𔖭",
    "UNUS" : "𔖭",
    "sa8" : "𔖭",
    "MINUS" : "𔖮",
    "MORI" : "𔖯",
    "VI2.MINUS" : "𔖯",
    "lignum" : "𔖰",
    "ra" : "𔖱",
    "ri" : "𔖱",
    "'" : "𔖲",
    "2" : "𔖳",
    "2'" : "𔖴",
    "VIR2" : "𔖵",
    "WD" : "𔖵",
    "VIR2A" : "𔖶",
    "SERVUS" : "𔖷",
    "mì" : "𔖷",
    "3" : "𔖸",
    "tara'" : "𔖸",
    "tari'" : "𔖸",
    "tara" : "𔖹",
    "tari" : "𔖹",
    "DOMINUS" : "𔖺",
    "4" : "𔖻",
    "mi" : "𔖻",
    "5" : "𔖼",
    "8" : "𔖽",
    "*394" : "𔖾",
    "9" : "𔖿",
    "nú" : "𔖿",
    "*396" : "𔗀",
    "10" : "𔗁",
    "DECEM" : "𔗁",
    "*398" : "𔗂",
    "100" : "𔗃",
    "CENTUM" : "𔗃",
    "1000" : "𔗄",
    "MILLE" : "𔗄",
    "*401" : "𔗅",
    "SCUTELLA" : "𔗆",
    "sa4" : "𔗆",
    "*403" : "𔗇",
    "ANIMAL" : "𔗈",
    "*405" : "𔗉",
    "*406" : "𔗊",
    "*407" : "𔗋",
    "*408" : "𔗌",
    "*409" : "𔗍",
    "<" : "𔗎",
    ">" : "𔗏",
    "ni" : "𔗐",
    "ru" : "𔗑",
    "hi" : "𔗒",
    "*414" : "𔗓",
    "sa" : "𔗔",
    "*416" : "𔗕",
    "sa-x" : "𔗖",
    "*418" : "𔗗",
    "mí" : "𔗘",
    "urhi" : "𔗘",
    "*420" : "𔗙",
    "us" : "𔗚",
    "PANIS.SCUTELLA" : "𔗛",
    "ku" : "𔗜",
    "*424" : "𔗝",
    "*425" : "𔗞",
    "*426" : "𔗟",
    "*427" : "𔗠",
    "*428" : "𔗡",
    "tana" : "𔗢",
    "OMNIS2" : "𔗣",
    "pú" : "𔗣",
    "*431" : "𔗤",
    "*432" : "𔗥",
    "sá" : "𔗦",
    "ka" : "𔗧",
    "a-x" : "𔗨",
    "*436" : "𔗩",
    "*437" : "𔗪",
    "PASTOR" : "𔗫",
    "wa" : "𔗬",
    "wi" : "𔗬",
    "*440" : "𔗭",
    "*441" : "𔗮",
    "*442" : "𔗯",
    "*443" : "𔗰",
    "*444" : "𔗱",
    "la''" : "𔗲",
    "li''" : "𔗲",
    "lu" : "𔗲",
    "ki" : "𔗳",
    "ni-x" : "𔗴",
    "*448" : "𔗵",
    "*449" : "𔗶",
    "a" : "𔗷",
    "WE" : "𔗷",
    "a+ra" : "𔗸",
    "a+ri" : "𔗸",
    "huru" : "𔗹",
    "*452" : "𔗺",
    "*453" : "𔗻",
    "*454" : "𔗼",
    "la-x" : "𔗽",
    "sí-x" : "𔗾",
    "*457" : "𔗿",
    "*457A" : "𔘀",
    "*458" : "𔘁",
    "*459" : "𔘂",
    "*460" : "𔘃",
    "ma-x'" : "𔘄",
    "*462" : "𔘅",
    "*463" : "𔘆",
    "*464" : "𔘇",
    "*465" : "𔘈",
    "*466" : "𔘉",
    "*467" : "𔘊",
    "*468" : "𔘋",
    "*469" : "𔘌",
    "12" : "𔘍",
    "*471" : "𔘎",
    "*472" : "𔘏",
    "*473" : "𔘐",
    "EUNUCHUS" : "𔘑",
    "*475" : "𔘒",
    "*476" : "𔘓",
    "*477" : "𔘔",
    "*478" : "𔘕",
    "*479" : "𔘖",
    "*480" : "𔘗",
    "*481" : "𔘘",
    "*482" : "𔘙",
    "*483" : "𔘚",
    "*484" : "𔘛",
    "*485" : "𔘜",
    "*486" : "𔘝",
    "*487" : "𔘞",
    "tí" : "𔘟",
    "*489" : "𔘠",
    "*490" : "𔘡",
    "*491" : "𔘢",
    "*492" : "𔘣",
    "*493" : "𔘤",
    "*494" : "𔘥",
    "*495" : "𔘦",
    "*496" : "𔘧",
    "*497" : "𔘨",
    "*501" : "𔘩",
    "*502" : "𔘪",
    "*503" : "𔘫",
    "*504" : "𔘬",
    "*505" : "𔘭",
    "hana" : "𔘮",
    "*507" : "𔘯",
    "CURRERE" : "𔘰",
    "hwi'" : "𔘰",
    "hwa'" : "𔘰",
    "*509" : "𔘱",
    "*510" : "𔘲",
    "*511" : "𔘳",
    "*512" : "𔘴",
    "*513" : "𔘵",
    "*514" : "𔘶",
    "*515" : "𔘷",
    "*516" : "𔘸",
    "*517" : "𔘹",
    "*518" : "𔘺",
    "*519" : "𔘻",
    "*520" : "𔘼",
    "*521" : "𔘽",
    "*522" : "𔘾",
    "*523" : "𔘿",
    "PROPHETA" : "𔙀",
    "CORNU+CAPUT" : "𔙀",
    "PRINCEPS" : "𔙁",
    "*526" : "𔙂",
    "APER" : "𔙃",
    "tì" : "𔙄",
    "LINGUA-x" : "𔙅",
    "*530" : "𔙆",
    "???": "X"
        }


def alpha_to_luwian(input):
    """ Converts text in Latin Alphabet to Hieroglyphic Luwian Script

    Each syllable should be separated by a sing dash, each word by a space.

    Parameters
    ----------
    input : str
        Text input with syllables separated by dashes and words by spaces.

    Returns
    -------
    output : str
        Transliterated text in Hieroglyphic Luwian Script

    Usage
    -----

    > alpha_to_luwian("EGO-mi u'-ra-hi-li-na")
    + '𔐀𔖻  𔑻𔖱𔗒𔔹𔐤'

    """
    output = input.replace("-","")


    output = output.replace("(DEUS)MONS.MENSA", "𔕍")
    output = output.replace("(DEUS)MONS.SARPA", "𔕍")
    output = output.replace("(DEUS)VIA+TERRA", "𔓧")

    # ASIGNS

    output = output.replace("*003", "𔐂")
    output = output.replace("*005", "𔐄")
    output = output.replace("*011", "𔐋")
    output = output.replace("*013", "𔐍")
    output = output.replace("*020", "𔐔")
    output = output.replace("*023", "𔐗")
    output = output.replace("*030", "𔐟")
    output = output.replace("*033", "𔐢")
    output = output.replace("*037", "𔐦")
    output = output.replace("*038", "𔐧")
    output = output.replace("*040", "𔐪")
    output = output.replace("*044", "𔐯")
    output = output.replace("*047", "𔐵")
    output = output.replace("*048", "𔐶")
    output = output.replace("*050", "𔐸")
    output = output.replace("*051", "𔐹")
    output = output.replace("*054", "𔐼")
    output = output.replace("*060", "𔑂")
    output = output.replace("*061", "𔑃")
    output = output.replace("*063", "𔑅")
    output = output.replace("*064", "𔑆")
    output = output.replace("*067", "𔑌")
    output = output.replace("*068", "𔑍")
    output = output.replace("*069", "𔑎")
    output = output.replace("*071", "𔑐")
    output = output.replace("*072", "𔑑")
    output = output.replace("*074", "𔑓")
    output = output.replace("*075", "𔑔")
    output = output.replace("*076", "𔑕")
    output = output.replace("*077", "𔑖")
    output = output.replace("*087", "𔑠")
    output = output.replace("*088", "𔑡")
    output = output.replace("*092", "𔑥")
    output = output.replace("*094", "𔑧")
    output = output.replace("*106", "𔑽")
    output = output.replace("*113", "𔒉")
    output = output.replace("*116", "𔒍")
    output = output.replace("*117", "𔒎")
    output = output.replace("*118", "𔒏")
    output = output.replace("*119", "𔒐")
    output = output.replace("*122", "𔒓")
    output = output.replace("*123", "𔒔")
    output = output.replace("*124", "𔒕")
    output = output.replace("*126", "𔒘")
    output = output.replace("*127", "𔒙")
    output = output.replace("*129", "𔒛")
    output = output.replace("*135A", "𔒢")
    output = output.replace("*136", "𔒣")
    output = output.replace("*139", "𔒦")
    output = output.replace("*140", "𔒧")
    output = output.replace("*141", "𔒨")
    output = output.replace("*142", "𔒩")
    output = output.replace("*143", "𔒪")
    output = output.replace("*144", "𔒫")
    output = output.replace("*145", "𔒬")
    output = output.replace("*146", "𔒭")
    output = output.replace("*147", "𔒮")
    output = output.replace("*149", "𔒰")
    output = output.replace("*150", "𔒱")
    output = output.replace("*152", "𔒳")
    output = output.replace("*154", "𔒵")
    output = output.replace("*155", "𔒶")
    output = output.replace("*156", "𔒷")
    output = output.replace("*157", "𔒸")
    output = output.replace("*158", "𔒹")
    output = output.replace("*159", "𔒺")
    output = output.replace("*161", "𔒼")
    output = output.replace("*162", "𔒽")
    output = output.replace("*163", "𔒾")
    output = output.replace("*164", "𔒿")
    output = output.replace("*167", "𔓂")
    output = output.replace("*168", "𔓃")
    output = output.replace("*169", "𔓄")
    output = output.replace("*170", "𔓅")
    output = output.replace("*171", "𔓆")
    output = output.replace("*180", "𔓏")
    output = output.replace("*183", "𔓒")
    output = output.replace("*184", "𔓓")
    output = output.replace("*185", "𔓔")
    output = output.replace("*186", "𔓕")
    output = output.replace("*187", "𔓖")
    output = output.replace("*188", "𔓗")
    output = output.replace("*189", "𔓘")
    output = output.replace("*194", "𔓝")
    output = output.replace("*195", "𔓞")
    output = output.replace("*198", "𔓡")
    output = output.replace("*203", "𔓨")
    output = output.replace("*205", "𔓪")
    output = output.replace("*206", "𔓫")
    output = output.replace("*208", "𔓮")
    output = output.replace("*211", "𔓲")
    output = output.replace("*213", "𔓴")
    output = output.replace("*217", "𔓺")
    output = output.replace("*218", "𔓻")
    output = output.replace("*219", "𔓼")
    output = output.replace("*220", "𔓽")
    output = output.replace("*222", "𔓿")
    output = output.replace("*224", "𔔁")
    output = output.replace("*227", "𔔄")
    output = output.replace("*230", "𔔈")
    output = output.replace("*232", "𔔊")
    output = output.replace("*233", "𔔋")
    output = output.replace("*234", "𔔌")
    output = output.replace("*235", "𔔍")
    output = output.replace("*236", "𔔎")
    output = output.replace("*238", "𔔐")
    output = output.replace("*240", "𔔒")
    output = output.replace("*242", "𔔔")
    output = output.replace("*253", "𔔟")
    output = output.replace("*256", "𔔢")
    output = output.replace("*258", "𔔤")
    output = output.replace("*259", "𔔥")
    output = output.replace("*260", "𔔦")
    output = output.replace("*261", "𔔧")
    output = output.replace("*262", "𔔨")
    output = output.replace("*263", "𔔩")
    output = output.replace("*265", "𔔫")
    output = output.replace("*270", "𔔱")
    output = output.replace("*271", "𔔲")
    output = output.replace("*273", "𔔴")
    output = output.replace("*274", "𔔵")
    output = output.replace("*275", "𔔶")
    output = output.replace("*279", "𔔺")
    output = output.replace("*282", "𔔽")
    output = output.replace("*284", "𔔿")
    output = output.replace("*285", "𔕀")
    output = output.replace("*287", "𔕂")
    output = output.replace("*293", "𔕉")
    output = output.replace("*295", "𔕌")
    output = output.replace("*297", "𔕎")
    output = output.replace("*302", "𔕔")
    output = output.replace("*308", "𔕚")
    output = output.replace("*310", "𔕝")
    output = output.replace("*311", "𔕞")
    output = output.replace("*312", "𔕟")
    output = output.replace("*317", "𔕤")
    output = output.replace("*320", "𔕧")
    output = output.replace("*321", "𔕨")
    output = output.replace("*323", "𔕪")
    output = output.replace("*324", "𔕫")
    output = output.replace("*329A", "𔕱")
    output = output.replace("*333", "𔕷")
    output = output.replace("*339", "𔖀")
    output = output.replace("*342", "𔖃")
    output = output.replace("*348", "𔖉")
    output = output.replace("*349", "𔖊")
    output = output.replace("*350", "𔖋")
    output = output.replace("*351", "𔖌")
    output = output.replace("*352", "𔖍")
    output = output.replace("*353", "𔖎")
    output = output.replace("*354", "𔖏")
    output = output.replace("*356", "𔖑")
    output = output.replace("*357", "𔖒")
    output = output.replace("*359A", "𔖕")
    output = output.replace("*359", "𔖔")
    output = output.replace("*361", "𔖗")
    output = output.replace("*365", "𔖜")
    output = output.replace("*373", "𔖦")
    output = output.replace("*374", "𔖧")
    output = output.replace("*375", "𔖨")
    output = output.replace("*394", "𔖾")
    output = output.replace("*396", "𔗀")
    output = output.replace("*398", "𔗂")
    output = output.replace("*401", "𔗅")
    output = output.replace("*403", "𔗇")
    output = output.replace("*405", "𔗉")
    output = output.replace("*406", "𔗊")
    output = output.replace("*407", "𔗋")
    output = output.replace("*408", "𔗌")
    output = output.replace("*409", "𔗍")
    output = output.replace("*414", "𔗓")
    output = output.replace("*416", "𔗕")
    output = output.replace("*418", "𔗗")
    output = output.replace("*420", "𔗙")
    output = output.replace("*424", "𔗝")
    output = output.replace("*425", "𔗞")
    output = output.replace("*426", "𔗟")
    output = output.replace("*427", "𔗠")
    output = output.replace("*428", "𔗡")
    output = output.replace("*431", "𔗤")
    output = output.replace("*432", "𔗥")
    output = output.replace("*436", "𔗩")
    output = output.replace("*437", "𔗪")
    output = output.replace("*440", "𔗭")
    output = output.replace("*441", "𔗮")
    output = output.replace("*442", "𔗯")
    output = output.replace("*443", "𔗰")
    output = output.replace("*444", "𔗱")
    output = output.replace("*448", "𔗵")
    output = output.replace("*449", "𔗶")
    output = output.replace("*452", "𔗺")
    output = output.replace("*453", "𔗻")
    output = output.replace("*454", "𔗼")
    output = output.replace("*457A", "𔘀")
    output = output.replace("*457", "𔗿")
    output = output.replace("*458", "𔘁")
    output = output.replace("*459", "𔘂")
    output = output.replace("*460", "𔘃")
    output = output.replace("*462", "𔘅")
    output = output.replace("*463", "𔘆")
    output = output.replace("*464", "𔘇")
    output = output.replace("*465", "𔘈")
    output = output.replace("*466", "𔘉")
    output = output.replace("*467", "𔘊")
    output = output.replace("*468", "𔘋")
    output = output.replace("*469", "𔘌")
    output = output.replace("*471", "𔘎")
    output = output.replace("*472", "𔘏")
    output = output.replace("*473", "𔘐")
    output = output.replace("*475", "𔘒")
    output = output.replace("*476", "𔘓")
    output = output.replace("*477", "𔘔")
    output = output.replace("*478", "𔘕")
    output = output.replace("*479", "𔘖")
    output = output.replace("*480", "𔘗")
    output = output.replace("*481", "𔘘")
    output = output.replace("*482", "𔘙")
    output = output.replace("*483", "𔘚")
    output = output.replace("*484", "𔘛")
    output = output.replace("*485", "𔘜")
    output = output.replace("*486", "𔘝")
    output = output.replace("*487", "𔘞")
    output = output.replace("*489", "𔘠")
    output = output.replace("*490", "𔘡")
    output = output.replace("*491", "𔘢")
    output = output.replace("*492", "𔘣")
    output = output.replace("*493", "𔘤")
    output = output.replace("*494", "𔘥")
    output = output.replace("*495", "𔘦")
    output = output.replace("*496", "𔘧")
    output = output.replace("*497", "𔘨")
    output = output.replace("*501", "𔘩")
    output = output.replace("*502", "𔘪")
    output = output.replace("*503", "𔘫")
    output = output.replace("*504", "𔘬")
    output = output.replace("*505", "𔘭")
    output = output.replace("*507", "𔘯")
    output = output.replace("*509", "𔘱")
    output = output.replace("*510", "𔘲")
    output = output.replace("*511", "𔘳")
    output = output.replace("*512", "𔘴")
    output = output.replace("*513", "𔘵")
    output = output.replace("*514", "𔘶")
    output = output.replace("*515", "𔘷")
    output = output.replace("*516", "𔘸")
    output = output.replace("*517", "𔘹")
    output = output.replace("*518", "𔘺")
    output = output.replace("*519", "𔘻")
    output = output.replace("*520", "𔘼")
    output = output.replace("*521", "𔘽")
    output = output.replace("*522", "𔘾")
    output = output.replace("*523", "𔘿")
    output = output.replace("*526", "𔙂")
    output = output.replace("*530", "𔙆")

    output = output.replace("ADORARE", "𔐅")
    output = output.replace("AEDIFICARE", "𔔘")
    output = output.replace("AEDIFICIUM+MINUS", "𔔗")
    output = output.replace("AEDIFICIUM.PONERE", "𔔘")
    output = output.replace("AEDIFICIUM", "𔔖")
    output = output.replace("ALA", "𔑗")
    output = output.replace("AMPLECTI", "𔐈")
    output = output.replace("ANIMAL", "𔗈")
    output = output.replace("ANNUS+ANNUS", "𔖁")
    output = output.replace("ANNUS", "𔕺")
    output = output.replace("APER", "𔙃")
    output = output.replace("AQUILA", "𔒟")
    output = output.replace("ARGENTUM", "𔔣")
    output = output.replace("ASCIA", "𔔼")
    output = output.replace("ASINUS", "𔑯")
    output = output.replace("ASINUS2", "𔑱")
    output = output.replace("ASINUS2A", "𔑲")
    output = output.replace("AUDIRE+tu+mi", "𔑒")
    output = output.replace("AURIGA", "𔕄")
    output = output.replace("AURIGA2", "𔕅")
    output = output.replace("AURIS+tu+mi", "𔑒")
    output = output.replace("AVIS2", "𔒞")
    output = output.replace("AVIS3", "𔒜")
    output = output.replace("AVIS4", "𔒟")
    output = output.replace("AVIS5", "𔒝")
    output = output.replace("AVIS-x", "𔒡")
    output = output.replace("AVIS", "𔒚")
    output = output.replace("AVUS", "𔕳")
    output = output.replace("BESTIA", "𔑪")
    output = output.replace("BIBERE", "𔐇")
    output = output.replace("BONUS2", "𔖢")
    output = output.replace("BONUS", "𔓀")
    output = output.replace("BOS+MI", "𔑾")
    output = output.replace("BOS.MI", "𔒀")
    output = output.replace("BOS'", "𔑻")
    output = output.replace("BOS", "𔑺")
    output = output.replace("BOS2.MI", "𔒁")
    output = output.replace("BOS2", "𔑼")
    output = output.replace("BRACCHIUM", "𔐡")
    output = output.replace("CAELUM", "𔓑")
    output = output.replace("CANIS2", "𔑭")
    output = output.replace("CANIS", "𔑬")
    output = output.replace("CAPERE+SCALPRUM", "𔕲")
    output = output.replace("CAPERE2.CAPERE2", "𔐭")
    output = output.replace("CAPERE2", "𔐮")
    output = output.replace("CAPERE", "𔐫")
    output = output.replace("CAPRA2A", "𔑹")
    output = output.replace("CAPRA2", "𔑸")
    output = output.replace("CAPRA", "𔑶")
    output = output.replace("CAPUT+SCALPRUM", "𔐊")
    output = output.replace("CAPUT", "𔐉")
    output = output.replace("CASTRUM", "𔔉")
    output = output.replace("CENTUM", "𔗃")
    output = output.replace("CERVUS3", "𔑵")
    output = output.replace("CERVUS2", "𔑴")
    output = output.replace("CERVUS", "𔑳")
    output = output.replace("CONTRACTUS", "𔖅")
    output = output.replace("CORNU+CAPUT", "𔙀")
    output = output.replace("CORNU", "𔒂")
    output = output.replace("CRUS+FLUMEN", "𔑜")
    output = output.replace("CRUS.CRUS", "𔑟")
    output = output.replace("CRUS2", "𔑝")
    output = output.replace("CRUS", "𔑛")
    output = output.replace("CRUX2", "𔕜")
    output = output.replace("CRUX", "𔕛")
    output = output.replace("CUBITUM", "𔔕")
    output = output.replace("CUM", "𔑀")
    output = output.replace("CURRERE", "𔘰")
    output = output.replace("CURRUS", "𔕃")
    output = output.replace("DARE.DARE", "𔑊")
    output = output.replace("DARE", "𔑈")
    output = output.replace("DECEM", "𔗁")
    output = output.replace("DELERE", "𔔚")
    output = output.replace("DEUS.DOMUS", "𔔛")
    output = output.replace("DEUS", "𔖖")
    output = output.replace("DIES", "𔖓")

    # MAGNUS
    output = output.replace("MAGNUS.DOMINA", "𔐐")
    output = output.replace("MAGNUS.DOMUS", "𔔜")
    output = output.replace("MAGNUS.FILIA", "𔐴")
    output = output.replace("MAGNUS.REX", "𔐒")

    # REX

    output = output.replace("REX.FILIA", "𔐳")
    output = output.replace("REX.FILIUS", "𔐲")
    output = output.replace("REX.INFANS.FILIUS", "𔐲")

    output = output.replace("MAGNUS", "𔖙")
    output = output.replace("DOMINA", "𔐏")
    output = output.replace("DOMINUS", "𔖺")
    output = output.replace("FEMINA", "𔑘")
    output = output.replace("FILIA", "𔐱")
    output = output.replace("FILIUS", "𔐰")
    output = output.replace("DOMUS+MINUS", "𔔚")
    output = output.replace("DOMUS+SCALA", "𔔞")
    output = output.replace("DOMUS+x", "𔔝")
    output = output.replace("DOMUS", "𔔙")
    output = output.replace("EDERE", "𔐆")
    output = output.replace("EGO2", "𔐁")
    output = output.replace("EGO", "𔐀")
    output = output.replace("ENSIS", "𔐻")
    output = output.replace("EQUUS", "𔑮")
    output = output.replace("EUNUCHUS2", "𔔠")
    output = output.replace("EUNUCHUS", "𔘑")
    output = output.replace("EXERCITUS", "𔔰")
    output = output.replace("FINES+ha", "𔓹")
    output = output.replace("FINES", "𔓸")
    output = output.replace("FLUMEN", "𔓳")
    output = output.replace("FONS", "𔓶")
    output = output.replace("FORTIS", "𔐝")
    output = output.replace("FRATER2", "𔔷")
    output = output.replace("FRATER", "𔐰")
    output = output.replace("FRONS", "𔐚")
    output = output.replace("FULGUR", "𔓣")
    output = output.replace("FUSUS", "𔕗")
    output = output.replace("GENUFLECTERE", "𔑞")
    output = output.replace("GRYLLUS", "𔒑")
    output = output.replace("HASTARIUS", "𔓈")
    output = output.replace("HATTI+LI", "𔓠")
    output = output.replace("HATTUSILI", "𔓠")
    output = output.replace("HATTI", "𔓟")
    output = output.replace("HEROS", "𔐕")
    output = output.replace("HORDEUM", "𔓎")
    output = output.replace("HORREUM", "𔔡")
    output = output.replace("IACULUM", "𔕀")
    output = output.replace("INFANS", "𔐰")
    output = output.replace("INFRA", "𔐿")
    output = output.replace("ISHUWA", "𔔃")
    output = output.replace("IUDEX+la", "𔔸")
    output = output.replace("IUDEX+ra", "𔖤")
    output = output.replace("IUDEX+ri", "𔖤")
    output = output.replace("IUDEX+tara", "𔖤")
    output = output.replace("IUDEX+tari", "𔖤")
    output = output.replace("IUDEX.la", "𔔸")
    output = output.replace("IUDEX", "𔖣")
    output = output.replace("IUSTITIA", "𔖣")
    output = output.replace("JANUS", "𔒯")
    output = output.replace("LAPIS+SCALPRUM", "𔔭")
    output = output.replace("LAPIS", "𔔮")
    output = output.replace("LECTUS", "𔕓")
    output = output.replace("LEO+MONS.tu+LEO", "𔓭")
    output = output.replace("LEO", "𔑪")
    output = output.replace("LEO2", "𔑫")
    output = output.replace("LEPUS2", "𔒌")
    output = output.replace("LEPUS", "𔒋")
    output = output.replace("LIBARE", "𔐜")
    output = output.replace("LIBATIO", "𔒤")
    output = output.replace("LIGARE", "𔐠")
    output = output.replace("LINGERE", "𔒈")
    output = output.replace("LINGUA+CLAVUS", "𔓌")
    output = output.replace("LINGUA-x", "𔙅")
    output = output.replace("LINGUA", "𔓊")
    output = output.replace("LIS", "𔐘")
    output = output.replace("LITUS+na", "𔐥")
    output = output.replace("LITUUS+U", "𔒊")
    output = output.replace("LITUUS", "𔖫")
    output = output.replace("LOCUS", "𔓤")
    output = output.replace("LONGUS", "𔑄")
    output = output.replace("LOQUI", "𔐖")
    output = output.replace("LUNA", "𔓜")
    output = output.replace("MALLEUS", "𔔻")
    output = output.replace("MALUS2", "𔖠")
    output = output.replace("MALUS", "𔖟")
    output = output.replace("MANDARE2", "𔑋")
    output = output.replace("MANDARE", "𔑊")
    output = output.replace("MANUS+CULTER", "𔐻")
    output = output.replace("MANUS+MINUS", "𔑄")
    output = output.replace("MANUS.CULTER", "𔐺")
    output = output.replace("CULTER", "𔕿")
    output = output.replace("MANUS", "𔑁")
    output = output.replace("MATER", "𔑘")
    output = output.replace("MENSA2", "𔕋")
    output = output.replace("MILLE", "𔗄")
    output = output.replace("MINUS", "𔖮")
    output = output.replace("MORI", "𔖯")
    output = output.replace("MONS2", "𔐃")
    output = output.replace("MONS", "𔓬")
    output = output.replace("MURSILI", "𔔅")
    output = output.replace("NEG2", "𔕵")
    output = output.replace("NEG3", "𔕶")
    output = output.replace("NEG", "𔕴")
    output = output.replace("NEPOS", "𔕒")
    output = output.replace("OCCIDENS", "𔖬")
    output = output.replace("OCULUS", "𔐙")
    output = output.replace("OMNIS2", "𔗣")
    output = output.replace("OMNIS(+mi)", "𔖝")
    output = output.replace("OMNIS", "𔖝")
    output = output.replace("ORIENS", "𔓛")
    output = output.replace("OVIS2", "𔒆")
    output = output.replace("OVIS3", "𔒇")
    output = output.replace("OVIS", "𔒄")
    output = output.replace("PANIS.SCUTELLA", "𔗛")
    output = output.replace("PANIS", "𔓐")
    output = output.replace("PASTOR", "𔗫")
    output = output.replace("PES.REGIO", "𔔬")
    output = output.replace("mí.REGIO", "𔔇")
    output = output.replace("PES.SCALA.ROTAE", "𔑤")
    output = output.replace("PES2.PES2", "𔑨")
    output = output.replace("PES2.PES", "𔑩")
    output = output.replace("PES2", "𔑦")
    output = output.replace("PES", "𔑣")
    output = output.replace("PISCIS", "𔒥")
    output = output.replace("PITHOS.SCUTELLA", "𔕺")
    output = output.replace("PITHOS''", "𔖄")
    output = output.replace("PITHOS'", "𔕾")
    output = output.replace("PITHOS", "𔕺")
    output = output.replace("POCULUM", "𔖇")
    output = output.replace("PODIUM", "𔔪")
    output = output.replace("PONERE", "𔑇")
    output = output.replace("PORTA2", "𔔑")
    output = output.replace("PORTA", "𔔏")
    output = output.replace("POST", "𔐣")
    output = output.replace("PRAE", "𔐎")
    output = output.replace("PRINCEPS", "𔙁")
    output = output.replace("PROPHETA", "𔙀")
    output = output.replace("PUGNUS+PUGNUS", "𔐠")
    output = output.replace("PUGNUS+x", "𔐩")
    output = output.replace("PUGNUS", "𔐨")
    output = output.replace("PURUS", "𔕩")
    output = output.replace("REGIO", "𔔆")
    output = output.replace("REL", "𔕰")
    output = output.replace("REX", "𔐑")
    output = output.replace("ROTA", "𔕈")
    output = output.replace("SACERDOS2", "𔖥")
    output = output.replace("SACERDOS", "𔖐")
    output = output.replace("SARA", "𔕕")
    output = output.replace("SARI", "𔕕")
    output = output.replace("SARMA2", "𔑚")
    output = output.replace("SARMA", "𔑙")
    output = output.replace("SARPA", "𔕋")
    output = output.replace("SCRIBA", "𔕭")
    output = output.replace("SCUTELLA", "𔗆")
    output = output.replace("SCUTUM", "𔔳")
    output = output.replace("SERVUS", "𔖷")
    output = output.replace("SIGILLUM", "𔕮")
    output = output.replace("SOL", "𔓚")
    output = output.replace("SOL2.THRONUS/MENSA", "𔕌")
    output = output.replace("MENSA", "𔕊")
    output = output.replace("SOL2", "𔓙")
    output = output.replace("SOLIUM", "𔕐")
    output = output.replace("SPHINX", "𔒒")
    output = output.replace("STATUA", "𔐌")
    output = output.replace("STELE", "𔔭")
    output = output.replace("SUB", "𔐿")
    output = output.replace("SUPER", "𔑏")
    output = output.replace("TELIPINU", "𔒲")
    output = output.replace("TERRA", "𔓤")
    output = output.replace("TESHUB", "𔕥")
    output = output.replace("THRONUS''", "𔕍")
    output = output.replace("THRONUS'", "𔕋")
    output = output.replace("THRONUS2", "𔕏")
    output = output.replace("THRONUS", "𔕊")
    output = output.replace("TONITRUS", "𔓢")
    output = output.replace("UNGULA", "𔒗")
    output = output.replace("UNUS", "𔖭")
    output = output.replace("URBS+li", "𔔅")
    output = output.replace("URBS-li", "𔔅")
    output = output.replace("URBS", "𔔂")
    output = output.replace("URCEUS", "𔖆")
    output = output.replace("VACUUS", "𔔗")
    output = output.replace("VAS", "𔖂")
    output = output.replace("VERSUS", "𔐛")
    output = output.replace("VIR2.MINUS", "𔖯")
    output = output.replace("VIR2A", "𔖶")
    output = output.replace("VIR2", "𔖵")
    output = output.replace("VIR", "𔕠")
    output = output.replace("VIA+TERRA+SCALPRUM", "𔓦")
    output = output.replace("VIA+TERRA.SCALPRUM", "𔓥")
    output = output.replace("VIA", "𔓾")
    output = output.replace("SCALPRUM", "𔔯")
    output = output.replace("VITA", "𔖡")
    output = output.replace("VITELLUS", "𔒃")
    output = output.replace("VITIS", "𔒻")
    output = output.replace("WD", "𔖵")
    output = output.replace("WE", "𔗷")
    output = output.replace("zuwa", "𔕀")
    output = output.replace("ha-x", "𔕡")
    output = output.replace("hala", "𔕈")
    output = output.replace("hali", "𔕈")
    output = output.replace("hana", "𔘮")
    output = output.replace("hara", "𔕆")
    output = output.replace("hari", "𔕆")
    output = output.replace("huru", "𔗹")
    output = output.replace("hu", "𔕙")
    output = output.replace("hwi-x", "𔓎")
    output = output.replace("hwa'", "𔘰")
    output = output.replace("hwi'", "𔘰")
    output = output.replace("há-li", "𔓠")
    output = output.replace("há", "𔓟")
    output = output.replace("hí", "𔕘")
    output = output.replace("hú", "𔖈")
    output = output.replace("kar", "𔕢")
    output = output.replace("ka", "𔗧")
    output = output.replace("ki-x", "𔔓")
    output = output.replace("ki", "𔗳")
    output = output.replace("ku", "𔗜")
    output = output.replace("kwa", "𔕰")
    output = output.replace("kwi", "𔕰")
    output = output.replace("ká'", "𔐿")
    output = output.replace("ká", "𔐾")
    output = output.replace("la''", "𔗲")
    output = output.replace("la'", "𔕦")
    output = output.replace("la+la", "𔓋")
    output = output.replace("la+ra+a", "𔓍")
    output = output.replace("la-x", "𔗽")
    output = output.replace("li''", "𔗲")
    output = output.replace("li'", "𔕦")
    output = output.replace("li-x", "𔒗")
    output = output.replace("lignum", "𔖰")
    output = output.replace("lu", "𔗲")
    output = output.replace("lá", "𔓇")
    output = output.replace("lì", "𔕇")
    output = output.replace("lí'", "𔒖")
    output = output.replace("lí", "𔓇")
    output = output.replace("ma''", "𔒆")
    output = output.replace("ma'", "𔒅")
    output = output.replace("ma", "𔒄")
    output = output.replace("ma-x'", "𔘄")
    output = output.replace("ma-x", "𔒃")
    output = output.replace("mi", "𔖻")
    output = output.replace("muwa'''", "𔒁")
    output = output.replace("muwa''", "𔒀")
    output = output.replace("muwa'", "𔑿")
    output = output.replace("muwa", "𔑾")
    output = output.replace("mu''''", "𔖛")
    output = output.replace("mu'''", "𔒁")
    output = output.replace("mu''", "𔒀")
    output = output.replace("mu'", "𔑿")
    output = output.replace("mu", "𔑾")
    output = output.replace("mà", "𔕖")
    output = output.replace("má", "𔖘")
    output = output.replace("mì", "𔖷")
    output = output.replace("mí", "𔗘")
    output = output.replace("ni-x", "𔗴")
    output = output.replace("nu", "𔒴")
    output = output.replace("nà", "𔑝")
    output = output.replace("ná", "𔕵")
    output = output.replace("nì", "𔐽")
    output = output.replace("ní", "𔓵")
    output = output.replace("nú", "𔖿")
    output = output.replace("pa-x", "𔓐")
    output = output.replace("pari", "𔐎")
    output = output.replace("pi", "𔑈")
    output = output.replace("pi'", "𔑉")
    output = output.replace("pu", "𔕯")
    output = output.replace("pú", "𔗣")
    output = output.replace("ru", "𔗑")
    output = output.replace("rú''", "𔑵")
    output = output.replace("rú'", "𔑴")
    output = output.replace("rú", "𔑳")
    output = output.replace("sa-x", "𔗖")
    output = output.replace("sa4", "𔗆")
    output = output.replace("sa5", "𔕮")
    output = output.replace("sa6", "𔔀")
    output = output.replace("sa7", "𔕣")
    output = output.replace("sa8", "𔖭")
    output = output.replace("sara", "𔑏")
    output = output.replace("sari", "𔑏")
    output = output.replace("sa", "𔗔")
    output = output.replace("si", "𔓉")
    output = output.replace("su", "𔖢")
    output = output.replace("sà'''", "𔑹")
    output = output.replace("sà''", "𔑸")
    output = output.replace("sà'", "𔑷")
    output = output.replace("sà", "𔑶")
    output = output.replace("sá", "𔗦")
    output = output.replace("sí-x", "𔗾")
    output = output.replace("sú", "𔒂")
    output = output.replace("ta-x", "𔐭")
    output = output.replace("ta'", "𔑰")
    output = output.replace("ta4", "𔕦")
    output = output.replace("ta5", "𔓇")
    output = output.replace("ta6", "𔑛")
    output = output.replace("tala", "𔖞")
    output = output.replace("tana", "𔗢")
    output = output.replace("tapa'", "𔒌")
    output = output.replace("tapa", "𔒋")
    output = output.replace("tara'", "𔖸")
    output = output.replace("tara", "𔖹")
    output = output.replace("tari'", "𔖸")
    output = output.replace("tari", "𔖹")
    output = output.replace("ta", "𔑯")
    output = output.replace("ti4", "𔕦")
    output = output.replace("ti5", "𔓇")
    output = output.replace("ti", "𔑣")
    output = output.replace("tu4", "𔔆")
    output = output.replace("tuzzi", "𔔾")
    output = output.replace("tu", "𔑢")
    output = output.replace("tà'", "𔐬")
    output = output.replace("tà", "𔐫")
    output = output.replace("tá", "𔐞")
    output = output.replace("tì", "𔙄")
    output = output.replace("tí", "𔘟")
    output = output.replace("tù", "𔕭")
    output = output.replace("tú", "𔕬")
    output = output.replace("u'''", "𔖚")
    output = output.replace("u''", "𔑼")
    output = output.replace("u'", "𔑻")
    output = output.replace("urhi", "𔗘")
    output = output.replace("ur", "𔖙")
    output = output.replace("us", "𔗚")
    output = output.replace("u", "𔑺")
    output = output.replace("wa5", "𔓩")
    output = output.replace("wa5'", "𔓬")
    output = output.replace("wa6", "𔓤")
    output = output.replace("wa7", "𔕁")
    output = output.replace("wa9", "𔔻")
    output = output.replace("wi(ya)", "𔒻")
    output = output.replace("wi'", "𔒻")
    output = output.replace("wi5", "𔓩")
    output = output.replace("wi5'", "𔓬")
    output = output.replace("wi6", "𔓤")
    output = output.replace("wi7", "𔕁")
    output = output.replace("wi9", "𔔻")
    output = output.replace("wi", "𔗬")
    output = output.replace("wà", "𔓀")
    output = output.replace("wá", "𔓁")
    output = output.replace("wì", "𔓀")
    output = output.replace("wí", "𔓁")
    output = output.replace("za-x", "𔕽")
    output = output.replace("za'", "𔖩")
    output = output.replace("za4", "𔒈")
    output = output.replace("za", "𔖪")
    output = output.replace("zi4", "𔒚")
    output = output.replace("zi", "𔖩")
    output = output.replace("zà", "𔕼")
    output = output.replace("zá", "𔕹")
    output = output.replace("zì'", "𔕻")
    output = output.replace("zì", "𔕺")
    output = output.replace("zí", "𔕠")
    output = output.replace("wa", "𔗬")
    output = output.replace("hi", "𔗒")
    output = output.replace("li", "𔔹")
    output = output.replace("pa", "𔕸")
    output = output.replace("la", "𔓊")

    #  Vowels
    output = output.replace("arha'", "𔓹")
    output = output.replace("arha", "𔓸")
    output = output.replace("ha", "𔓷")
    output = output.replace("a+ra", "𔗸")
    output = output.replace("a+ri", "𔗸")
    output = output.replace("a+tá", "𔐷")
    output = output.replace("a-x", "𔗨")
    output = output.replace("ara", "𔒟")
    output = output.replace("ara'", "𔒠")
    output = output.replace("ari", "𔒟")
    output = output.replace("ari'", "𔒠")
    output = output.replace("i(a)", "𔓯")
    output = output.replace("i+ra", "𔓰")
    output = output.replace("i+ri", "𔓰")
    output = output.replace("ia", "𔓱")
    output = output.replace("ra", "𔖱")
    output = output.replace("ri", "𔖱")
    output = output.replace("na", "𔐤")
    output = output.replace("ni", "𔗐")
    output = output.replace("ià", "𔖬")
    output = output.replace("iá", "𔕑")
    output = output.replace("a", "𔗷")
    output = output.replace("i", "𔓯")
    output = output.replace("á", "𔐓")
    output = output.replace("í", "𔕐")


    # Numbers

    output = output.replace("12", "𔘍")
    output = output.replace("1", "𔖭")
    output = output.replace("1", "𔗁")
    output = output.replace("1", "𔗃")
    output = output.replace("1", "𔗄")
    output = output.replace("2'", "𔖴")
    output = output.replace("2", "𔖳")
    output = output.replace("3", "𔖸")
    output = output.replace("4", "𔖻")
    output = output.replace("5", "𔖼")
    output = output.replace("8", "𔖽")
    output = output.replace("9", "𔖿")

    output = output.replace("'", "𔖲")

    output = output.replace("<", "𔗎")
    output = output.replace(">", "𔗏")

    return output


def luwian_to_alpha(input, warnings=True):
    """ Converts text in Hieroglyphic Luwian Script to Latin Alphabet

    Some warnings might occur if a syllable has multiple values.

    Parameters
    ----------
    input : str
        Text input in Hieroglyphic Luwian Script
    warnings : bool
        Reminds that the function is VERY experimental.
        Defaults to true

    Returns
    -------
    output : str
        Transliterated text in Latin Alphabet

    Usage
    -----

    > luwian_to_alpha("𔐀𔖻  𔑻𔖱𔗒𔔹𔐤")
    + EXPECT ERRORS, THIS FUNCTION IS EXPERIMENTAL
    + EGO-4 BOS'-ra-hi-li-na
    > luwian_to_alpha("𔐀𔖻  𔑻𔖱𔗒𔔹𔐤", warnings=False) # The output is still wrong
    + EGO-4 BOS'-ra-hi-li-na
    """

    if warnings:
        print("EXPECT ERRORS, THIS FUNCTION IS EXPERIMENTAL")

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
    # a = ["MAGNUS.REX MAGNUS TONITRUS MAGNUS.REX HEROS ka ra ka mi sà REGIO REX",
         # "??? pa VIR ti sa MAGNUS.REX HEROS INFANS ní mu za",
         # "wa tu tá a CORNU ra ti REGIO LIS arha' SPHINX"]
    a = ["MAGNUS.REX MAGNUS-TONITRUS MAGNUS.REX HEROS ka-ra-ka-mi-sà REGIO REX",
         "???-pa-VIR-ti-sa MAGNUS.REX HEROS INFANS-ní-mu-za",
         "wa-tu-tá-a CORNU-ra-ti REGIO LIS arha'-SPHINX"]
    b = [alpha_to_luwian(i) for i in a]
    for i in b:
        print(i)

    # for i in b:
        # print(luwian_to_alpha(i))

