#! /usr/bin python3

""" Avestan script converter

The transliteration scheme is as follows:

        a		𐬀
        A		𐬁
        á		𐬂
        Á		𐬃
        ã		𐬄
        ãã		𐬅
        æ		𐬆
        Æ		𐬇
        e		𐬈
        E		𐬉
        o		𐬊
        O		𐬋
        i		𐬌
        I		𐬍
        u		𐬎
        U		𐬏
        k		𐬐
        x		𐬑
        X		𐬒
        xw		𐬓
        g		𐬔
        G		𐬕
        gh		𐬖
        c		𐬗
        j		𐬘
        t		𐬙
        th		𐬚
        d		𐬛
        dh		𐬜
        T		𐬝
        p		𐬞
        f		𐬟
        b		𐬠
        B		𐬡
        ng		𐬢
        ngh	        𐬣
        ngw     	𐬤
        n		𐬥
        ñ		𐬦
        N		𐬧
        m		𐬨
        M		𐬩
        Y		𐬪
        y		𐬫
        v		𐬬
        r		𐬭
        s		𐬯
        z		𐬰
        sh		𐬱
        zh		𐬲
        shy     	𐬳
        S		𐬴
        h		𐬵

"""

from tools import get_key



def alpha_to_avestan(input):
    """ Converts text in Latin Alphabet to Avestan Script

    Each syllable should be separated by a sing dash, each word by a space.

    Parameters
    ----------
    input : str
        Text input with syllables separated by dashes and words by spaces.

    Returns
    -------
    output : str
        Transliterated text in Avestan Script

    Usage
    -----
    
    > alpha_to_avestan("<++>")
    + 

    """
    # print(input.translate(script))

    output = input
    output = output.replace("A", "𐬁")
    output = output.replace("aa", "𐬀")
    output = output.replace("a", "𐬀")
    output = output.replace("Á", "𐬃")
    output = output.replace("áá", "𐬂")
    output = output.replace("á", "𐬂")
    output = output.replace("ãã", "𐬅")
    output = output.replace("ã", "𐬄")
    output = output.replace("ææ", "𐬆")
    output = output.replace("æ", "𐬆")
    output = output.replace("Æ", "𐬇")
    output = output.replace("ee", "𐬈")
    output = output.replace("e", "𐬈")
    output = output.replace("E", "𐬉")
    output = output.replace("oo", "𐬊")
    output = output.replace("o", "𐬊")
    output = output.replace("O", "𐬋")
    output = output.replace("i", "𐬌")
    output = output.replace("I", "𐬍")
    output = output.replace("u", "𐬎")
    output = output.replace("U", "𐬏")
    output = output.replace("k", "𐬐")
    output = output.replace("X", "𐬒")
    output = output.replace("xw", "𐬓")
    output = output.replace("x", "𐬑")
    output = output.replace("c", "𐬗")
    output = output.replace("j", "𐬘")
    output = output.replace("th", "𐬚")
    output = output.replace("t", "𐬙")
    output = output.replace("dh", "𐬜")
    output = output.replace("d", "𐬛")
    output = output.replace("T", "𐬝")
    output = output.replace("p", "𐬞")
    output = output.replace("f", "𐬟")
    output = output.replace("b", "𐬠")
    output = output.replace("B", "𐬡")
    output = output.replace("ngh", "𐬣")
    output = output.replace("ngw", "𐬤")
    output = output.replace("ng", "𐬢")
    output = output.replace("gh", "𐬖")
    output = output.replace("g", "𐬔")
    output = output.replace("G", "𐬕")
    output = output.replace("ñ", "𐬦")
    output = output.replace("n", "𐬥")
    output = output.replace("N", "𐬧")
    output = output.replace("m", "𐬨")
    output = output.replace("M", "𐬩")
    output = output.replace("Y", "𐬪")
    output = output.replace("y", "𐬫")
    output = output.replace("v", "𐬬")
    output = output.replace("r", "𐬭")
    output = output.replace("sh", "𐬱")
    output = output.replace("zh", "𐬲")
    output = output.replace("shy", "𐬳")
    output = output.replace("S", "𐬴")
    output = output.replace("s", "𐬯")
    output = output.replace("z", "𐬰")
    output = output.replace("h", "𐬵")

    return output


if __name__ == "__main__":
       a = """
       paoiriiáá dasa xshpanoo
       spitama zarathushtra
       tishtrioo raeeuuáá xwarænangwháá
       """
       b = alpha_to_avestan(a)
       print(b)
